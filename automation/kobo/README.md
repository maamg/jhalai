# KoBo XLSForm generator

`kobo.py` builds survey and choices worksheets for a beneficiary-identification form. The source contains form definitions, not collected respondent answers.

```sh
python -m pip install -r requirements.txt
python kobo.py
```

Run from this folder. Output: `RMTP_Questionnaire_XLSForm.xlsx`. The script overwrites that filename on each run. Validate the generated form in your intended KoBo environment before using it for data collection.

This is the canonical copy of two byte-identical scripts found in the original Python and SQL folders.
