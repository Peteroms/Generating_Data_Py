import matplotlib.pyplot as plt

from random_walk import Randomwalk

# Keep making the new walks, as long as the program is avtive.
while True:
    # Make random walk, and plot the points.
    rw = Randomwalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=10)

    # Emphasize the first and last points
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)
    
    plt.show()

    keep_running = input("Make another random walk? (y/n): ")
    if keep_running == 'n':
        break

