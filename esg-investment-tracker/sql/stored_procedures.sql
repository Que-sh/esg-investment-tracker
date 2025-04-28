USE ESGInvestmentDB;
GO

-- Stored Procedure 1: Compute Weighted ESG Score
CREATE OR ALTER PROCEDURE sp_GetWeightedESGScore
AS
BEGIN
    SELECT 
        SUM(esg_score * investment_amount) / NULLIF(SUM(investment_amount), 0) AS weighted_esg_score
    FROM Investments;
END;
GO

-- Stored Procedure 2: Compute Total Returns
CREATE OR ALTER PROCEDURE sp_GetTotalReturns
AS
BEGIN
    SELECT 
        SUM(investment_amount * (annual_return / 100)) AS total_annual_return
    FROM Investments;
END;
GO

-- Stored Procedure 3: Get Investment Summary (for Python visualization)
CREATE OR ALTER PROCEDURE sp_GetInvestmentSummary
AS
BEGIN
    SELECT 
        bond_id,
        name,
        esg_score,
        annual_return,
        investment_amount
    FROM Investments;
END;
GO