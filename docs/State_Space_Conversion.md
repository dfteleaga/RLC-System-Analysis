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

In a **non-homogenous** case where an input voltage is present, we would have to use the complete state-space form. The form we have used until now, $\dot{x} = Ax$, does not take any input conditions into account. In reality, we know that there will be an input voltage which is why we have to use the form:

$\dot{x} = Ax + Bu$

where $u$ is the input. This doesn't change the equation much as the only thing we'd have to do is add the input voltage:

$\dot{x_2} = -\frac{R}{L}x_2 - \frac{1}{LC}x_1 + \frac{1}{L}V_{in}(t)$

## 5. Alternative State Choice

Instead of defining our states as $I$ and $\dot{I}$, another approach would be using the two variables which represent different energy stores $I$ and $V_C$. This approach takes energies into account and is an overall more physical state choice which also works better with forced damped cases.

The inductor stores magnetic energy: 

$E_L = \frac{1}{2}LI^2$

The capacitor stores electric energy:

$E_C = \frac{1}{2}CV_C^2$

Since it is known that the order of a system corresponds to the number of independent energy stores, a valid choice for our state variables is:

$x_1 = I$

$x_2 = V_C$

Starting from KVL:

$V_{in}(t) = RI + L\dot{I} + V_C$

Rearrange for $\dot{I}$:

$\dot{I} = \frac{1}{L}V_{in}(t) - \frac{R}{L}I - \frac{1}{L}V_C$

Using $I = C\dot{V_C}$ we get:

$\dot{V_C} = \frac{1}{C}I$

This results into another state-space formulation which is commonly used:

$\dot{x_1} = -\frac{R}{L}x_1 - \frac{1}{L}x_2 + \frac{1}{L}V_{in}(t)
$

$\dot{x_2} = \frac{1}{C}x_1$