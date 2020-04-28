'''Let's continue using the student_data dataset. In an earlier exercise, we explored the relationship between studying and final grade by using a bar plot to compare the average final grade ("G3") among students in different categories of "study_time".

In this exercise, we'll try using a box plot look at this relationship instead. As a reminder, to create a box plot you'll need to use the catplot() function and specify the name of the categorical variable to put on the x-axis (x=____), the name of the quantitative variable to summarize on the y-axis (y=____), the Pandas DataFrame to use (data=____), and the type of plot (kind="box").

We have already imported matplotlib.pyplot as plt and seaborn as sns.'''

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours",
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="box",
            order=study_time_order)

# Show plot
plt.show()

