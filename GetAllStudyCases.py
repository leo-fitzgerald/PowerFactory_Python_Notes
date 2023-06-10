import powerfactory as pf
app = pf.GetApplication()

# Get active study case
active_case = app.GetActiveStudyCase()
app.PrintPlain(active_case)
# returns: <class 'powerfactory.DataObject'>

# get study case folder
study_case_folder = app.GetProjectFolder('study')

# get list of all study cases
study_cases = study_case_folder.GetContents()
# returns list: <class 'powerfactory.DataObject'>

# print all study cases
for case in study_cases:
    app.PrintPlain(case)