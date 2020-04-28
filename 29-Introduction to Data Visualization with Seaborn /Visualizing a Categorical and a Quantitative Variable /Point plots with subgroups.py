'''Let's continue exploring the dataset of students in secondary school. This time, we'll ask the question: is being in a romantic relationship associated with higher or lower school attendance? And does this association differ by which school the students attend? Let's find out using a point plot.

We've already imported Seaborn as sns and matplotlib.pyplot as plt.'''

# Create a point plot with subgroups
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school")

# Show plot
plt.show()

# Turn off the confidence intervals for this plot
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None)

# Show plot
plt.show()

# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None,
            estimator=median)

# Show plot
plt.show()