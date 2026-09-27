# Kaggle SQL and BigQuery Practice

Saved learning work by Abdul Aziz: dataset exploration, schema inspection and introductory SQL. Six distinct notebooks are retained after comparing eight uploaded files (including the notebook imported earlier).

## Start here

**[Chicago Crime exercises](notebooks/03-chicago-crime-exercises.ipynb)** contain saved Kaggle checker results marked **Correct** for all three questions: counting tables, counting TIMESTAMP fields, and identifying latitude/longitude fields for mapping. This is course-exercise evidence from the saved notebook, not a fresh run or an independent research project.

## Learning sequence

| Step | Notebook | What it demonstrates | Saved evidence / status |
| --- | --- | --- | --- |
| 1 | [BigQuery walkthrough](notebooks/01-bigquery-hacker-news-walkthrough.ipynb) | Client, dataset/table references, Hacker News schema and row previews | Schema and dataframe outputs saved |
| 2 | [Schema practice](notebooks/02-hacker-news-schema-practice.ipynb) | Column names/types, field selection, Bengali learning notes | Schema, printed fields and dataframe outputs saved |
| 3 | [Chicago Crime exercises](notebooks/03-chicago-crime-exercises.ipynb) | Table count, TIMESTAMP field count, mapping fields | Three saved Correct results |
| 4 | [SELECT–FROM–WHERE draft](notebooks/select-from-where.ipynb) | City selection and country filtering | Incomplete; no saved result |

## Supporting material

- [Chicago Crime alternate attempt](drafts/chicago-crime-alternate-attempt.ipynb): a different attempt, not a duplicate. Q1 has a saved Correct result; Q2/Q3 are unfinished. Raw SQL appears in a Python cell. Saved solution/hint feedback is retained.
- [OpenAQ exercise template](templates/openaq-select-where-exercises.ipynb): setup output is saved, but answer placeholders remain. It is not presented as solved work.
- [Reviewed SELECT query](queries/select-from-where.sql): previously extracted query with corrected identifier quoting; not executed.
- [Extracted schema-count query](queries/chicago-crime-timestamp-fields.sql): SQL from the alternate attempt, placed in a SQL file; not executed.
- [SELECT draft details](notes/select-from-where.md)
- [Review notes](notes/REVIEW.md)
- [Duplicate decisions and original filenames](IMPORT-MAP.md)

## Sources and execution

The Chicago Crime and OpenAQ exercise notebooks link to [Kaggle Learn — Intro to SQL](https://www.kaggle.com/learn/intro-to-sql). Original course prompts, credits, hints and solutions remain in their notebooks. Course scaffolding is not claimed as independently authored work. The original public URLs for the user's individual notebooks were not supplied.

Open these notebooks on Kaggle with the appropriate BigQuery integration and, for exercise checkers, Kaggle `learntools`. Outside Kaggle, BigQuery authentication/project setup and the relevant Python dependencies are required. Dataset availability and cloud execution were not rechecked during this organisation pass.

Existing output cells are historical evidence from the uploaded files. They were not regenerated. No cloud queries were executed and no missing answers were filled in.

[All SQL practice](../README.md) · [Programming collection](../../README.md)
