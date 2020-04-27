'''Before saving your visualization, you might want to also set the size that the figure will have on the page. To do so, you can use the Figure object's set_size_inches method. This method takes a sequence of two values. The first sets the width and the second sets the height of the figure.

Here, you will again have a Figure object called fig already provided (you can run plt.show if you want to see its contents). Use the Figure methods set_size_inches and savefig to change its size and save two different versions of this figure.'''

# Set figure dimensions and save as a PNG
fig.set_size_inches([3, 5])
fig.savefig('figure_3_5.png')

# Set figure dimensions and save as a PNG
fig.set_size_inches([5, 3])
fig.savefig('figure_5_3.png')