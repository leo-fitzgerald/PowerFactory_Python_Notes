# Get Study Cases - using IEEE 9 Bus model 

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

# ------------- Results ------------- #
#    01- Load Flow
#    02- Five Cycles Classical SG Model
#    03- Three Cycles Standard SG Model
#    04- Three Cycles IEEE Type 1 Amplidyne
#    05- Three Cycles IEEE Type 1 Mag-A
#    06- Three Cycles IEEE Type 3 SCPT
#    07- Comparison Excitation Models
#    08- Three Cycles IEEE Type 1 Mag-A_PSS