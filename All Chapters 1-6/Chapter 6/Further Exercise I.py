## Exercise I: Stack bar graph
# In January 2007, a Gallup poll asked 1008 Americans aged 18 and over whether they planned to watch the upcoming Super Bowl. The pollster also asked who planned to watch whether they were looking forward more to watch football games or commercials. The results were summarized in the table
# ```
#                 Male	 Female	  Total
# Game		279	  200	    479
# Commercials	81	  156	    237
# won’t watch	132	  160	    292
# Total		492	  516	    1008
# ```

import matplotlib.pyplot as plt

# Data
categories = ['Male', 'Female']
game = [279, 200]
commercials = [81, 156]
wont_watch = [132, 160]

# Create a stacked bar graph
plt.bar(categories, game, label='Game', color='blue')
plt.bar(categories, commercials, bottom=game, label='Commercials', color='orange')
plt.bar(categories, wont_watch, bottom=[sum(x) for x in zip(game, commercials)], label="Won't Watch", color='gray')

# Add labels and title
plt.xlabel('Gender')
plt.ylabel('Number of Respondents')
plt.title('Super Bowl Viewing Plans by Gender')
plt.legend()

# Show the plot
plt.show()
