import powerfactory as pf
app = pf.GetApplication()

# Get active study case
active_case = app.GetActiveStudyCase()
app.PrintPlain(active_case)
# returns: <class 'powerfactory.DataObject'>

# run power flow 
app.GetFromStudyCase('ComLdf').Execute()

# get list of all lines
lines = app.GetCalcRelevantObjects('*.ElmLne')


# print all line loading
for line in lines:
    app.PrintPlain("{} | {} % ".format(line.loc_name, line.GetAttribute('c:loading')))


# ------------- Results ------------- #
# Line 4-5 | 14.153885616890863 %% 
# Line 4-6 | 8.60918683909552 %% 
# Line 5-7 | 21.449562270775953 %% 
# Line 6-9 | 15.427162750035569 %% 
# Line 7-8 | 18.94140153743569 %% 
# Line 8-9 | 8.455192584470337 %% 