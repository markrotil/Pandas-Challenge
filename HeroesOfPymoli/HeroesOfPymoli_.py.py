#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd
import os
import numpy as np

# File to Load (Remember to Change These)
filepath = os.path.join("Resources", "purchase_data.csv")

# Read Purchasing File and store into Pandas data frame
purchase_data_df = pd.read_csv(filepath)
purchase_data_df.tail()


# ## Player Count

# * Display the total number of players
# 

# In[2]:


#counts the unique gamertags under "SN"
player_count_df = purchase_data_df["SN"].nunique()

#Creates a dataframe that has the header "Total" displaying the information retrieved from my player count, then visualizes it
total_player_count_df = pd.DataFrame({"Total" : [player_count_df]})
total_player_count_df.head()


# Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[3]:


# makes a counter to count each unique item name
item_count_df = purchase_data_df["Item Name"].nunique()
#find the average price of all the items within the CVS 
average_price_df = round(purchase_data_df["Price"].mean(), 2)
#counts the number of purchases by counting the item ID
total_purchase_df = purchase_data_df["Item ID"].count()
#Takes all the Prices in the "Price" column and adds them up
total_revenue_df = purchase_data_df["Price"].sum()
#Creates a summary data frame that includes all the variables above
total_unique_items_df = pd.DataFrame({"Number of Unique Items": [item_count_df], 
                                      "Average Item Price" : f"${average_price_df}", 
                                      "Number of Purchases" : [total_purchase_df],
                                     "Total Revenue" : f"${total_revenue_df}"
                                     })
#prints out the Dat Frame
total_unique_items_df.head()


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[7]:


# Locates male, female and Other / None-Disclosed respectively 
male_df = purchase_data_df.loc[(purchase_data_df["Gender"] == "Male"), ["SN"] ]  
female_df = purchase_data_df.loc[purchase_data_df["Gender"] == "Female", ["SN"] ]                  
other_df = purchase_data_df.loc[purchase_data_df["Gender"] == "Other / Non-Disclosed", ["SN"] ]

# Counts the number of unique names using the "SN" column
male_count_df = len(male_df.SN.unique())
female_count_df = len(female_df.SN.unique())
other_count_df = len(other_df.SN.unique())

# Takes the Counts above divide them by the total number of players
# Multiplys it by 100 and rounded to two decimal places to get a percentage for each gender
male_percent_df = (male_count_df/player_count_df)*100
female_percent_df = (female_count_df/player_count_df)*100
other_percent_df = (other_count_df/player_count_df)*100

# Creates a data frame table that compares the genders in player coutn and percentage
percent_table_df = pd.DataFrame({
    "Gender" : ["Male", "Female", "Other / Non-Disclosed"],
    "Total Count" : [(male_count_df), (female_count_df), (other_count_df)],
    "Percentage of Players" : [male_percent_df, female_percent_df, other_percent_df]
    
})

# Formats the series to include a "%" at the end of each value in the column
percent_table_df["Percentage of Players"] = percent_table_df["Percentage of Players"].map("{:.2f}%".format)

# Showcases dataframe 
percent_table_df


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[8]:


# Locates the Gender column and if it is "Male", will add a count to via "Purchase ID"
male_purchase_df = purchase_data_df.loc[(purchase_data_df["Gender"] == "Male"), ["Purchase ID"]]
# Gets the length of the above Dataframe
male_purchase_good_df = len(male_purchase_df)


# Locates the Gender column and if it is "Male", will add a count to via "Price"
male_average_purchase_df = purchase_data_df.loc[(purchase_data_df["Gender"] == "Male"), ("Price")]
# will take the length of the data fram above and find the average
true_male_average_purchase_good_df = male_average_purchase_df.mean()


# Locates the Gender column and if it is "Male", will add a count to via "Price"
male_total_purchase_df = purchase_data_df.loc[(purchase_data_df["Gender"] == "Male"), ("Price")]
# will take the length of the data fram above and find the sum of all purchases 
true_male_total_purchase_good_df = male_total_purchase_df.sum()
#true_male_total_purchase_good_df


# MAthematically calculation to finds the average amount spent by each "Male" individual
male_average_spent_per_person_df = true_male_total_purchase_good_df/male_count_df




#Repeats steps above for the "Gender" == "Female" category 

female_purchase_df = purchase_data_df.loc[(purchase_data_df["Gender"] == "Female"), ["Purchase ID"]]
female_purchase_good_df = len(female_purchase_df)


