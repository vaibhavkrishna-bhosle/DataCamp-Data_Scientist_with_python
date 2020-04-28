'''Seaborn supports setting different styles that can control the aesthetics of the final plot. In this exercise, you will plot the same data in two different styles in order to see how the styles change the output.'''

# Plot with a dark style
sns.set_style('dark')
sns.distplot(df['fmr_2'])
plt.show()

# Clear the figure
plt.clf()

