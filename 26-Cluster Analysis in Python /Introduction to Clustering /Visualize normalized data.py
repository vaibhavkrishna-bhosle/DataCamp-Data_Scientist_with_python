'''After normalizing your data, you can compare the scaled data to the original data to see the difference. The variables from the last exercise, goals_for and scaled_data are already available to you.'''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

scaled_data = np.array()[3.07692308, 2.30769231, 1.53846154, 2.30769231, 0.76923077,
       0.76923077, 1.53846154, 0.00000000, 0.76923077, 3.07692308]
goals_for = [4,3,2,3,1,1,2,0,1,4]

# Plot original data
plt.plot(goals_for, label='original')

# Plot scaled data
plt.plot(scaled_data, label='scaled')

# Show the legend in the plot
plt.legend()

# Display the plot
plt.show()