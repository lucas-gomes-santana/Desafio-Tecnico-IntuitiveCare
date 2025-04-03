SELECT REG_ANS, SUM(VL_SALDO_FINAL - VL_SALDO_INICIAL) AS Total_Despesas
FROM operadoras_financeiro
WHERE DESCRICAO LIKE '%SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO-HOSPITALAR%'
AND DATA_REGISTRO BETWEEN DATE_SUB(CURDATE(), INTERVAL 1 YEAR) AND CURDATE()
GROUP BY REG_ANS
ORDER BY Total_Despesas DESC
LIMIT 10;
