import pandas as pd
import numpy as np
import seaborn as sns #importing our visualization library
import matplotlib.pyplot as plt


df = pd.read_csv('netflix_titles.csv')


df.head()


df.isnull().sum()


sns.heatmap(df.isnull(),cmap = 'viridis')


#We have null values in  director, cast,country,date_added and rating.So lets deal with it.


df['rating'].value_counts().unique()


#In the above data, we can choose to drop the director and cast columns completely as they are not a huge part for us while we visualize the data and they dont add any significant value to our analysis. We are only focused on visualizing this data hence dropping two columns wont be any trouble for us.But this should not be a regular practise as if we are making a recommender system, we cannot drop the director and cast of a movie as these are a key feature used to recommend movies to users


df.drop(['director','cast'],axis = 1,inplace = True)


df.head()


#We replaced all the Nan values in the country column with United States as Netflix was created in the USA and every show is aired on Netflix US. So instead of dropping the whole column we just replaced the values in it in order to save our data.


df['country'].replace(np.nan, 'United States',inplace  = True)


#We already have released year for each movie and hence even if we dont have released date,it wont affect our analsis much. Hence we can Drop released date column.


df.drop(['date_added'],axis =1,inplace = True)


df.head()


df['rating'].value_counts()


df['listed_in'].value_counts()


#As we can see we only have 10 missing values in our rating column, we can either drop them or replace them. We have TV-MA which is the most common raing and hence we can replace all these nan values with TV-MA.


df['rating'].replace(np.nan, 'TV-MA',inplace  = True)


df.isnull().sum()


#We have now dealt with all of our missing data so lets get started with our data visualization


df.head()


sns.countplot(x='type',data = df) #looking at number of Movies and TV shows


plt.figure(figsize = (12,8))
sns.countplot(x='rating',data = df)


plt.figure(figsize = (35,6))
sns.countplot(x='release_year',data = df)


#As we can see most of the Movies and Tv shows on Netflix are Released in the past decade and very few were released earlier


plt.figure(figsize=(16,6))
sns.scatterplot(x='rating',y='type',data = df) #analysing the type, whether its a movie or a movie v/s the rating it has


plt.figure(figsize = (12,8))
sns.countplot(x='rating',data = df,hue='type')



df['rating'].value_counts().plot.pie(autopct='%1.1f%%',figsize=(20,35)) #distribution according to the rating
plt.show()



old = df.sort_values("release_year", ascending = True) #oldest movies available on netflix
old = old[old['duration'] != ""]
old[['title', "release_year"]][:15]


tag = "Stand-Up Comedy" #standup shows on Netflix
df["relevant"] = df['listed_in'].fillna("").apply(lambda x : 1 if tag.lower() in x.lower() else 0)
com = df[df["relevant"] == 1]
com[com["country"] == "United States"][["title", "country","release_year"]].head(10)


tag = "Kids' TV" #Kids TV shows on Netflix
df["relevant"] = df['listed_in'].fillna("").apply(lambda x : 1 if tag.lower() in x.lower() else 0)
com = df[df["relevant"] == 1]
com[com["country"] == "United States"][["title", "country","release_year"]].head(10)


df_countries = pd.DataFrame(df.country.value_counts().reset_index().values, columns=["country", "count"])
df_countries.head()

date = pd.DataFrame(df.release_year.value_counts().reset_index().values, columns=["Year", "Count"])
date.head()


plt.figure(figsize=(12,6))
df[df["type"]=="Movie"]["release_year"].value_counts()[:20].plot(kind="bar",color="Red")
plt.title("Frequency of Movies which were released in different years and are available on Netflix")

plt.figure(figsize=(12,6))
df[df["type"]=="TV Show"]["release_year"].value_counts()[:20].plot(kind="bar",color="Blue")
plt.title("Frequency of TV shows which were released in different years and are available on Netflix")


plt.figure(figsize=(12,6))
df[df["type"]=="Movie"]["listed_in"].value_counts()[:10].plot(kind="barh",color="black")
plt.title("Top 10 Genres of Movies",size=18)

plt.figure(figsize=(12,6))
df[df["type"]=="TV Show"]["listed_in"].value_counts()[:10].plot(kind="barh",color="brown")
plt.title("Top 10 Genres of TV Shows",size=18)

