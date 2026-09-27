# Programming Learning Archive

This is the rescued historical record of my programming practice. The clear English repository names linked below are the curated views intended for academic readers. The former personal label `Jhalai (ঝালাই)` can remain in the commit history or rename redirect, but it is not the public-facing title.

This repository is a learning portfolio: a record of how I have learned to use code step by step for geography, GIS, remote sensing, data work and everyday automation.

It is meant to help a professor or research supervisor understand my programming background. It is not presented as a professional software-engineering portfolio or as a production application.

## Start here for a supervisor

The curated domain repositories will be the quickest route for a professor. This archive remains the provenance record: older attempts, course structure and incomplete work are kept visible rather than presented as polished software.

| Domain | Curated repository | Evidence in this archive |
| --- | --- | --- |
| Python foundations | python-foundations | python/fundamentals/, python/string-list-methods/ and python/subin/ |
| Python course practice | python-code-in-place | python/code-in-place/ |
| Python projects | python-100-days-projects | python/100-days/ (excluding OOP) |
| Python OOP | python-object-oriented-practice | python/100-days/oop in python/, python/oop-basics/ and python/oop-harry/ |
| Python statistics | python-statistics-practice | python/statistics/ |
| KoBo automation | kobo-form-automation | automation/kobo/ |
| SQL and BigQuery | sql-kaggle-practice | sql/ |
| Earth Engine / remote sensing | earth-engine-remote-sensing | gee/ |
| JavaScript and web | javascript-web-foundations | related legacy repositories |
| R and statistics | r-statistics-practice | r/ and python/statistics/ |

1. [Learning map](#learning-map) — the progression across programming areas.
2. [Earth Engine learning evidence](gee/) — Code Editor JavaScript exercises and the showcase format for future scripts.
3. [SQL and BigQuery evidence](sql/kaggle/) — Kaggle notebooks, saved checker results and clearly labelled incomplete work.
4. [Python archive](python/) — the original course grouping; curated stage repositories use one-level layouts.

## Learning map

| Stage | Evidence in this collection | What it shows |
| --- | --- | --- |
| Programming foundations | [Python practice](python/) | Variables, conditions, loops, functions, data structures, OOP and small problem-solving exercises |
| Querying and data inspection | [SQL and BigQuery](sql/kaggle/) | Dataset/schema inspection, SELECT–FROM–WHERE practice and introductory analytical queries |
| Geospatial scripting | [Google Earth Engine](gee/) | JavaScript in the Earth Engine Code Editor, image-collection filtering and the structure used for future remote-sensing workflows |
| Analysis and statistics | [Python statistics](python/statistics/) and [R](r/) | Descriptive work, normality/Q–Q examples, data frames and file imports |
| Research support and automation | [KoBo automation](automation/kobo/) | A small pandas-based workflow for generating a KoBo XLSForm |
| Web and presentation practice | [HTML practice](web/) | Basic pages and visual presentation exercises |

The collection keeps earlier attempts so the progression is visible. Course exercises, templates, unfinished attempts and personal adaptations are labelled in their folder READMEs; course scaffolding is not claimed as independent research.

## How to read the Earth Engine work

The files in gee/ are exported source files that can be read on GitHub. A finished Code Editor script should also have a short project note and a snapshot link from Earth Engine's Get Link action. Use [the showcase template](gee/SHOWCASE_TEMPLATE.md) for each substantial script.

A useful project entry answers five questions:

- What research or learning question does the script address?
- Which dataset, date range and study area are used?
- What preprocessing and method are applied?
- What output or validation evidence was produced?
- Where are the GitHub source and Earth Engine Code Editor links?

## Organisation

Course groups remain together so local imports continue to resolve. Original script names and code are preserved. The import inventory records the destination or exclusion reason for every original file.

Books, lecture slides, certificates, editor state, downloaded pages and local datasets are not part of this public learning record. Third-party code retains its existing attribution; see [THIRD-PARTY.md](THIRD-PARTY.md).

[File catalogue](docs/FILE-CATALOG.md) · [Setup notes](docs/SETUP.md) · [Known issues](docs/KNOWN-ISSUES.md) · [All my GitHub projects](https://github.com/maamg/maamg/blob/main/PROJECTS.md)
