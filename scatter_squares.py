import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=50)

# Set chart title and label axes
plt.title("Squares Numbers", fontsize=26)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square of Value", fontsize=24)

plt.show()


