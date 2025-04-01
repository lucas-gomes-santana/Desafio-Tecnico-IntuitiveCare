CREATE DATABASE IF NOT EXISTS ans_demonstracoes CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ans_demonstracoes;


CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    DATA DATE NOT NULL COMMENT 'Data do registro contábil',
    REG_ANS VARCHAR(6) NOT NULL COMMENT 'Registro ANS da operadora',
    CD_CONTA_CONTABIL VARCHAR(20) NOT NULL COMMENT 'Código da conta contábil',
    DESCRICAO TEXT COMMENT 'Descrição detalhada da conta contábil',
    VL_SALDO_INICIAL DECIMAL(15,2) COMMENT 'Valor do saldo inicial do período',
    VL_SALDO_FINAL DECIMAL(15,2) COMMENT 'Valor do saldo final do período',
    
    INDEX idx_data (DATA),
    INDEX idx_reg_ans (REG_ANS),
    INDEX idx_conta (CD_CONTA_CONTABIL),
    INDEX idx_data_reg_ans (DATA, REG_ANS),
    INDEX idx_conta_desc (CD_CONTA_CONTABIL, DESCRICAO(100))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
