
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt

# need to save the Python file into the same folder as the csv file, otherwise need to change the path

wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

# examine the first dataframe

# print(df1)

print(wood['Name'].nunique())
print(steel['Name'].nunique())

# 61 and 63 distinct roller coasters in Wood and Steel rankings.

print(wood['Supplier'].nunique())
print(steel['Supplier'].nunique())

# 32 and 15 distinct suppliers in Wood and Steel rankings.

info1 = wood.groupby('Year of Rank')['Rank'].count().reset_index()

print(info1)

# Year 2013 has 10 Rank counts, etc.

# plt. clf() clears the entire current figure with all its axes, but leaves the window opened, such that it may be reused for other plots. 
# plt. close() closes a window, which will be the current window, if not specified otherwise                   

# Write a function that will plot the ranking of a given roller coaster over time as a line
# Your function should take a roller coaster’s name and a ranking DataFrame as arguments.
def roller_ranking(coaster_name, park_name, df):
    ranking = df[(df['Name'] == coaster_name) & (df['Park'] == park_name)] 
    # select a subset of the ranking DataFrame based on two criteria
    x = ranking['Year of Rank']
    # x is a Series object, not a dataframe.
    y = ranking['Rank']
    plt.plot(x, y, marker = 'o', label = coaster_name)
    plt.xlabel('Year')
    plt.ylabel('Rank of Roller Coasters')
    plt.legend()
    plt.title(coaster_name + ' ranking over the years')
    plt.show()

#indentation error: replace all the tabs with 手打的空格
ax1 = plt.subplots()
roller_ranking('El Toro', 'Six Flags Great Adventure', wood)
# call with the name 'El Toro' and the Wood Ranking dataframe to test.

# Write a function that will plot the ranking of TWO given roller coaster over time as lines
def roller_ranking_two(name1, name2, park1, park2, df):
    ranking1 = df[(df['Name'] == name1) & (df['Park'] == park1)]
    ranking2 = df[(df['Name'] == name2) & (df['Park'] == park2)]
    # select two DataFrames that satisfy certain criteria
    x = ranking1['Year of Rank']
    # the x-axis should be the same for both roller coasters
    y1 = ranking1['Rank']
    y2 = ranking2['Rank']
    plt.plot(x, y1, marker = 'o', color = 'green', label = name1)
    plt.plot(x, y2, marker = 's', color = 'black', label = name2)
    plt.xlabel('Year')
    plt.ylabel('Rank of Roller Coasters')
    plt.legend()
    plt.title(name1 + " & " + name2 + " ranking over the years")
    plt.show()

ax2 = plt.subplots()
roller_ranking_two('El Toro', 'Boulder Dash', 'Six Flags Great Adventure', 'Lake Compounce', wood)

# Write a function that will plot the ranking of top N given roller coaster over time as lines
def roller_ranking_top_n(n, df):
    top_n_rankings = df[df['Rank'] <= n].reset_index() # select all rows that have a Rank less than or equal to n
    plt.figure(figsize = (8, 6))  # create a figure to plot
    for coaster in set(top_n_rankings['Name']):
        coaster_ranking = top_n_rankings[top_n_rankings['Name'] == coaster]
        plt.plot(coaster_ranking['Year of Rank'], coaster_ranking['Rank'], label = coaster, marker = 'o')
    plt.legend()
    plt.xlabel('Year of Rank')
    plt.ylabel('Rank of Roller Coasters')
    plt.title('Rank of Top ' + str(n) + " roller coasters over time")
    
# test the function
roller_ranking_top_n(2, wood)
roller_ranking_top_n(4, steel)

# plt.close('all') # comment for all previous plots to show.

rc = pd.read_csv('roller_coasters.csv') # pay attention to the 's' in the file name
print(rc.head()) # inspect the dataframe

# Write a function that plots a histogram of any numeric column of the roller coaster dataframe
# inputs: dataframe and a column name
# pd.dropna() to remove all missing values before plotting the histogram


