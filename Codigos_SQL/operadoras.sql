-- Criar o banco de dados
CREATE DATABASE IF NOT EXISTS operadoras CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE operadoras;

-- Criar a tabela operadoras_ativas (Dados das operadoras)
CREATE TABLE IF NOT EXISTS operadoras_info (
    Registro_ANS VARCHAR(6),
    CNPJ VARCHAR(14),
    Razao_Social VARCHAR(140),
    Nome_Fantasia VARCHAR(140),
    Modalidade VARCHAR(2),
    Logradouro VARCHAR(40),
    Numero VARCHAR(20),
    Complemento VARCHAR(40),
    Bairro VARCHAR(30),
    Cidade VARCHAR(30),
    UF VARCHAR(2),
    CEP VARCHAR(8),
    DDD VARCHAR(4),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(50),
    Cargo_Representante VARCHAR(40),
    Regiao_de_Comercializacao INT,
    Data_Registro_ANS DATE,
    
    PRIMARY KEY (Registro_ANS),
    INDEX idx_cnpj (CNPJ),
    INDEX idx_uf (UF),
    INDEX idx_regiao (Regiao_de_Comercializacao)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE IF NOT EXISTS operadoras_financeiro (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    REG_ANS INT NOT NULL,
    CD_CONTA_CONTABIL VARCHAR(20) NOT NULL,
    DESCRICAO VARCHAR(255) NOT NULL,
    VL_SALDO_INICIAL DECIMAL(15,2) NOT NULL,
    VL_SALDO_FINAL DECIMAL(15,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
