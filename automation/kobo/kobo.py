import pandas as pd

# --- Survey Sheet ---
survey = [
    {"type": "begin_group", "name": "beneficiary_identification", "label": "1. Beneficiary Identification"},
    {"type": "text", "name": "name", "label": "1.1 Full name of the fish grower/farmer"},
    {"type": "text", "name": "father_husband_name", "label": "1.2 Father/Husband’s Name"},
    {"type": "select_one gender", "name": "gender", "label": "1.3 Gender"},
    {"type": "select_one age_group", "name": "age", "label": "1.4 Age"},
    {"type": "text", "name": "mobile", "label": "1.5 Mobile"},
    {"type": "select_one occupation", "name": "occupation", "label": "1.6 Occupation"},
    {"type": "select_one literacy", "name": "literacy", "label": "1.7 Literacy"},
    {"type": "select_one pond_ownership", "name": "pond_ownership", "label": "1.8 Pond Ownership"},
    {"type": "end_group", "name": "", "label": ""}
]

# --- Choices Sheet ---
choices = [
    {"list_name": "gender", "name": "1", "label": "Male"},
    {"list_name": "gender", "name": "2", "label": "Female"},
    {"list_name": "gender", "name": "3", "label": "Transgender"},

    {"list_name": "age_group", "name": "1", "label": "15–25"},
    {"list_name": "age_group", "name": "2", "label": "26–35"},
    {"list_name": "age_group", "name": "3", "label": "36–45"},
    {"list_name": "age_group", "name": "4", "label": "46–55"},
    {"list_name": "age_group", "name": "5", "label": "55-above"},

    {"list_name": "occupation", "name": "1", "label": "Professional fish farmer"},
    {"list_name": "occupation", "name": "2", "label": "Subsistence/seasonal fish farmer"},
    {"list_name": "occupation", "name": "3", "label": "Others"},

    {"list_name": "literacy", "name": "1", "label": "Can sign only"},
    {"list_name": "literacy", "name": "2", "label": "Non institutional/self-educated"},
    {"list_name": "literacy", "name": "3", "label": "Primary"},
    {"list_name": "literacy", "name": "4", "label": "Secondary"},
    {"list_name": "literacy", "name": "5", "label": "University"},

    {"list_name": "pond_ownership", "name": "1", "label": "Own"},
    {"list_name": "pond_ownership", "name": "2", "label": "Leased"},
    {"list_name": "pond_ownership", "name": "3", "label": "Mortgage"},
    {"list_name": "pond_ownership", "name": "4", "label": "Family"},
    {"list_name": "pond_ownership", "name": "5", "label": "Joint farming"},
    {"list_name": "pond_ownership", "name": "6", "label": "Others"}
]

# Convert to DataFrames
survey_df = pd.DataFrame(survey)
choices_df = pd.DataFrame(choices)

# Save to Excel
with pd.ExcelWriter("RMTP_Questionnaire_XLSForm.xlsx", engine="xlsxwriter") as writer:
    survey_df.to_excel(writer, sheet_name="survey", index=False)
    choices_df.to_excel(writer, sheet_name="choices", index=False)
