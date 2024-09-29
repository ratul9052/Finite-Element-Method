import numpy as np
import matplotlib.pyplot as plt

# Generate the mesh
def generate_mesh(L, N):
    return np.linspace(0, L, N + 1)

# Element stiffness matrix (constant for uniform mesh)
def element_stiffness_matrix(h_e):
    return (1 / h_e) * np.array([[1, -1], [-1, 1]])

# Element load vector (constant for f(x) = 1)
def element_load_vector(h_e):
    return (h_e / 2) * np.array([1, 1])

# Assemble the global stiffness matrix and load vector
def assemble_global_system(N, x_nodes):
    K = np.zeros((N + 1, N + 1))
    F = np.zeros(N + 1)
    
    for e in range(N):
        h_e = x_nodes[e+1] - x_nodes[e]
        K_e = element_stiffness_matrix(h_e)
        F_e = element_load_vector(h_e)

        # Add to global matrix and vector
        K[e:e+2, e:e+2] += K_e
        F[e:e+2] += F_e

    return K, F

# Apply Dirichlet boundary conditions u(0) = u(L) = 0
def apply_boundary_conditions(K, F):
    K[0, :] = 0
    K[-1, :] = 0
    K[0, 0] = 1
    K[-1, -1] = 1
    F[0] = 0
    F[-1] = 0
    return K, F

# Solve the linear system
def solve_system(K, F):
    return np.linalg.solve(K, F)

# Plot the FEM and analytical solutions
def plot_solution(x_nodes, u_fem, u_analytical):
    plt.plot(x_nodes, u_fem, label='FEM Solution', marker='o')
    plt.plot(x_nodes, u_analytical, label='Analytical Solution', linestyle='--')
    plt.xlabel('x')
    plt.ylabel('u(x)')
    plt.legend()
    plt.title('FEM vs Analytical Solution')
    plt.show()

# Main function
L = 1
N = 50  # Try with a larger number of elements
x_nodes = generate_mesh(L, N)

# Analytical solution
u_analytical = 0.5*x_nodes * (1 - x_nodes)

# Assemble the system
K, F = assemble_global_system(N, x_nodes)

# Apply boundary conditions
K, F = apply_boundary_conditions(K, F)

# Solve the system
u_fem = solve_system(K, F)

# Plot and compare
plot_solution(x_nodes, u_fem, u_analytical)


