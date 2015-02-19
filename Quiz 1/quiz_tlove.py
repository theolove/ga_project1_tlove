# Answers to Data Science Quiz

"""
1. pylab includes more libraries, including numpy
"""

"""
2. Read in the gooogle adwords
"""
import pandas as pd
import numpy as np

ads = pd.read_csv("ads.csv", skiprows=3, header=0, skipfooter=1)

# 3. subset where spend > 30
big_ads = ads[ads["spend"] > 30]

# 3b. subset where ad_id is 200 and spend > 30
big_ads2 = ads[(ads["ad_id"] == 200) & (ads["spend"] > 30)]

# 4. aggregate count of ads and sum of spend by day
ads_group = ads.groupby('date')

daily_sum = pd.DataFrame({'Count': ads_group.ad_id.count(),
                          'Spend_Total': ads_group.spend.sum()})

print daily_sum

"""
5.
import the matplotlib library as an object called plt
make the python division function automatically return a float

set the 'ctr' column of ads as clicks / impressions

create a figurespace
add a subplot to the figure space, the figurespace will has 1 column and 2 rows and this is the first subplot
make this first subplot a histogram of spend

add the next sublplot
this is a scatter of spend as x and ctr as y, with green dots as the format
show the figure with the two subplots
"""

"""
6. $0.02 (i.e. the y-intercept)
7. clicks has a pvalue > 0.10 and should be dropped
8. ad 1772 is $.50 cheaper than any other add with the same impressions 

9. A trellis plot, in general, is a grid of grpahs, where each feature of data set plotted against each other feature.
The diagonal of the plot is the would be the feature against itself, so usually, a histogram is used.
This can be implemented by Pandas in pandas.scatter_plot

10. reset_index() changes the index of a DataFrame to a new feature. This can be helpful if you want to make a timeseries column into an index.
"""



