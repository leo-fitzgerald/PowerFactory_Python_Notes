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

# ------------- Results ------------- #
# Min distance    Bus 1 to    Bus 9 | 2.0 km
# Min distance    Bus 2 to    Bus 9 | 2.0 km
# Min distance    Bus 8 to    Bus 9 | 1.0 km
# Min distance    Bus 9 to    Bus 9 | 0.0 km
# Min distance    Bus 3 to    Bus 9 | 0.0 km
# Min distance    Bus 6 to    Bus 9 | 1.0 km
# Min distance    Bus 4 to    Bus 9 | 2.0 km
# Min distance    Bus 5 to    Bus 9 | 3.0 km
# Min distance    Bus 7 to    Bus 9 | 2.0 km