def create_hist(df, name):
    # to check if the column contains numeric or qualitative information
    if type(df[name][0]) == str:
        print("Please make sure the column you enter contains numeric information")
    else:
        if name == 'height':
            df = df[df[name] <= 140] # cut the outliers
            df_new = df.dropna(axis = 0, how = 'any') # drop missing values
        else:
            df_new = df.dropna(axis = 0, how = 'any')
        df_name = df_new[name]
        plt.hist(df_name, density = True)
        plt.xlabel('time')
        plt.ylabel('frequency')
        plt.title('Histogram of ' + name)
        
ax3 = plt.subplots()
create_hist(rc, 'height')

print(type(rc['speed'].reset_index()['speed'][0]))

# Write a function that creates a bar chart showing the number of inversions for each roller coaster
# Your function should take the roller coaster DataFrame and an amusement park name as arguments.

# print(rc['num_inversions'][0])

w = 10
h = 8

def create_bar(df, park_name):
    park_coasters = df[df['park'] == park_name] # select a subset of the whole dataframe
    park_coasters = park_coasters.sort_values(by = ['num_inversions'], ascending = False)
    coaster_names = park_coasters['name']
    number_inversions = park_coasters['num_inversions']
    plt.figure(figsize = (w, h))
    ax = plt.subplot()
    plt.bar(range(len(coaster_names)), number_inversions)
    ax.set_xticks(range(len(coaster_names)))
    ax.set_xticklabels(coaster_names, rotation = 'vertical')
    plt.xlabel('Roller Coasters')
    plt.ylabel('Number of Inversions at each park')
    plt.legend(coaster_names)
    plt.title('Number of inversions')
    
# create_bar(rc, 'Lake Compounce')


# Write a function that creates a pie chart that compares the number of operating roller coasters 
# ('status.operating') to the number of closed roller coasters ('status.closed.definitely'). 
# Your function should take the roller coaster DataFrame as an argument. 

def create_pie(df):
    operating = df[df['status'] == 'status.operating']
    closed = df[df['status'] == 'status.closed.definitely']
    status_counts = [len(operating), len(closed)]
    plt.pie(status_counts, autopct = '%0.1f%%', labels = ['Operating', 'Closed'])
    plt.axis('equal')
    plt.legend()
    plt.title('Status of Roller Coasters')
         
ax4 = plt.subplots()    
create_pie(rc)

# Write a function that creates a scatterplot of two numeric columns of the rc dataframe
# Your function should take the roller coaster DataFrame and two-column names as arguments.

def create_scatter(df, name1, name2):
    # first we want to check if the columns contain numeric information
    if (type(df[name1][0]) == str) or (type(df[name2][0]) == str):
        print("Please make sure the column you enter contains numeric information")
    else:
        if name1 == 'height':
            df = df[df[name1] <= 140] # cut the outliers
            df_new = df.dropna(axis = 0, how = 'any') # drop missing values
        elif name2 == 'height':
            df = df[df[name2] <= 140] # cut the outliers
            df_new = df.dropna(axis = 0, how = 'any') # drop missing values           
        else:
            df_new = df.dropna(axis = 0, how = 'any')
        df_name_one = df_new[name1]
        df_name_two = df_new[name2]
        # df_name = np.array(df_name) # change this to an array and put into histogram
        plt.scatter(df_name_one, df_name_two, marker = 'o')
        plt.xlabel(name1)
        plt.ylabel(name2)
        plt.title('Plot of ' + name2 + " against " + name1)

ax5 = plt.subplots()
create_scatter(rc, 'speed', 'length')

plt.close('all') # --- comment this line for previous graphs to show

# rc.sort_values(by = ['seating_type'], ascending = False)

# What roller coaster seating type is most popular? Sit Down.
popularity = rc['seating_type'].value_counts()
this_df = rc['seating_type']
print(popularity)
ax6 = plt.subplots()
plt.pie(popularity, labels = this_df.unique())
plt.legend()



        
    

    











        
        
    
    




