create database esg_proj
use esg_proj
select * from esg_cleaned;
select top 5 * from esg_cleaned;
-- which region has the highest average esg performance
SELECT Region,ROUND(AVG(ESG_Overall),2) AS Avg_ESG_Score FROM esg_cleaned GROUP BY Region ORDER BY Avg_ESG_Score DESC;
--Which industry produces the highest emissions?
