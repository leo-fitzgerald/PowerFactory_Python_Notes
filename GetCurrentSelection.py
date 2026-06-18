import powerfactory as pf
app = pf.GetApplication()

# Get the current selection
obj = app.GetCurrentSelection()

if not obj:
    app.PrintPlain("No object selected.")
else:
    app.PrintPlain(obj[0].loc_name)    # return selected object name
    app.PrintPlain(obj[0].uknom)       # return selected object nominal voltage
