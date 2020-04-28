'''In this exercise, we'll explore data from students in secondary school. The "study_time" variable records each student's reported weekly study time as one of the following categories: "<2 hours", "2 to 5 hours", "5 to 10 hours", or ">10 hours". Do students who report higher amounts of studying tend to get better final grades? Let's compare the average final grade among students in each category using a bar plot.

Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt.'''

# Create bar plot of average final grade in each study category
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar")

# Show plot
plt.show()

# Rearrange the categories
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=["<2 hours",
                   "2 to 5 hours",
                   "5 to 10 hours",
                   ">10 hours"])

# Show plot
plt.show()


# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=["<2 hours",
                   "2 to 5 hours",
                   "5 to 10 hours",
                   ">10 hours"],
            ci=None)

# Show plot
plt.show()
