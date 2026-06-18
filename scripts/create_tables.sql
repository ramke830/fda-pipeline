-- FDA Drug Adverse Events Database Schema
-- MADSC301 Business Intelligence
-- Ramakrishna Lavoori - 25056894

CREATE TABLE IF NOT EXISTS drug_events (
    id SERIAL PRIMARY KEY,
    report_id VARCHAR(50),
    country VARCHAR(100),
    serious VARCHAR(20),
    drug_name VARCHAR(200),
    reaction VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Useful views for analysis
CREATE OR REPLACE VIEW top_drugs AS
SELECT drug_name, COUNT(*) as report_count
FROM drug_events
GROUP BY drug_name
ORDER BY report_count DESC
LIMIT 10;

CREATE OR REPLACE VIEW serious_summary AS
SELECT serious, COUNT(*) as count,
ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) as percentage
FROM drug_events
GROUP BY serious;

CREATE OR REPLACE VIEW top_reactions AS
SELECT reaction, COUNT(*) as count
FROM drug_events
GROUP BY reaction
ORDER BY count DESC
LIMIT 10;