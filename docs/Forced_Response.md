# RLC Forced Response Analysis

## 1. Objective

After analysing the natural response of the RLC system, I wanted to study the behaviour of the circuit in a damped case which is when an external voltage source is applied.

## 2. Models Used

During this project we considered two different state-space options:

$x_1 = I$

$x_2 = \dot{I}$

This formulation is convenient for natural responses but when an external voltage is applied, this formulation becomes less intuitive as the input voltage is added to $\dot{I}$ rather than directly to the current.

The better representation for the forced behaviour would be:

$x_1 = I$

$x_2 = V_C$

This state choice corresponds directly to two energy storage elements in the circuit which makes it a more physically meaningful choice for states.

## 3. Input Applied

The constant voltage input applied to the circuit ($V_{in}(t) = 1$)
represents a step input applied at the start of the simulation. Numerically, the system was simulated using the same solver as in the natural response analysis.

## 4. Observed Behaviour

The forced response creates a temporary current as energy begins to flow through the circuit. Current first flows through the inductor and to the capacitor which begins to charge whilst energy is being dissipated through the resistor.

Depending on the resistance, the transient current may oscillate briefly before settling due to energy level exchanges between the capacitor and inductor. 

After some time, the capacitor becomes fully charged and the current in the circuit approaches zero.

## 5. Comparison with Natural Response

The natural response described the behaviour of the RLC circuit with no external voltage source.

In contrast, the forced response shows how the circuit behaves when there is already an external energy source applied.

Although the temporary behaviour still shows oscillations in the lightly damped cases, the long-term behaviour is mainly determined by the external input and the circuit configuration.

For a DC voltage, the capacitor will eventually charge completely which causes the current in the circuit to tend to zero.

## 6. Interpretation

The inductor resists sudden changes in current, while the capacitor stores the charge and gradually approaches the applied voltage. The resistor dissipates energy continuously as heat, reducing the amplitude of the oscillations.

This experiment demonstrates how the same RLC system can exhibit both natural and forced responses depending on whether an external voltage is applied or not.