# RLC Simulation Results

## Parameters

L = 1 Henry

C = 1 Farad

Initial Current = 1 Amp

Initial Rate of Change of Current = 0 Amp/s

## 1. Underdamped Case (R = 0.5Ω)

In this case, the resistance is relatively small. This means that only a small amount of energy will be dissipated as heat in the resistor during each oscillation, making the system show oscillatory behaviour.

Due to the resistance not being 0, some energy is still lost during each cycle which is why the amplitude of the wave is seen to be slowly decreasing. This produces the decaying oscillation seen in the plot.

## 2. Critically Damped Case (R = 2Ω)

Using $\zeta = \frac{R}{2}\sqrt{\frac{C}{L}}$ and setting $\zeta$ as $1$ (since we want to find the critical damping case) we find that the value of $R$ which causes critical damping is $2\Omega$

At critical damping resistance, the system returns to equilibrium without oscillating. Unlike in the underdamped case, the system doesn't overshoot or oscillate.

Critical damping represents the optimal balance between energy storage and dissipation.

## 3. Overamped Case (R = 5Ω)

In the overdamped case, the resistance is large and energy is dissipated as heat very quickly. This means that no oscillation occurs and the system reaches equilibrium without changing direction.

The system returns to equilibrium **more slowly** than in the critically damped case. This happens because excessive resistance dominates the motion, making the transfer of energy slower.

This simulation shows a slow, smooth decay towards zero.

## 4. Overall Interpretation

These results demonstrate how resistance controls the behaviour of an RLC circuit.

Increasing the resistance causes more energy to be dissipated as heat in the resistor, reducing oscillations in the system. 

The three distinct behaviours in each damping case match the theoretical predictions for second-order systems and confirm that this simulation accurately represents the physical behaviour of the circuit.