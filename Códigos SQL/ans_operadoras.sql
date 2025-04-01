CREATE DATABASE IF NOT EXISTS ans_operadoras CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ans_operadoras;


CREATE TABLE IF NOT EXISTS operadoras_ativas (
    REGISTRO_OPERADORA VARCHAR(6) COMMENT 'Registro de operadora de plano privado de assistência à saúde concedido pela ANS',
    CNPJ VARCHAR(14) COMMENT 'CNPJ da Operadora',
    Razao_Social VARCHAR(140) COMMENT 'Razão Social da Operadora',
    Nome_Fantasia VARCHAR(140) COMMENT 'Nome Fantasia da Operadora',
    Modalidade VARCHAR(2) COMMENT 'Classificação das operadoras de planos privados de assistência à saúde',
    Logradouro VARCHAR(40) COMMENT 'Endereço da Sede da Operadora',
    Número VARCHAR(20) COMMENT 'Número do Endereço da Sede da Operadora',
    Complemento VARCHAR(40) COMMENT 'Complemento do Endereço da Sede da Operadora',
    Bairro VARCHAR(30) COMMENT 'Bairro do Endereço da Sede da Operadora',
    Cidade VARCHAR(30) COMMENT 'Cidade do Endereço da Sede da Operadora',
    UF VARCHAR(2) COMMENT 'Estado do Endereço da Sede da Operadora',
    CEP VARCHAR(8) COMMENT 'CEP do Endereço da Sede da Operadora',
    DDD VARCHAR(4) COMMENT 'Código de DDD da Operadora',
    Telefone VARCHAR(20) COMMENT 'Número de Telefone da Operadora',
    Fax VARCHAR(20) COMMENT 'Número de Fax da Operadora',
    Endereco_eletronico VARCHAR(255) COMMENT 'E-mail da Operadora',
    Representante VARCHAR(50) COMMENT 'Representante Legal da Operadora',
    Cargo_Representante VARCHAR(40) COMMENT 'Cargo do Representante Legal da Operadora',
    Regiao_de_Comercializacao INT COMMENT 'Área onde a operadora comercializa seu plano de saúde (1-6 conforme normas ANS)',
    Data_Registro_ANS DATE COMMENT 'Data do Registro da Operadora na ANS (formato AAAA-MM-DD)',
    
    PRIMARY KEY (REGISTRO_OPERADORA),
    INDEX idx_cnpj (CNPJ),
    INDEX idx_uf (UF),
    INDEX idx_regiao (Regiao_de_Comercializacao)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
