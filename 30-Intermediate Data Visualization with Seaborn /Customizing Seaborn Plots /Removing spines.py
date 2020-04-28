'''In general, visualizations should minimize extraneous markings so that the data speaks for itself. Seaborn allows you to remove the lines on the top, bottom, left and right axis, which are often called spines.'''


# Set the style to white
sns.set_style('white')

# Create a regression plot
sns.lmplot(data=df,
           x='pop2010',
           y='fmr_2')

# Remove the spines
sns.despine()

# Show the plot and clear the figure
plt.show()
plt.clf()