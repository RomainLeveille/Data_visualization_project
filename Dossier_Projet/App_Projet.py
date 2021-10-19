import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.write("Romain Leveillé Nizerolle, 2021")
st.sidebar.write ("My linkedin : https://www.linkedin.com/in/romain-leveill%C3%A9-nizerolle-9186b4177/")
st.title('Visualization of my Samsung Health Data')


path = "donnee_projet.csv"
df = pd.read_csv(path, delimiter = ',') 


df["update_time"]= df["update_time"].map(pd.to_datetime)


def get_weekday(dt) : return dt.weekday()
    
df['weekday'] = df['update_time'].map(get_weekday)

st.write(df.describe())
fig1 = plt.figure(figsize=(12, 8))
plt.hist(df.weekday, bins = 7, rwidth = 0.8, range = (-.5, 6.5), figure = fig1)
plt.xlabel('Day of the week', figure = fig1)
plt.ylabel('Frequency', figure = fig1)
plt.title('Frequency about the day of the week', figure = fig1);    
plt.xticks(np.arange(7), 'Mon Tue Wed Thu Fri Sat Sun'.split(), figure = fig1)
st.pyplot(fig1)

st.write("As you can see, this figure only show the frequency of the times I walk each day, but not how long I walk.")

st.write("So, we will focus on the average number of steps I did each day of the week and each hour of the week")

def get_hours(dt) : 
    return dt.hour

df['hour'] = df['update_time'].map(get_hours)

def get_year(dt) : return dt.year()
#df['year'] = df['update_time'].map(get_year)



#fig6 = plt.figure(figsize=(12, 8))
#sns.lineplot(x = df.year, y = df.step_count, figure = fig6)
#plt.xlabel('Year', figure = fig6)
#plt.ylabel('Number of steps', figure = fig6)
#plt.title('Number of steps about the year', figure = fig6)

#st.pyplot(fig6)

fig2 = plt.figure(figsize=(12, 8))
sns.lineplot(x = df.weekday, y = df.step_count, figure = fig2)
plt.xlabel('Day of the week', figure = fig2)
plt.ylabel('Number of steps', figure = fig2)
plt.title('Number of steps about the day of the week', figure = fig2)
plt.xticks(np.arange(7), 'Mon Tue Wed Thu Fri Sat Sun'.split(), figure = fig2)

st.pyplot(fig2)

fig3 = plt.figure(figsize=(12, 8))
sns.lineplot(x = df.hour, y = df.step_count, figure = fig3)
plt.xlabel('Hour of the day', figure = fig3)
plt.ylabel('Number of steps', figure = fig3)
plt.title('Number of steps about the hour of the day', figure = fig3)
plt.xticks(np.arange(24), '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24'.split(), figure = fig3)

st.pyplot(fig3)

def count_rows(rows): return len(rows)

#df2 = df.groupby(['step_count', 'weekday']).apply(count_rows).unstack()
#st.write(df2.head())

#fig4 = plt.figure(figsize=(12, 8))
#heatmap = sns.heatmap(df2, linewidths = .5, figure = fig4)
#Annoted heatmap
#heatmap.set_yticklabels(('Lun Mar Mer Jeu Ven Sam Dim').split(), rotation='horizontal', figure = fig4)
#st.pyplot(fig4)


st.write('It is good to see all these times I walked, but it is better if we can see all the calories I burned.')
st.write('So, we will now see my burned calories each day of the week.')


fig4 = plt.figure(figsize=(12, 8))
sns .lineplot(x = df.weekday, y = df.calorie, figure = fig4)
plt.xlabel('Day of the week', figure = fig4)
plt.ylabel('Calories burned', figure = fig4)
plt.title('Calories burned each day of the week', figure = fig4);    
plt.xticks(np.arange(7), 'Mon Tue Wed Thu Fri Sat Sun'.split(), figure = fig4)
st.pyplot(fig4)

st.write("And what about each month?")

def get_month(dt): return dt.month 

df['month'] = df['update_time'].map(get_month)

#select_year = st.sidebar.selectbox('Select the year')

fig5 = plt.figure(figsize=(12, 8))
sns .lineplot(x = df.month, y = df.calorie, figure = fig5)
plt.xlabel('Month', figure = fig5)
plt.ylabel('Calories burned', figure = fig5)
plt.title('Calories burned each month', figure = fig5);    
plt.xticks(np.arange(12), 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split(), figure = fig5)
st.pyplot(fig5)

