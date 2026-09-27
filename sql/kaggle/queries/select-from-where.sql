-- Reviewed extraction from notebooks/select-from-where.ipynb.
-- The original closing single quote was corrected to a backtick.
-- Not executed; current source-table availability has not been verified.
-- Returns one city value per matching row, including possible duplicates.
SELECT city
FROM `bigquery-public-data.openaq.global_air_quality`
WHERE country = 'US';
