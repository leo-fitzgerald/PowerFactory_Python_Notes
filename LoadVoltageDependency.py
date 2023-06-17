# Voltage Dependency of Load
# Ref: Voltage Stability of Electric Power Systems - Theirre Van Cutsem, Costas Vournas

import numpy as np

# P0 - Active Power at Rated voltage V0
# Q0 - Reactive power at Rated voltage V0
# V - Voltage

def ExponentialLoadConstZ(P0, Q0, V):   # power proportional to voltage squared
    alpha = 2.0                         # for constant impedance load
    beta = 2.0                          # for constant impedance load
    V0 = 1.0                            # rated per unit voltage

    P = P0 * (V/V0)**alpha
    Q = Q0 * (V/V0)**beta

    return P, Q

def ExponentialLoadConstI(P0, Q0, V):   # power proportional to voltage
    alpha = 1.0                         # for constant current load
    beta = 1.0                          # for constant current load
    V0 = 1.0                            # rated per unit voltage

    P = P0 * (V/V0)**alpha
    Q = Q0 * (V/V0)**beta

    return P, Q

def ExponentialLoadConstP(P0, Q0, V):   # power proportional to voltage
    alpha = 0.0                         # for constant power load
    beta = 0.0                          # for constant power load
    V0 = 1.0                            # rated per unit voltage

    P = P0 * (V/V0)**alpha
    Q = Q0 * (V/V0)**beta

    return P, Q

# A - % Constant Impedance
# B - % Constant Current
# C - % Constant Power

def PolynomialLoadModel(P0, Q0, V, A, B, C):
        if A + B + C != 1:
            print("Error: A + B + C must equal 1")
            return
        
        V0 = 1.0                            # rated per unit voltage
        a = 2.0                             # for constant impedance load
        b = 1.0                             # for constant current load
        c = 0.0                             # for constant power load

        P = P0 * (A*(V/V0)**a + B*(V/V0)**b + C*(V/V0)**c)
        Q = Q0 * (A*(V/V0)**a + B*(V/V0)**b + C*(V/V0)**c)

        return P, Q


print(ExponentialLoadConstZ(1, 1, 0.9))

print(PolynomialLoadModel(1, 1, 0.9, 0.25, 0.25, 0.5))