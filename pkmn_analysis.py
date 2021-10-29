import pandas as pd 
import seaborn as sns 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure



#%%
pkmn = pd.read_csv("pokemon_data.csv")
pkmn.head()

# %%

# Question 1: What's the most common type for pokemon? 
#There are pokemon with double types eg. (water type or ice/water type. )

#Total number of pokemon 
total_pkmn = len(pkmn)

#Get counts of unique values using value_counts(), save that as a dataframe. 
primary_counts = pkmn['Primary Type'].value_counts().rename_axis('type').reset_index(name='primary_counts')
scnd_counts = pkmn['Secondary type'].value_counts().rename_axis('type').reset_index(name='second_counts')

#merge the 
total_types = pd.merge(primary_counts, scnd_counts, on = "type")

total_types['total_counts'] = total_types['primary_counts'] + total_types['second_counts']
total_types['type_percent'] = (total_types['total_counts'] / sum(total_types['total_counts'])) *100

pkmn_types = pkmn[['Primary Type', 'Secondary type']]

# %% 
# A bit of a side quest... 
# How many pokemon have secondary type? 
dual_type = [] 

def isNaN(string):
    return string != string

# Secondary Type is not NaN, meaning it's a dual type pokemon
for index, row in pkmn.iterrows():
    if not isNaN(row['Secondary type']):
        dual_type.append(row['Name'])

dual_type_number = len(dual_type)
#Number of dual type pokemon: 
print(f"Number of dual type pokemon: {dual_type_number}")
print(f"That's {dual_type_number/ total_pkmn :.1%} of {total_pkmn} pokemon available")


# %% 
#Pie chart

colors = sns.color_palette('muted')[0:10]
plt.figure(figsize=(15, 5), dpi=80)
plt.title("Percentage of types")

plt.pie(total_types['total_counts'], labels = total_types['type'], colors = colors, autopct='%.0f%%')
plt.show()


# %% 
sns.set(rc={'figure.figsize':(20,8)})
total_baplot = sns.barplot(data = total_types, x= "type", y = "total_counts")


# %%
# Question 2: What's the top 10 pokemon with highest base stats (total stats)?
# And what's the average base stat for each type(in this case, filtered based on primary type)?


top10 = pkmn.nlargest(10,'Total')

#Created separate dataframe, so I can change the Names to Name2 only if the Name2 is not null. 
plot_top10 = top10[['Name','Name2','Total']]
plot_top10['Name'] = plot_top10['Name'].where(plot_top10['Name2'].isnull(), plot_top10['Name2'])

sns.set(rc={'figure.figsize':(20,8)})
top10_bar = sns.barplot(data=plot_top10, x="Name", y="Total").set(
    title= "Top 10 Pokemon with highest total base stats "
)

#%% 

#Get a list of unique types
type_list = pkmn['Primary Type'].unique()
#Empty dictionary to save all the types + filtered dataframe. 
type_df = {} 
#Another dictionary to save average 
type_base_average = {} 

#Save all the filtered types into the dictionary 
for x in type_list: 
    type_df[x] = pkmn[pkmn['Primary Type'] == x]

for x in type_df:
    type_base_average[x] = type_df[x]['Total'].mean()

#Switch the dictionary to dataframe 
type_average = pd.DataFrame.from_dict(type_base_average,orient='index',columns=[ 'Average Basestats Primary'])
type_average = type_average.rename_axis('type')

total_types = pd.merge(total_types,type_average ,on = "type")

#List descending order, Top 5 types
total_types.nlargest(5,'Average Basestats Primary')

#%%
#Chart 
sns.set(rc={'figure.figsize':(20,8.27)})

type_bar = sns.barplot(
    data=total_types, x= 'type', y = 'total_counts',ci=None
    ).set(title = "Count of Each Pokemon Types")

# %% 
# Base Stats 
sns.set(rc={'figure.figsize':(20,8.27)})

type_bar = sns.barplot(
    data=total_types, x= 'type', y = 'Average Basestats Primary',ci=None
    ).set(title = "Average Total Base Stats of each type")


# %%
# Question 3: Dragon Type pokemon's characteristics
dragon = {}
psychic = {}

# make use of the type_df 

#populate dragon type dictionary 
dragon['Attack'] = type_df['DRAGON']['Attack'].mean()
dragon['Defense'] = type_df['DRAGON']['Defense'].mean()
dragon['HP'] = type_df['DRAGON']['HP'].mean()
dragon['Sp.Attack'] = type_df['DRAGON']['Sp.Attack'].mean()
dragon['Sp.Defense'] = type_df['DRAGON']['Sp.Defense'].mean()
dragon['speed'] = type_df['DRAGON']['Speed'].mean()
dragon['type'] = "Dragon"

dragon_df = pd.DataFrame.from_dict(dragon,orient='index',columns=[ 'Dragon'])
dragon_df= dragon_df.T

#Let's compare it with normal type 

#populate dragon type dictionary 
psychic['Attack'] = type_df['PSYCHIC']['Attack'].mean()
psychic['Defense'] = type_df['PSYCHIC']['Defense'].mean()
psychic['HP'] = type_df['PSYCHIC']['HP'].mean()
psychic['Sp.Attack'] = type_df['PSYCHIC']['Sp.Attack'].mean()
psychic['Sp.Defense'] = type_df['PSYCHIC']['Sp.Defense'].mean()
psychic['speed'] = type_df['PSYCHIC']['Speed'].mean()
psychic['type'] = "Psychic"

psychic_df = pd.DataFrame.from_dict(psychic,orient='index',columns=['Psychic'])
psychic_df = psychic_df.T

result = pd.concat([psychic_df,dragon_df])
print(result.to_markdown())

# %%
