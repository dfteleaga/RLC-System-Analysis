# RLC Modelling Foundations

## 1. Objective

Understand how a series RLC circuit forms a second-order differential equation system.

## 2. Interpretation of Components

### 2.1. Resistors (R):

The resistor will dissipate electrical energy as heat whilst also acting as a damper for the system. 

The main equation we will use for the resistor component of the RLC circuit is:

$V_R= IR$

Resistors will dissipate energy and decrease the amplitude of oscillations.

### 2.2. Inductors (L)

The inductor will store energy in a magnetic field and oppose the changes in current due to Lenz's Law.

The main equations we will use regarding the inductor will be its voltage-current relationship:

$V_L = L\frac{dI}{dt}$

and the energy formula:

$E_L = \frac{1}{2}LI^2$

### 2.3 Capacitors (C)

The capacitor will store energy between two plates in an electric field. The voltage across the capacitor will depend on its stored charge.

The main equations we will use regarding the capacitor will be its current-voltage relationship:

$I = C\frac{dV_C}{dt}$

which is also written as:

$V_C = \frac{1}{C}\int Idt$

and the energy formula:

$E_C = \frac{1}{2}CV_C^2$

## 3. Analogy to Mass-Spring-Damper System

The RLC system is mathematically analogous to a mechanical oscillator system:

$F(t) = m\frac{d^2x}{dt^2} + c\frac{dx}{dt} + kx$

Mapping this onto the our circuit:

|Mechanical         |Electrical     |
|-------------------|---------------|
|Mass ($m$)           |Inductor ($L$)   |
|Damping ($c$)        |Resistor ($R$)   |
|Spring Constant ($k$)|Elastance ($1/C$)| 
|Force ($F(t)$)       |Voltage ($V$)

## 4. Derivation using Kirchhoff's Voltage Law

We know that Kirchhoff's Voltage Law (KVL) is:

$\sum \varepsilon = \sum V_{drops}$

So we have:

$V(t) = V_R + V_L + V_C$

Substitute each component's equations:

$V(t) = RI + L\frac{dI}{dt} + \frac{1}{C}\int Idt$

Differentiate both sides to remove the integral and rearranging:

$\frac{dV(t)}{dt} = L\frac{d^2I}{dt^2} + R\frac{dI}{dt} + \frac{I}{C}$

Divide through by L:

$\frac{1}{L}\frac{dV(t)}{dt} = \frac{d^2I}{dt^2} + \frac{R}{L}\frac{dI}{dt} + \frac{I}{LC}$

Which is comparable to the standard second-order form.

## 5. Natural Frequency and Damping

$\omega_0 = \frac{1}{\sqrt{LC}} = 2\pi f_0$

Or:

$f_0 = \frac{1}{2\pi\sqrt{LC}}$

This natural frequency determines how fast the system oscillates.

Damping Ratio:

$\zeta = \frac{R}{2}\sqrt{\frac{C}{L}}$

Controlls how the system oscillates.

Cases:

$\zeta < 1$ -> Underdamped

$\zeta = 1$ -> Critically Damped

$\zeta > 1$ -> Overdamped

### Why does Oscillation Occur?

1. Initially, the capacitor charges and stores electric energy.
2. Capacitor discharges and current increases through the inductor, building magnetic energy.
3. Current is pushed back by inductor, charging the capacitor in the opposite direction
4. Energy keeps swapping repeatedly between L and C
5. If $R=0$, energy is ideally conserved and oscillation continues forever as the system isn't being damped. If $R>0$, energy is lost over time and the amplitude of the oscillation decays.