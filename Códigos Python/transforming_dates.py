import os
import zipfile
import pandas as pd
import pdfplumber
from pathlib import Path

# Configuração de caminhos
BASE_DIR = Path(__file__).parent
ANEXOS_DIR = BASE_DIR.parent / "Anexos"
ANEXO_I_PDF = ANEXOS_DIR / "Anexo_I.pdf"
OUTPUT_CSV = ANEXOS_DIR / "Rol_Procedimentos.csv"
OUTPUT_ZIP = ANEXOS_DIR / "Teste_Lucas_Gomes_Santana.zip"

def extrair_tabelas_pdf(pdf_path):
    """Extrai tabelas do PDF com configurações personalizadas"""
    todas_linhas = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for pagina in pdf.pages:
            # Configurações para melhor extração
            settings = {
                "vertical_strategy": "lines",
                "horizontal_strategy": "text",
                "intersection_y_tolerance": 10
            }
            
            tabelas = pagina.extract_tables(settings)
            
            for tabela in tabelas:
                for linha in tabela:
                    # Filtra linhas válidas
                    if any(celula and str(celula).strip() for celula in linha):
                        todas_linhas.append(linha)
    
    return todas_linhas

def identificar_cabecalho(linhas):
    """Identifica o cabeçalho baseado no conteúdo"""
    for i, linha in enumerate(linhas):
        if "Código" in str(linha) and ("OD" in str(linha)) or ("AMB" in str(linha)):
            return i, linha
    return None, None

def processar_dados(linhas):
    """Processa e estrutura os dados"""
    idx_cabecalho, cabecalho = identificar_cabecalho(linhas)
    
    if not cabecalho:
        # Cabeçalho padrão caso não seja encontrado
        cabecalho = ["Código", "Descrição", "OD", "AMB", "HC", "HS", "REF", "PAC", "DUT", "Subgrupo", "Grupo", "Capítulo"]
        dados = [linha for linha in linhas if len(linha) >= 4]  # Pelo menos 4 colunas
    else:
        dados = linhas[idx_cabecalho+1:]
    
    # Filtra linhas válidas
    dados = [linha for linha in dados if len(linha) > 1 and linha[0] and str(linha[0]).strip()]
    
    return cabecalho, dados

def salvar_dados(cabecalho, dados):
    """Salva os dados processados"""
    df = pd.DataFrame(dados, columns=cabecalho)
    
    # Substitui abreviações
    df.columns = df.columns.str.replace('OD', 'Seg. Odontológica')
    df.columns = df.columns.str.replace('AMB', 'Seg. Ambulatorial')
    
    # Salva CSV
    df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8-sig')
    
    # Compacta
    with zipfile.ZipFile(OUTPUT_ZIP, 'w') as zipf:
        zipf.write(OUTPUT_CSV, arcname=OUTPUT_CSV.name)

def main():
    print("=== PROCESSAMENTO DO ANEXO I ===")
    
    # Extrai tabelas
    print("Extraindo dados do PDF...")
    linhas = extrair_tabelas_pdf(ANEXO_I_PDF)
    
    # Processa dados
    print("Processando dados...")
    cabecalho, dados = processar_dados(linhas)
    
    # Salva resultados
    print("Salvando resultados...")
    salvar_dados(cabecalho, dados)
    
    print(f"""
    Processo concluído com sucesso!
    Arquivo CSV gerado: {OUTPUT_CSV}
    Arquivo ZIP criado: {OUTPUT_ZIP}
    """)

if __name__ == "__main__":
    main()