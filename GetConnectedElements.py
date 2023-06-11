import powerfactory as pf
app = pf.GetApplication()

# Get active study case
active_case = app.GetActiveStudyCase()

# Get all buses
buses = app.GetCalcRelevantObjects('*.ElmTerm')

# Get elements connected to each bus 

import powerfactory as pf
app = pf.GetApplication()

# Get active study case
active_case = app.GetActiveStudyCase()

# Get all buses
buses = app.GetCalcRelevantObjects('*.ElmTerm')

# get connected elements
for bus in buses:
    connected_elements = bus.GetConnectedElements()
    app.PrintPlain("{} | {}".format(bus, connected_elements))
    # returns: <class 'powerfactory.DataObject'>

app.PrintPlain("\n")

# get connected elements
for bus in buses:
    connected_elements = bus.GetConnectedElements()
    for element in connected_elements:
        app.PrintPlain("{} | {}".format(bus.loc_name, element.loc_name))
    app.PrintPlain("\n")
