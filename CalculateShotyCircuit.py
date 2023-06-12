# run IEC & Complete Method 3-phase short circuit at all buses using IEEE 9 Bus model 
# return fault current and short circuit r1, x1 values for each bus

def bus_results():
    buses = app.GetCalcRelevantObjects('*.ElmTerm')
    for bus in buses:
        # round values for readability
        name, vnom, ikss, r, x = bus.GetAttribute('loc_name'), round(bus.GetAttribute('uknom'),3), round(bus.GetAttribute('m:Ikss'),3), round(bus.GetAttribute('m:rSbase'),3), round(bus.GetAttribute('m:xSbase'),3)       
        app.PrintPlain("{} | {} kV | {} kA | r1:{} pu | x1:{} pu ".format(name, vnom, ikss, r, x))

def shortcircuit(sc_type):
    sc = app.GetFromStudyCase('ComShc')
    if sc_type == "IEC":
        sc.iopt_mde = 1        # IEC
        sc.iopt_sch = "3psc"   # 3 phase short circuit
        sc.iopt_curr = 0       # maximum fault level
        sc.iopt_allbus = 2     # all buses
        
        # execute short circuit, get list of all buses
        sc.Execute()
        # app.PrintPlain(" ---------------- IEC 60909 ----------------")
        bus_results

    elif sc_type == "Complete":
        sc.iopt_mde = 3        # complete
        sc.iopt_sch = "3psc"   # 3 phase short circuit
        sc.iopt_curr = 0       # maximum fault level 
        sc.iopt_allbus = 2     # all buses

        # execute short circuit, get list of all buses
        sc.Execute()
        bus_results()

        
import powerfactory as pf

app = pf.GetApplication()
shortcircuit("IEC")
app.PrintPlain("\n")
shortcircuit("Complete")


# ------------- Results ------------- #
# Bus 1 | 16.5 kV | Type:IEC | 57.012 kA | r1:0.004 pu | x1:0.067 pu 
# Bus 2 | 18.0 kV | Type:IEC | 47.749 kA | r1:0.003 pu | x1:0.074 pu 
# Bus 3 | 13.8 kV | Type:IEC | 48.364 kA | r1:0.006 pu | x1:0.095 pu 
# Bus 4 | 230.0 kV | Type:IEC | 3.053 kA | r1:0.006 pu | x1:0.09 pu 
# Bus 5 | 230.0 kV | Type:IEC | 2.256 kA | r1:0.011 pu | x1:0.122 pu 
# Bus 6 | 230.0 kV | Type:IEC | 2.146 kA | r1:0.015 pu | x1:0.128 pu 
# Bus 7 | 230.0 kV | Type:IEC | 3.081 kA | r1:0.005 pu | x1:0.09 pu 
# Bus 8 | 230.0 kV | Type:IEC | 2.455 kA | r1:0.008 pu | x1:0.112 pu 
# Bus 9 | 230.0 kV | Type:IEC | 2.771 kA | r1:0.007 pu | x1:0.099 pu 

# ------------- Results ------------- #
# Bus 1 | 16.5 kV | Type:IEC | 57.012 kA | r1:0.004 pu | x1:0.067 pu 
# Bus 2 | 18.0 kV | Type:IEC | 47.749 kA | r1:0.003 pu | x1:0.074 pu 
# Bus 3 | 13.8 kV | Type:IEC | 48.364 kA | r1:0.006 pu | x1:0.095 pu 
# Bus 4 | 230.0 kV | Type:IEC | 3.053 kA | r1:0.006 pu | x1:0.09 pu 
# Bus 5 | 230.0 kV | Type:IEC | 2.256 kA | r1:0.011 pu | x1:0.122 pu 
# Bus 6 | 230.0 kV | Type:IEC | 2.146 kA | r1:0.015 pu | x1:0.128 pu 
# Bus 7 | 230.0 kV | Type:IEC | 3.081 kA | r1:0.005 pu | x1:0.09 pu 
# Bus 8 | 230.0 kV | Type:IEC | 2.455 kA | r1:0.008 pu | x1:0.112 pu 
# Bus 9 | 230.0 kV | Type:IEC | 2.771 kA | r1:0.007 pu | x1:0.099 pu 

