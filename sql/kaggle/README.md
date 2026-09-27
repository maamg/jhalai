# Kaggle SQL Practice

A collection of saved SQL learning notebooks by Abdul Aziz.

## Exercise index

| Exercise | Concepts | Status |
| --- | --- | --- |
| [Select, From, Where](notebooks/select-from-where.ipynb) | Select a column, identify a table, filter rows | Original incomplete notebook; no saved results |
| [Reviewed SQL query](queries/select-from-where.sql) | Same query with matching identifier quotes | Syntax correction only; not executed against BigQuery |

## Select, From, Where

**Question:** Which values in the `city` column occur in rows whose `country` is `US`?

The notebook references `bigquery-public-data.openaq.global_air_quality`. This is the table named in the saved exercise; its current availability and schema have not been verified.

- `SELECT city` returns the city column.
- `FROM` identifies the source table.
- `WHERE country = 'US'` keeps rows with that country value.
- There is no `DISTINCT`, so repeated city values may appear.
- There is no `ORDER BY`, so no particular result order is requested.

## Original and reviewed versions

The original notebook is preserved byte-for-byte from the uploaded file. The separate SQL file fixes the mismatched table-name closing quote (a single quote instead of a backtick) and adds a terminating semicolon. These edits were made during repository organisation; the SQL file is not a separate historical exercise.

The notebook still needs:
1. `from google.cloud import bigquery` before creating the client.
2. A correctly configured BigQuery project and authentication.
3. The matching closing backtick in the query.
4. A result-retrieval step after `client.query(query)`.

The original variable name is `qurey_job`. This is a spelling issue, not itself a syntax error; any subsequent reference must use the same name, or both should be renamed consistently.

## Reproduction and evidence

Use the reviewed query in an authorised BigQuery environment with access to the referenced table. Query execution may consume BigQuery quota or incur charges depending on configuration. No cloud queries were run during this import.

The uploaded notebook contains no saved outputs or execution evidence. Result samples have not been invented. The original Kaggle notebook URL and precise course attribution were not included in the file and can be added when available.

## Files

- [Original notebook](notebooks/select-from-where.ipynb)
- [Reviewed SQL](queries/select-from-where.sql)
- [All SQL practice](../README.md)
- [Programming collection](../../README.md)
