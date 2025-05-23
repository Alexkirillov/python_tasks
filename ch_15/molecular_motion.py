import matplotlib.pyplot as plt
from random_walk import RandomWalk
# keep making new walks as long as the program is active


while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    plt.style.use("classic")
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=1)
    ax.set_aspect("equal")

    #emphasize the first and the last points.
    ax.scatter(0,0, c= "green",edgecolors="none",s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none",s=100)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("make another walk? (y/n):")
    if keep_running == "n":
        break