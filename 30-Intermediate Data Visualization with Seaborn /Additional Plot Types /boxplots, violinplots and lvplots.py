'''Seaborn's categorical plots also support several abstract representations of data. The API for each of these is the same so it is very convenient to try each plot and see if the data lends itself to one over the other.

In this exercise, we will use the color palette options presented in Chapter 2 to show how colors can easily be included in the plots.'''

# Create a boxplot
sns.boxplot(data=df,
            x='Award_Amount',
            y='Model Selected')

plt.show()
plt.clf()

# Create a violinplot with the husl palette
sns.violinplot(data=df,
               x='Award_Amount',
               y='Model Selected',
               palette='husl')

plt.show()
plt.clf()

# Create a lvplot with the Paired palette and the Region column as the hue
sns.lvplot(data=df,
           x='Award_Amount',
           y='Model Selected',
           palette='Paired',
           hue='Region')

plt.show()
plt.clf()

