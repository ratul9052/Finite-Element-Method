# 1D Poisson Equation Solver using Finite Element Method (FEM)

This repository contains a Python implementation of the **Finite Element Method (FEM)** to solve the 1D Poisson equation:

$$
 \frac{d^2 u}{dx^2} = -f(x), \quad 0 \leq x \leq L
$$

with **Dirichlet boundary conditions**:

$$
u(0) = 0, \quad u(L) = 0
$$

In this problem, $f(x) = -1$, and the **analytical solution** is:

$$
u(x) = x(1 - x)/2
$$

## Problem Setup

### Strong Form

The strong form of the equation is:

$$
 \frac{d^2 u}{dx^2} = -1
$$

with the boundary conditions $u(0) = 0$ and $u(L) = 0$.

### Weak Formulation

To solve this equation using FEM, the weak form is derived. First, multiply the differential equation by a test function $v(x)$ and integrate over the domain:

$$
\int_0^L \left( - \frac{d^2 u}{dx^2} \right) v(x) \, dx = \int_0^L f(x) v(x) \, dx
$$

Using integration by parts, this simplifies to:

$$
\int_0^L \frac{du}{dx} \frac{dv}{dx} \, dx = \int_0^L f(x) v(x) \, dx
$$

where the boundary terms vanish due to the Dirichlet boundary conditions $u(0) = u(L) = 0$.

### Discretization and Shape Functions

The domain $[0, L]$ is discretized into $N$ elements with $N+1$ nodes. The solution $u(x)$ is approximated by a sum of linear shape functions $\phi_i(x)$ as follows:

$$
u(x) \approx \sum_{i=0}^{N} u_i \phi_i(x)
$$

The shape functions $\phi_i(x)$ are piecewise linear and locally supported, meaning each shape function is non-zero only over two adjacent elements.

### Deriving the Element Stiffness Matrix

For each element $e$, the local stiffness matrix is computed by evaluating the integral:

$$
K_{e,ij} = \int_{x_e}^{x_{e+1}} \frac{d\phi_i}{dx} \frac{d\phi_j}{dx} \, dx
$$

For linear elements, the gradients of the shape functions are constant over each element:

$$
\frac{d\phi_1}{dx} = -\frac{1}{h_e}, \quad \frac{d\phi_2}{dx} = \frac{1}{h_e}
$$

where $h_e$ is the length of the element. Substituting into the above equation gives the local element stiffness matrix:

$$
K_e = \frac{1}{h_e} \begin{bmatrix} 1 & -1 \\\ -1 & 1 \end{bmatrix}
$$

### Element Load Vector

The local load vector is computed by evaluating the integral:

$$
F_e = \int_{x_e}^{x_{e+1}} f(x) \phi(x) \, dx
$$

For the source term $f(x) = 1$, the local load vector becomes:

$$
F_e = \frac{h_e}{2} \begin{bmatrix} 1 \\\ 1 \end{bmatrix}
$$

### Global System Assembly

The global stiffness matrix $K$ and load vector $F$ are assembled by summing the contributions from all elements. The global system can be written as:

$$
K u = F
$$

where $u$ is the vector of nodal values $u_i$.

### Applying Boundary Conditions

The Dirichlet boundary conditions $u(0) = 0$ and $u(L) = 0$ are enforced by modifying the global stiffness matrix and load vector, setting the first and last rows to reflect the boundary conditions.

### Solving the System

Once the system is assembled and boundary conditions are applied, the linear system $K u = F$ is solved to obtain the nodal values $u_i$.

### Comparing with the Analytical Solution

The analytical solution to the 1D Poisson equation is:

$$
u(x) = x(1 - x)/2
$$

The FEM solution is compared with this analytical solution to verify its accuracy.