female_average_purchase_df = purchase_data_df.loc[(purchase_data_df["Gender"] == "Female"), ("Price")]
true_female_average_purchase_good_df = female_average_purchase_df.mean()


female_total_purchase_df = purchase_data_df.loc[(purchase_data_df["Gender"] == "Female"),("Price") ]
true_female_total_purchase_good_df = female_total_purchase_df.sum()

female_average_spent_per_person_df = true_female_total_purchase_good_df/female_count_df




#Repeats steps above for the "Gender" == "Other / Non-Disclosed" category 

other_purchase_df = purchase_data_df.loc[(purchase_data_df["Gender"] == "Other / Non-Disclosed"), ["Purchase ID"]]
other_purchase_good_df = len(other_purchase_df)


other_average_purchase_df = purchase_data_df.loc[(purchase_data_df["Gender"] == "Other / Non-Disclosed"), ("Price")]
true_other_average_purchase_good_df = other_average_purchase_df.mean()


other_total_purchase_df = purchase_data_df.loc[(purchase_data_df["Gender"] == "Other / Non-Disclosed"),("Price") ]
true_other_total_purchase_good_df = other_total_purchase_df.sum()

other_average_spent_per_person_df = true_other_total_purchase_good_df/other_count_df


# In[9]:


# Creates a data frame showcasing "Gender", "Purchase Count", "Average Purchase Price"
#"Total Purchase Value" and"Average Total Purchase Per Person"
gender_purchase_table_df = pd.DataFrame({
    "Gender" : ["Male", "Female","Other / Non-Disclosed" ],
    "Purchase Count" : [male_purchase_good_df,female_purchase_good_df, other_purchase_good_df],
    "Average Purchase Price" : [true_male_average_purchase_good_df, true_female_average_purchase_good_df,
                                true_other_average_purchase_good_df],
    "Total Purchase Value" : [true_male_total_purchase_good_df, true_female_total_purchase_good_df, 
                              true_other_total_purchase_good_df],
    "Average Total Purchase Per Person" : [male_average_spent_per_person_df, female_average_spent_per_person_df,
                                          other_average_spent_per_person_df]
})

# Formats the column rolls that require "$" in front of the values and shows only 2 decimal points
gender_purchase_table_df["Total Purchase Value"] = gender_purchase_table_df["Total Purchase Value" ].map("${:.2f}".format)
gender_purchase_table_df["Average Purchase Price"] = gender_purchase_table_df["Average Purchase Price"].map("${:.2f}".format)
gender_purchase_table_df["Average Total Purchase Per Person"] = gender_purchase_table_df["Average Total Purchase Per Person"].map("${:.2f}".format)

# Showcases the dataframe
gender_purchase_table_df


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[10]:


# Makes a bin for the different age groups
age_bins = [0, 9.9, 14.9, 19.9, 24.9, 29.9, 34.9, 39.9, 50]
# Makes labels corresponding with the age groups above
age_group = ["<10", "10-14", "15-19", "20-24", "25-29",
            "30-34", "35-39", "40+" ]

# Creates another column in the data set for age demographics 
purchase_data_df["Age Demographic"] = pd.cut(purchase_data_df["Age"], age_bins, labels =age_group)


# In[11]:


# Creates a dataframe that drops repeated names found in the "SN" column
no_dupes_df = purchase_data_df.drop_duplicates(subset=["SN"])

# Groups the filtered data frame above and groups them to the BIns created in the abvoe cell
age_demos = no_dupes_df.groupby("Age Demographic")
# Gives a count for each indvidual Bin label under the column "Age"
age_range_df = age_demos["Age"].count()

# Gives the percentage of the age gaps in percentages comapred to the all players
age_range_demos_df = (age_range_df / player_count_df)*100

# Puts the above information into a dataframe
age_range_and_demo_df = pd.DataFrame({
                                      "Age Count" : age_range_df,
                                     "Age Percentage" : age_range_demos_df})

# Formats the "Age Percentage Column" to include the "%" at the end and only include 2 decimal places
age_range_and_demo_df["Age Percentage"] = age_range_and_demo_df["Age Percentage"].map("{:.2f}%".format)

# Displays teh dataframe 
age_range_and_demo_df


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[12]:


# Makes a bin for the different age groups
age_bins = [0, 9.9, 14.9, 19.9, 24.9, 29.9, 34.9, 39.9, 50]
# Makes labels corresponding with the age groups above
age_group = ["<10", "10-14", "15-19", "20-24", "25-29",
            "30-34", "35-39", "40+" ]

