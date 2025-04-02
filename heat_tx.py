import matplotlib.pyplot as plt

k_values = [0.75, 1, 1.25]

x_values = [215, 210, 25, 0, 5, 10, 15, 20, 25, 30, 38]

for k in k_values:
    y_values = [-(20/0.3)*k*(x-25) for x in x_values]
    plt.plot(x_values, y_values, label=f"k={k}")

# Giving titles and axis label
plt.title("Heat Loss Through a Concrete Wall", fontsize=24)
plt.xlabel("Outside Wall Temperature (T2)", fontsize=20)
plt.ylabel("Heat Loss, Q (W)", fontsize=20)
plt.legend()
plt.grid(True)

plt.show()
