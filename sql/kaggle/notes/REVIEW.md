# Review notes

## Preservation

Five new, distinct notebooks were added under descriptive filenames, retaining their original bytes, cells and saved outputs. The previously imported SELECT draft remains at its original GitHub path. Two exact duplicate uploads were not added again. SHA-256 hashes and filename mappings are in [IMPORT-MAP.md](../IMPORT-MAP.md).

## Findings

- **BigQuery walkthrough:** the table-list comment says there are four tables, but the saved output lists only `full`. The last cell's comment says it previews `by`; the code selects `table.schema[:1]` and its saved output is actually `title`. Original source is retained.
- **Schema practice:** a separate, expanded attempt with Bengali notes, explicit field-name/type inspection and different preview sizes. It is not a duplicate of the walkthrough.
- **Chicago Crime exercises:** saved checker outputs say Correct for Q1, Q2 and Q3. A saved hint is also present. Identifying latitude/longitude is completed; no crime map is actually plotted.
- **Chicago Crime alternate attempt:** Q1 has a saved Correct result. Q2/Q3 still contain placeholders. The raw SQL cell is invalid as ordinary Python. A saved AttributeError occurs at Q3, and solution output is present elsewhere. This notebook is retained as a separate attempt; the upload does not establish which attempt was chronologically first.
- **OpenAQ template:** unanswered `____` placeholders remain; saved setup output is not evidence that the exercise was solved.
- **SELECT draft:** missing BigQuery import, mismatched identifier quote, misspelled `qurey_job` variable and unfinished result retrieval. Details are [here](select-from-where.md).

## Validation scope

Notebook JSON and code cells were inspected. Python parsing flagged the alternate attempt's raw SQL cell, as expected. Placeholders and undefined names may parse successfully but still fail at runtime. No notebook was executed, no course checks were rerun, and no query results were invented.
