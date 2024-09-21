# LF 
# Calculate Source Impedance from short circuit current 

import math

# ---------------------INPUT -------------------
Vline = 11      #  Three-phase line-line voltage
Isc3P = 21      #  Three-phase short circuit curent amp
Isc1P = 1.5     #  Single-phase short circuit curent amp
XR3P = 18       # Three-phase fault current XR ratio
XR1P = 40       # Single-phase fault current XR ratio

# ----------------------------------------------------------------
Sbase = 100 
Zbase = (Vline * Vline) / Sbase
Vphase = Vline/math.sqrt(3)
Ssc3P = Vline * Isc3P * math.sqrt(3)
Ssc1P = Vphase * Isc1P

Z1ohm = Vline / (Isc3P * math.sqrt(3))
Z1pu = Z1ohm / Zbase
R1ohm = Z1ohm * math.cos(math.atan(XR3P))
R1pu = R1ohm / Zbase
X1ohm = Z1ohm * math.sin(math.atan(XR3P))
X1pu = X1ohm / Zbase

Z0ohm = ((3*Vphase) / (Isc1P)) - 2*Z1ohm
R0ohm = Z0ohm * math.cos(math.atan(XR1P))
X0ohm= Z0ohm * math.sin(math.atan(XR1P))

Z0pu = Z0ohm / Zbase
R0pu = R0ohm / Zbase
X0pu = X0ohm / Zbase 

# ---------------------OUTPUT-------------------
print("---"*10)
print("Ikss 3P: {} kA".format(Isc3P))
print("Skss 3P: {0:.4g} MVA".format(Ssc3P))
print("Ikss 1P: {} kA".format(Isc1P))
print("Skss 1P: {0:.4g} MVA".format(Isc1P))
print("---"*10)
print("Z1: {0:.4g} ohm".format(Z1ohm))
print("R1: {0:.4g} ohm".format(R1ohm))
print("X1: {0:.4g} ohm".format(X1ohm))
print("---"*10)
print("Z1: {0:.4g} pu".format(Z1pu))
print("R1: {0:.4g} pu".format(R1pu))
print("X1: {0:.4g} pu".format(X1pu))
print("---"*10)
print("Z0: {0:.4g} ohm".format(Z0ohm))
print("R0: {0:.4g} ohm".format(R0ohm))
print("X0: {0:.4g} ohm".format(X0ohm))
print("---"*10)
print("Z0: {0:.4g} pu".format(Z0pu))
print("R0: {0:.4g} pu".format(R0pu))
print("X0: {0:.4g} pu".format(X0pu))
print("---"*10)
