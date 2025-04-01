SELECT 
    o.Razao_Social,
    o.Nome_Fantasia,
    o.UF,
    SUM(d.VL_SALDO_FINAL) AS total_despesas,
    COUNT(DISTINCT d.DATA) AS meses_considerados
FROM 
    ans_demonstracoes.demonstracoes_contabeis d
JOIN 
    ans_operadoras.operadoras_ativas o ON d.REG_ANS = o.REGISTRO_OPERADORA
WHERE 
    d.CD_CONTA_CONTABIL LIKE '%EVENTOS/%SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    AND d.DATA >= DATE_SUB(DATE_FORMAT(CURRENT_DATE, '%Y-%m-01'), INTERVAL 3 MONTH)
    AND d.DATA < DATE_FORMAT(CURRENT_DATE, '%Y-%m-01')
GROUP BY 
    o.Razao_Social, o.Nome_Fantasia, o.UF
ORDER BY 
    total_despesas DESC
LIMIT 10;