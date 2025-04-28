CREATE DATABASE ESGInvestmentDB;
GO

USE ESGInvestmentDB;
GO

CREATE TABLE Investments (
    bond_id VARCHAR(50) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    esg_score FLOAT NOT NULL CHECK (esg_score >= 0 AND esg_score <= 100),
    annual_return FLOAT NOT NULL CHECK (annual_return >= -100),
    investment_amount DECIMAL(18, 2) NOT NULL CHECK (investment_amount >= 0),
    issue_date DATE NOT NULL
);
GO

-- Insert sample data for testing
INSERT INTO Investments (bond_id, name, esg_score, annual_return, investment_amount, issue_date)
VALUES 
    ('BOND001', 'Green Energy Bond', 85.5, 4.2, 10000.00, '2023-01-15'),
    ('BOND002', 'Sustainable Infra Bond', 78.0, 3.8, 15000.00, '2023-06-20'),
    ('BOND003', 'Eco Housing Bond', 92.0, 5.1, 8000.00, '2024-02-10'),
    ('BOND004', 'Renewable Energy Bond', 88.5, 4.5, 12000.00, '2024-07-05');
GO