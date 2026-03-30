import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def rlc(t, x, R_value, L, C):
    x1 = x[0]
    x2 = x[1]
        
    dx1 = x2
    dx2 = -(R_value/L)*x2 - (1/(L*C))*x1  ## gets state space equations for RLC circuit
        
    return [dx1, dx2]

def simulate_rlc(R, L, C, t_span, initial_values):

    results = {}

    for R_value in R:
        results[R_value] = solve_ivp(rlc, (0,10), [1, 0] ,args = (R_value, L, C), t_eval=np.linspace(0, 10, 1000))
        
    return results

def plot_results(results):
    plt.figure()

    for R_value, sol in results.items():
        plt.plot(sol.t, sol.y[0], label=f"R_value = {R_value}") ## plots the current over time for each value of R_value
    ax = plt.gca()

    plt.xlabel('Time (s)')
    plt.ylabel('Current (A)')

    ## shift the x and y axes to the zero point so it lines up with the graph
    ax.spines['left'].set_position('zero') 
    ax.spines['bottom'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plt.legend()
    plt.savefig('plots/Natural Response.png')
    plt.show()
