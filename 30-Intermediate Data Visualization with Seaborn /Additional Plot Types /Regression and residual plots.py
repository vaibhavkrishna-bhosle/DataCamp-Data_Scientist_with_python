'''Linear regression is a useful tool for understanding the relationship between numerical variables. Seaborn has simple but powerful tools for examining these relationships.

For these exercises, we will look at some details from the US Department of Education on 4 year college tuition information and see if there are any interesting insights into which variables might help predict tuition costs.

For these exercises, all data is loaded in the df variable.'''

# Display a regression plot for Tuition
sns.regplot(data=df,
            y='Tuition',
            x="SAT_AVG_ALL",
            marker='^',
            color='g')

plt.show()
plt.clf()

# Display the residual plot
sns.residplot(data=df,
              y='Tuition',
              x="SAT_AVG_ALL",
              color='g')

plt.show()
plt.clf()