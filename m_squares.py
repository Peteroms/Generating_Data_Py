import matplotlib.pyplot as plt
# pyplot contains a number of functions that help generate charts and plots

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=2) # linewidth Controls the thickness of the line generated

# set chart title and label axes
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.show()   # plt.show() functions opens matplotlib viewer and displays the plot



