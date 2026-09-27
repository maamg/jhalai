# Known issues and validation

Python files were parsed without running them. Two existing syntax errors were found:

- `python/100-days/Fresh Hangman.py`, line 36: expected an indented block after 'for' statement on line 34.
- `python/code-in-place/rough.py`, line 1: invalid syntax.

Other limitations:

- The included graphics module does not supply the Canvas API used by two course scripts.
- Karel exercises require the course environment.
- R import practice uses local paths and unpublished datasets.
- BigQuery notes mix languages and contain an empty dataset identifier.
- Similar blackjack, auction, Hangman and GEE attempts are intentionally retained.
- Five course folders contain the same IDE starter `main.py`; these are retained in context.
- Some exercises may have runtime or logical errors. Syntax parsing does not establish correctness.
- No interactive exercises, GUI programs or network requests were executed as part of this import.
