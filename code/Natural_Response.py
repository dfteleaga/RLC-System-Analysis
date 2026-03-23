import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def rlc(t, x, R, L, C):
    x1 = x[0]
    x2 = x[1]
        
    dx1 = x2
    dx2 = -(R/L)*x2 - (1/(L*C))*x1  ## gets state space equations for RLC circuit
        
    return [dx1, dx2]

def simulate_rlc(R_values, L, C, t_span, initial_values):

    results = {}

    for R in R_values:
        sol = solve_ivp(rlc, (0,10), [1, 0] ,args = (R, L, C), t_eval=np.linspace(0, 10, 1000))
        results[R] = sol

    return results

def plot_results(results):
    plt.figure()

    for R in R_values:
        sol = results[R]
        plt.plot(sol.t, sol.y[0], label=f"R = {R}") ## plots the current over time for each value of R
    ax = plt.gca()

    plt.xlabel('Time (s)')
    plt.ylabel('Current (A)')

    ## shift the x and y axes to the zero point so it lines up with the graph
    ax.spines['left'].set_position('zero') 
    ax.spines['bottom'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plt.legend()
    plt.savefig('natural_response.png')
    plt.show()

if __name__ == "__main__":
    R_values = [0.5, 2, 5]
    L = 1
    C = 1

    t_span = (0, 10)
    initial_values = [1, 0]

    results = simulate_rlc(R_values, L, C, t_span, [1,0])
    plot_results(results)