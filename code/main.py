import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

global R, L, C
R = 0.001
L = 1
C = 1

def rlc(t, x):
    x1 = x[0]
    x2 = x[1]
    
    dx1 = x2
    dx2 = -(R/L)*x2 - (1/(L*C))*x1
    
    return [dx1, dx2]
t_span = (0, 10)

sol = solve_ivp(rlc, t_span, [1, 0])

plt.plot(sol.t, sol.y[0])
plt.plot(sol.t, sol.y[1])
plt.show()