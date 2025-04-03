import zipfile
import pandas as pd
import pdfplumber
from pathlib import Path
import os


BASE_DIR = Path(__file__).parent
ANEXOS_DIR = BASE_DIR.parent / "Outros_Arquivos" / "Anexos"
OUTROS_ARQUIVOS_DIR = BASE_DIR.parent / "Outros_Arquivos"
ANEXOS_ZIP = ANEXOS_DIR / "Anexos_Compactados.zip"
ANEXO_I_PDF = ANEXOS_DIR / "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
ANEXO_II_PDF = ANEXOS_DIR / "Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
OUTPUT_CSV = ANEXOS_DIR / "Procedimentos.csv"
OUTPUT_ZIP = OUTROS_ARQUIVOS_DIR / "Teste_Lucas_Gomes_Santana.zip"


# Deleta os anexos para ficar apenas o zip
def excluir_arquivos():
    arquivos_para_remover = [ANEXO_I_PDF, ANEXO_II_PDF, OUTPUT_CSV]
    
    for arquivo in arquivos_para_remover:
        try:
            if arquivo.exists():
                os.remove(arquivo)
                print(f"Arquivo removido: {arquivo.name}")
        except Exception as e:
            print(f"Erro ao remover {arquivo.name}: {e}")

# Descompacta o zip
def descompactar_zip():
    with zipfile.ZipFile(ANEXOS_ZIP, 'r') as zip_ref:
        zip_ref.extractall(ANEXOS_DIR)
    print(f"{ANEXOS_ZIP.name} descompactado")

# Extrai dados do PDF
def extrair_tabelas():
    with pdfplumber.open(ANEXO_I_PDF) as pdf:
        todas_linhas = []
        for pagina in pdf.pages:
            tabelas = pagina.extract_tables({
                "vertical_strategy": "lines",
                "horizontal_strategy": "text"
            })
            for tabela in tabelas:
                todas_linhas.extend(linha for linha in tabela if any(celula and str(celula).strip() for celula in linha))
    
    cabecalho = ["Código", "Descrição", "Seg. Odontológica", "Seg. Ambulatorial", 
                 "HC", "HS", "REF", "PAC", "DUT", "Subgrupo", "Grupo", "Capítulo"]
    dados = [linha for linha in todas_linhas if len(linha) > 1 and str(linha[0]).strip()]
    
    return cabecalho, dados

def main():
    print("=== PROCESSO INICIADO ===")
    try:
        descompactar_zip()
        
        cabecalho, dados = extrair_tabelas()
        pd.DataFrame(dados, columns=cabecalho).to_csv(OUTPUT_CSV, index=False, encoding='utf-8-sig')
        
        with zipfile.ZipFile(OUTPUT_ZIP, 'w') as zipf:
            zipf.write(OUTPUT_CSV, arcname=OUTPUT_CSV.name)
        print(f"✅ {OUTPUT_ZIP.name} criado em: {OUTPUT_ZIP.parent}")

        excluir_arquivos()
        
    except Exception as e:
        print(f"Erro durante o processo: {e}")

    finally:
        print("=== PROCESSO FINALIZADO ===")

if __name__ == "__main__":
    main()