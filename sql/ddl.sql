IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'AgroAnalytics')
BEGIN
    CREATE DATABASE AgroAnalytics;
END;
GO

USE AgroAnalytics;
GO

IF OBJECT_ID('dbo.stg_agro_producao') IS NOT NULL
    DROP TABLE dbo.stg_agro_producao;

CREATE TABLE dbo.stg_agro_producao (
    id INT IDENTITY(1,1) PRIMARY KEY,
    ano INT,
    estado_codigo INT,
    estado VARCHAR(100),
    produto_codigo INT,
    produto VARCHAR(150),
    valor DECIMAL(18,2)
);


IF OBJECT_ID('dbo.agro_producao_anual') IS NOT NULL
    DROP TABLE dbo.agro_producao_anual;

CREATE TABLE dbo.agro_producao_anual (
    ano INT,
    produto VARCHAR(150),
    producao_total DECIMAL(18,2)
);
