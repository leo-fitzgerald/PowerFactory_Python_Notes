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
