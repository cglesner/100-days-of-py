"""Generate example matplotlib plots of polynomials created using the
func.Polynomial class."""

import matplotlib.pyplot as plt
from func import Poly

# Define an example polynomial and it's derivatives.
f_x = Poly([(3, 1), (2, -2), (1, 1)])

# Define a set of x-values for the plot.
num_points = 100
x_min = -2
x_max = 2
x_values = [x_min + i*(x_max - x_min)/num_points for i in range(num_points)]
y_values = [f_x(x) for x in x_values]

plt.plot(x_values, y_values)

input("Enter to quit.")