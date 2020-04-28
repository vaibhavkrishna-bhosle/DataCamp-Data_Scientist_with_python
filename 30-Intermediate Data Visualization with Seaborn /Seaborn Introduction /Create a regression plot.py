'''For this set of exercises, we will be looking at FiveThirtyEight's data on which US State has the worst drivers. The data set includes summary level information about fatal accidents as well as insurance premiums for each state as of 2010.

In this exercise, we will look at the difference between the regression plotting functions.'''

# Create a regression plot of premiums vs. insurance_losses
sns.regplot(data=df,
            x="insurance_losses",
            y="premiums")

# Display the plot
plt.show()


# Create an lmplot of premiums vs. insurance_losses
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums")

# Display the second plot
plt.show()