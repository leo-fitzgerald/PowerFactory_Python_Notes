# Get next upstream higher voltage bus using IEEE 9 Bus model

import powerfactory as pf
app = pf.GetApplication()

# get all buses
buses = app.GetCalcRelevantObjects('*.ElmTerm')

# get min distance from all buses to bus 9
for bus in buses:
    app.PrintPlain("Next upstream HV Bus for {} is {}".format(bus, bus.GetNextHVBus()))


# ------------- Results -------------
# Next upstream HV Bus for    Bus 1 is Bus 4
# Next upstream HV Bus for    Bus 2 is Bus 7
# Next upstream HV Bus for    Bus 8 is None
# Next upstream HV Bus for    Bus 9 is None
# Next upstream HV Bus for    Bus 3 is Bus 9
# Next upstream HV Bus for    Bus 6 is None
# Next upstream HV Bus for    Bus 4 is None
# Next upstream HV Bus for    Bus 5 is None
# Next upstream HV Bus for    Bus 7 is None