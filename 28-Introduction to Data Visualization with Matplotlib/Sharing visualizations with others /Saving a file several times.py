'''If you want to share your visualizations with others, you will need to save them into files. Matplotlib provides as way to do that, through the savefig method of the Figure object. In this exercise, you will save a figure several times. Each time setting the parameters to something slightly different. We have provided and already created Figure object.'''

plt.show()


# Save as a PNG file
fig.savefig('my_figure.png')

# Save as a PNG file with 300 dpi
fig.savefig('my_figure_300dpi.png', dpi=300)
