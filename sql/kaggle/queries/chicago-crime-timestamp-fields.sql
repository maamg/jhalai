-- Extracted from drafts/chicago-crime-alternate-attempt.ipynb.
-- Originally entered as raw SQL in a Python code cell.
-- Query logic preserved; not executed during organisation.
SELECT COUNT(*)
FROM `bigquery-public-data.chicago_crime.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name = 'crime' AND data_type = 'TIMESTAMP';