# Creates another column in the data set for age demographics 
purchase_data_df["Age Demographic Purchases"] = pd.cut(purchase_data_df["Age"], age_bins, labels =age_group)


# In[13]:


# Make a counter for purchase counts for each of the bins
age_analysis_purchase = purchase_data_df.groupby(["Age Demographic Purchases"]).count()["Purchase ID"]
# Find the average purchase spent for each of the bins
age_analysis_purchase_average = purchase_data_df.groupby(["Age Demographic Purchases"]).mean()["Price"]
# Finds the total amount purchased for each bin
age_analysis_purchase_total_price = purchase_data_df.groupby(["Age Demographic Purchases"]).sum()["Price"]

# Finds the average total spent person for each bin
age_analysis_purchase_average_price = age_analysis_purchase_total_price/age_range_df
# Puts the above findings into a data
age_analysis_purchase_df = pd.DataFrame({"Purchase Count" : age_analysis_purchase,
                                         "Average Purchase Price" : age_analysis_purchase_average,
                                         "Total Purchase Value" : age_analysis_purchase_total_price,
                                         "Avg Total Purchase Per Person" : age_analysis_purchase_average_price
                                        })


# Formats the above columns to include a "$" and rounds the values to 2 decimal places
age_analysis_purchase_df["Average Purchase Price"] = age_analysis_purchase_df["Average Purchase Price"].map("${:.2f}".format)
age_analysis_purchase_df["Total Purchase Value"] = age_analysis_purchase_df["Total Purchase Value"].map("${:.2f}".format)
age_analysis_purchase_df ["Avg Total Purchase Per Person"] = age_analysis_purchase_df[ "Avg Total Purchase Per Person"].map("${:.2f}".format)

# Shpwcases the data frame
age_analysis_purchase_df


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[14]:


# Groups dataframe by "SN" and counts how many purchases each unique "SN" has made
top_spenders_count = purchase_data_df.groupby(["SN"]).count()["Purchase ID"]
# Finds the average price each of the Top Spenders paid
top_spenders_average_price = purchase_data_df.groupby(["SN"]).mean()["Price"]
# Finds the total amount paid for each Top Spender
top_spenders_total_price = purchase_data_df.groupby(["SN"]).sum()["Price"]

# Puts the ablove findings intoa dataframe
top_spenders_df = pd.DataFrame({"Purchase Count" : top_spenders_count,
                                         "Average Purchase Price" : top_spenders_average_price,
                                         "Total Purchase Value" : top_spenders_total_price
                                        })

# Formats the columsn to include "$" and show only 2 decimal points
top_spenders_df["Average Purchase Price"] =top_spenders_df["Average Purchase Price"].map("${:.2f}".format)  
top_spenders_df["Total Purchase Value"] =top_spenders_df["Total Purchase Value"].map("${:.2f}".format)


# Displays the top 5 Spenders in the the game 
top_spenders_df.sort_values(by='Purchase Count', ascending=False).head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[15]:


# Indexed the datframe by "Item ID" and "Item Name" and makes a counter
most_popular = purchase_data_df.groupby(["Item ID", "Item Name"])
most_popular.count()

# Creates a new dataframe with the index above and counts the purchase ID
most_popular_df = pd.DataFrame(most_popular["Purchase ID"].count())
#most_popular_df

# Get Total purchase value by Item
most_popular_total = most_popular["Price"].sum()
most_popular_total
most_popular_total_formatted = most_popular_total.map("${:,.2f}".format)
most_popular_total_formatted

# Get purchase price by Item
most_popular_price = most_popular["Price"].mean()
most_popular_price_formatted = most_popular_price.map("${:,.2f}".format)
most_popular_price_formatted

# Add new columns and values into the dataframe
most_popular_df["Item Price"] = most_popular_price_formatted
most_popular_df["Total Purchase Value"] =most_popular_total  
#most_popular_df.head()

# Makes a new dataframe, changes the name of "Purchase ID" to "Purchase Count"
most_popular_new_df = most_popular_df.rename(columns={"Purchase ID":"Purchase Count"})
most_popular_new_df


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[16]:


# Sorts the dataframe above from most profitabel to least profitable 

Top_5_Items_df= most_popular_new_df.sort_values("Purchase Count", ascending=False)
Top_5_Items_df.head()


# In[ ]:




