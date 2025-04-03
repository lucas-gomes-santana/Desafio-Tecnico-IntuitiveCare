from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pathlib import Path
import zipfile
from typing import List, Dict, Any

app = FastAPI()


BASE_DIR = Path(__file__).parent.absolute()
OUTROS_ARQUIVOS_DIR = BASE_DIR.parent / "Outros_Arquivos"
ZIP_FILE = OUTROS_ARQUIVOS_DIR / "Teste_Lucas_Gomes_Santana.zip"  # ZIP na raiz
CSV_FILE = OUTROS_ARQUIVOS_DIR / "Procedimentos.csv"  # CSV extraído aqui

# Configura o CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Extrai o csv do zip
def extrair_zip_completo():
    if ZIP_FILE.exists():
        with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
            zip_ref.extractall(OUTROS_ARQUIVOS_DIR)  # Extrai tudo aqui
        print(f"✅ ZIP descompactado. Arquivos extraídos em: {OUTROS_ARQUIVOS_DIR}")
        
        if not CSV_FILE.exists():
            raise FileNotFoundError(f"Arquivo CSV não encontrado após extração do ZIP")
    else:
        raise FileNotFoundError(f"Arquivo ZIP não encontrado: {ZIP_FILE}")

@app.on_event("startup")
async def startup_event():
    try:
        extrair_zip_completo()
        # Testa a leitura do CSV
        pd.read_csv(CSV_FILE, encoding='utf-8-sig').head()
        print("🟢 API pronta para buscas")
    except Exception as e:
        raise RuntimeError(f"Falha na inicialização: {str(e)}")

@app.get("/api/buscar", response_model=List[Dict[str, Any]])
async def buscar_procedimentos(termo: str, limite: int = 10):
    try:
        df = pd.read_csv(CSV_FILE, encoding='utf-8-sig')
        mask = df.apply(
            lambda row: row.astype(str).str.contains(termo, case=False).any(),
            axis=1
        )
        return df[mask].head(limite).fillna('').to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na busca: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)