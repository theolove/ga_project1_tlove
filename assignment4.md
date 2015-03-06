#1. Julie - Alcohol and Cancer
Great job, lots of information and analysis. 

**Data**

Looking at the source for the alcohol data, it appears that the methodology of collecting consumption data relies on sales and tax records. How would this change analysis? I know we discussed how New Hampshire is somewhere that people from other states go to buy alcohol. I think the same is true for DC, since it has lots of commuters who live in Virginia or Maryland.

You should keep as much data as possible, no reason to leave out the over 21 data when making your cleaned up dataset.

**Correlation Matrices**

Very attractive graphs and well designed. Interesting to see such weak correlations for everything else, and then a large one for wine.

**Liver Cancer vs. Ethenol per Capita**

It is a little confusing to look at this by state, and it gives a very small sample size for each of the trend lines. Did you try to analyze all the state data together? I am trying to figure out exactly what this shows, perhaps using a % of total consumption for each source instead of a gross value would make things more easily comparable. That being said, it is very interesting that you found so many clearly different trends in consumption vs. liver cancer based on source of ethanol. This might warrant futher analysis on to the differences between consumption patterns for various ethanol sources.

**Alcohol Consumption by Year by State**

A nice picture of general consumption trends by state.

I think your confusion is probably something that stems from looking at such aggregate data. The clue might be in more granular consumption data, since (as pointed out later in your work) you might have a few people drinking a lot leading to higher cancer rates, and they might prefer liquor, while the beer drinker in general doesn't get to consumption rates that cause spikes in liver cancer rates.

**Cancer Trends by State**

Nice clear treatment of trends by State, 

**Beer Regressions**

Good to see some attempts that didn't pan out. I think the main conclusion is that beer and state by themselves can't completely explain cancer rates that well, especially when you are trying to run regressions with a sample size of 12.

**Top Wine Consumption States**

Nice charts, but, as I mentioned in the "Data" section, I think there may be some external issues with sales data per capita for NH and DC that make it tough to draw any causal relationship.

**Overall**

Very in depth analysis with a lot of thoughtful avenues explored. I think there are some valid conclusions to be drawn and some clear relationsbhips established, but additional features and/or a more granular look would help get closer to the initial goal of the work.


#2. EK - BeerAdvocate Data

**Data Source**

It looks like you did a lot of work that was left out! I would have liked to see is more of an explanation of the initial data collection process and the munging that went in to the project. It sounded like, from the presentation and internal comment, tha the web-scraping dead-end sounded really interesting (let's see some code!). The source you gave for the current data says its not available. Where did you end up getting it, and how did you have to massage it? Were there any missing data you had to deal with? I would also have liked to see more explanations for the analysis. For instance, why did you only analyze the "top 5" beer? 

**Top 5 Beers**

Why only top 5 beers? Seems like it would be more interesting to look at top 5% or 10%. That being said, nice visualizations.

**Correlation**

A good illustration of expanding on a previous observation. Small typo in the title, and would have liked to have it specifically stated that this was a correlation matrrix for the entire dataset, and not the top5.

**ABV Analysis**

Interesting hypothesis to test. While there was no immediatley obvious correlation from the graph, perhaps we would find one in a linear regression? A few small typos in the descriptions. 

**Beer Style Analysis**

Good to see a look at some other categorical data, and one that is very important in the beer world. Definitely interesting to see the slant towards IPAs. Worth digging further.

**Overall**

This is a really interesting dataset and there are a lot of different ways to analyze it. The visualization aspect of the project was nice and covered a broad spectrum of techniques. It was good to see an attempt that was more of a dead end, which is something that many people tend to leave out of a project. Just more info on all the work you did to collect the data!

#3. Qasim - 311 Data

**Initial Data Observations**

Glad to see you focus in immediately on calls by agency as an important factor in the analysis and then being able to really isolate the agencies with the most information. This is such a large data set that focusing on differences between major categories of data really helps with the understanding.

**Calls Over Time**

Glad to see some time-series analysis, and cool to find the very blatant cyclicle behaviour holds across all agencies. Also a good technique to start annual and drill down, and it you seem to have covered most of the relevant time series. Nice explanations of the differences between agencies on the annual and monthly and daily level. Good work on explaining the anomalies in the days of the month and hourly data. 

**Calls by Borough**

Nice graphs to illustrate the differences between the boroughs. Could be worth some more analysis.

**LatLon Scatter Plots**

Really cool looking graphs and very nice way to visually show "hot zones". It would have been nice to make a more generic function for the lat and lon plots, and perhaps overlay them someway.

**Overall**

Very comprehensive time series analysis and good job looking at data by important categories. Overall your descriptions were good, although you could have standardized your code a little more. I am very interested to see what you look at next.
