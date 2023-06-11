# Get minimum electrical distance from one bus to another using IEEE 9 Bus model

import powerfactory as pf
app = pf.GetApplication()

# get all buses
buses = app.GetCalcRelevantObjects('*.ElmTerm')

# bus to get min distance to
bus_9 = app.GetCalcRelevantObjects('Bus 9.ElmTerm')


# get min distance from all buses to bus 9
for bus in buses:
    app.PrintPlain("Min distance {} to {} | {} km".format(bus, bus_9[0], bus.GetMinDistance(bus_9[0])))
