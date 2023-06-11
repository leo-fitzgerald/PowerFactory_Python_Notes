import powerfactory as pf
app = pf.GetApplication()

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

# ------------- Results ------------- #
#    Bus 1 | [<powerfactory.DataObject Nine-bus System\G1.ElmSym>, <powerfactory.DataObject Nine-bus System\T1.ElmTr2>]
#    Bus 2 | [<powerfactory.DataObject Nine-bus System\G2.ElmSym>, <powerfactory.DataObject Nine-bus System\T2.ElmTr2>]
#    Bus 3 | [<powerfactory.DataObject Nine-bus System\G3.ElmSym>, <powerfactory.DataObject Nine-bus System\T3.ElmTr2>]
#    Bus 4 | [<powerfactory.DataObject Nine-bus System\T1.ElmTr2>, <powerfactory.DataObject Nine-bus System\Line 4-5.ElmLne>, <powerfactory.DataObject Nine-bus System\Line 4-6.ElmLne>]
#    Bus 5 | [<powerfactory.DataObject Nine-bus System\Line 4-5.ElmLne>, <powerfactory.DataObject Nine-bus System\Load A.ElmLod>, <powerfactory.DataObject Nine-bus System\Line 5-7.ElmLne>]
#    Bus 6 | [<powerfactory.DataObject Nine-bus System\Load B.ElmLod>, <powerfactory.DataObject Nine-bus System\Line 6-9.ElmLne>, <powerfactory.DataObject Nine-bus System\Line 4-6.ElmLne>]
#    Bus 7 | [<powerfactory.DataObject Nine-bus System\Line 5-7.ElmLne>, <powerfactory.DataObject Nine-bus System\T2.ElmTr2>, <powerfactory.DataObject Nine-bus System\Line 7-8.ElmLne>]
#    Bus 8 | [<powerfactory.DataObject Nine-bus System\Line 7-8.ElmLne>, <powerfactory.DataObject Nine-bus System\Load C.ElmLod>, <powerfactory.DataObject Nine-bus System\Line 8-9.ElmLne>]
#    Bus 9 | [<powerfactory.DataObject Nine-bus System\Line 8-9.ElmLne>, <powerfactory.DataObject Nine-bus System\T3.ElmTr2>, <powerfactory.DataObject Nine-bus System\Line 6-9.ElmLne>]

# ------------- Results ------------- #
# Bus 1 | G1
# Bus 1 | T1

# Bus 2 | G2
# Bus 2 | T2

# Bus 3 | G3
# Bus 3 | T3

# Bus 4 | T1
# Bus 4 | Line 4-5
# Bus 4 | Line 4-6

# Bus 5 | Line 4-5
# Bus 5 | Load A
# Bus 5 | Line 5-7

# Bus 6 | Load B
# Bus 6 | Line 6-9
# Bus 6 | Line 4-6

# Bus 7 | Line 5-7
# Bus 7 | T2
# Bus 7 | Line 7-8

# Bus 8 | Line 7-8
# Bus 8 | Load C
# Bus 8 | Line 8-9

# Bus 9 | Line 8-9
# Bus 9 | T3
# Bus 9 | Line 6-9