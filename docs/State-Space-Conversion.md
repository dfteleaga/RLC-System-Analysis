# State Space Conversion Notes

## 1. Objective

Go over state space conversion basics and explain how second-order differential equations can be rewritten as a system of first-order differential equations, and applying it to the RLC circuit

## 2. State Variables in Differential Equations

A state is known as the minimum set of variables required to determine a system's condition at any given moment, allowing its future behaviour to also be determined given the system equations.

Given a simple system where a ball is moving in a straight line, if we were given just the position of the ball, we could not predict where it would be in 2 seconds because we wouldn't know which way or how fast it would be moving. This means that just position is **not enough**.

If we were given both the current **position** and the **velocity** of the ball (and the forces acting on the ball were known), it would be enough to determine the system's future behaviour.

**A differential equation of the nth order requires n initial conditions, and we therefore need n independent state variables.**