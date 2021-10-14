# Use this cell to begin your analysis, and add as many as you would like!
import matplotlib.pyplot as plt
import pandas as pd

#To see the large view of the data
plt.rcParams['figure.figsize'] = [15, 7]


#read datset using pandas
data = pd.read_csv('datasets/office_episodes.csv')


#print first 5 rows of the dataset
data.head()

#check the dataset 
data.info()

#describe the dataset for more clear view
data.describe()

# Checking for the presence of guest stars 
size=[]
for rows in data['has_guests']:
     if rows == False:
        size.append(25)
     else:
        size.append(250)

# Check first 10 values in the list      
size[:10]

#Only guest star apperances and non-guest star apperances
with_guest = data[data['has_guests'] == True]
without_guest = data[data['has_guests'] == False] 
#Plotting number of viwers in million per eposide numberfig = plt.figure()

# Create a scatter plot
plt.scatter(x=data['episode_number'],
            y=data['viewership_mil'],
            c= cols,
            s= size)

# Create a title
plt.title("Popularity, Quality, and Guest Appearances on the Office")

# Create an x-axis and an y-axis
plt.xlabel("Episode Number")
plt.ylabel("Viewership (Millions)")

# Show the plot
plt.show()


# Plotting non-guest starring episodes data
fig = plt.figure() 
plt.scatter(x=without_guest['episode_number'],
             y=without_guest['viewership_mil'],
             c= without_guest['colors'],
             s= without_guest['size'])  

# Plotting guest starring episodes data
plt.scatter(x= with_guest['episode_number'],
            y= with_guest['viewership_mil'],
            c=  with_guest['colors'],
            s= with_guest['size'],
            marker = '*')

# Create a title
plt.title("Popularity, Quality, and Guest Appearances on the Office")

# Create an x-axis and an y-axis
plt.xlabel("Episode Number")
plt.ylabel("Viewership (Millions)")

# Show the plot
plt.show()
# The Maximum view
max_view = max(data["viewership_mil"])

# Filter the Dataframe row that has the most watched episode
most_watched_ep = data.loc[data["viewership_mil"] == max_view]

# Top guest stars that were in that 
top_star = most_watched_ep[["guest_stars"]]

#print top stars
top_star
