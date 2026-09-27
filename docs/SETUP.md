# Running the exercises

Use Python 3 for Python exercises. Run each file from its containing folder, for example:

```sh
cd python/100-days
python "Band Name Generator.py"
```

Most exercises use the standard library and some prompt for input. Install `requests` for the Subin HTTP exercises. Those scripts perform network requests and may write downloaded files. Statistics and KoBo folders have separate dependency lists; versions are not pinned because a reproducible environment has not yet been established.

## Special environments

- Code in Place: `StepUp.py` requires the Stanford Karel environment. The bundled John Zelle `graphics.py` uses Tkinter and works with `GraphWin`; it does not provide Stanford's `Canvas` API. Canvas-based exercises need the matching course environment.
- Earth Engine: run JavaScript in the Earth Engine Code Editor, not Node.js.
- R: use R/RStudio, install the packages named in the source, and update local data paths.
- SQL: the supplied BigQuery file is a draft, not a runnable query.
- HTML: open locally in a browser; some resources require internet access.

Dependency installation, GUI execution, external services and course runtimes were not validated during organisation.
