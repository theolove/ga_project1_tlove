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

# 4. aggregate sum of spend by day
daily_sum = ads.groupby(ads["day"]).sum()
daily_sum["ads"] = ads.groupby(ads["day"]).count()["ad_id"]

# 5.

