import powerfactory as pf
app = pf.GetApplication()

# Get the current selection
obj = app.GetCurrentSelection()

app.PrintPlain(obj[0].loc_name)    # return selected object name
app.PrintPlain(obj[0].uknom)       # return selected object nominal voltage 
