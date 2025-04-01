from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import pandas as pd
from pathlib import Path
import zipfile
import os
from typing import List, Dict, Any

app = FastAPI()

BASE_DIR = Path(__file__).parent.absolute()
ANEXOS_DIR = BASE_DIR.parent / "Anexos"
ZIP_FILE = ANEXOS_DIR / "Teste_Lucas_Gomes_Santana.zip"
CSV_FILE = ANEXOS_DIR / "Rol_Procedimentos.csv"


# Configura o CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Extrai a planilha.csv do ZIP se necessário
def extrair_csv():
    if not CSV_FILE.exists() and ZIP_FILE.exists():
        with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
            zip_ref.extractall(ANEXOS_DIR)

@app.on_event("startup")
async def startup_event():
    extrair_csv()
    if not CSV_FILE.exists():
        raise RuntimeError(f"Arquivo CSV não encontrado: {CSV_FILE}")

@app.get("/api/buscar", response_model=List[Dict[str, Any]])
async def buscar_procedimentos(termo: str, limite: int = 10):

    try:
        df = pd.read_csv(CSV_FILE, encoding='utf-8-sig')
        mask = df.apply(
            lambda row: row.astype(str).str.contains(termo, case=False).any(),
            axis=1
        )
        resultados = df[mask].head(limite)
        return resultados.fillna('').to_dict(orient='records')
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)