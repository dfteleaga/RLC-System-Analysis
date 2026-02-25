# State Space Conversion Notes

## 1. Objective

Go over state space conversion basics and explain how second-order differential equations can be rewritten as a system of first-order differential equations, and applying it to the RLC circuit

## 2. State Variables in Differential Equations

We use state-space form as computers can solve first-order differential equations more easily and also because this is the standard format for control systems.

A state is known as the minimum set of variables required to determine a system's condition at any given moment, allowing its future behaviour to also be determined given the system equations.

Given a simple system where a ball is moving in a straight line, if we were given just the position of the ball, we could not predict where it would be in 2 seconds because we wouldn't know which way or how fast it would be moving. This means that just position is **not enough**.

If we were given both the current **position** and the **velocity** of the ball (and the forces acting on the ball were known), it would be enough to determine the system's future behaviour.

**A differential equation of the nth order requires n initial conditions, and we therefore need n independent state variables.**

## 3. Converting to State-Space Form

### 3.1 Considering a General Second-Order Equation

$\ddot{x} + a\dot{x} +bx = 0$

This equation is second-order. Most numerical solvers handle first-order differential equations a lot more easily, so we use state-space conversion to convert the above second-order differential into two first-order differential equations.

Let us define some variables:

$x_1 = x$

$x_2 = \dot{x}$

$x$ and $\dot{x}$ are chosen as these are sufficient to calculate $\ddot{x}$, and therefore determine the system's condition at any given time.

We can then see that:

$\dot{x_1} = x_2$

and by substituting back into the second-order equation:

$\dot{x_2} = -ax_2 - bx_1$

**The second-order differential equation has now been rewritten as a system of two first-order differential equations.**

## 4. Applying State-Space Conversion to the RLC Circuit

Taking a homogeneous RLC second-order equation:

$L\ddot{I} + R\dot{I} + \frac{1}{C}I = 0$

and dividing throughout by L:

$\ddot{I} + \frac{R}{L}\dot{I} + \frac{1}{LC}I = 0$

The two minimum variables we need to determine a system's condition at any moment are the current, $I$, and the rate of change of current, $\dot{I}$.

$I = x_1$

$\dot{I} = x_2$

In state-space form:

$\dot{x_1} = x_2$

$\dot{x_2} = -\frac{R}{L}x_2 - \frac{1}{LC}x_1$