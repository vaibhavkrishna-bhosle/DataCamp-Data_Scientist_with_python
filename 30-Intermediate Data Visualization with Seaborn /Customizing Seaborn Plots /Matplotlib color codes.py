'''Seaborn offers several options for modifying the colors of your visualizations. The simplest approach is to explicitly state the color of the plot. A quick way to change colors is to use the standard matplotlib color codes.'''

# Set style, enable color code, and create a magenta distplot
sns.set(color_codes=True)
sns.distplot(df['fmr_3'], color='m')

# Show the plot
plt.show()

