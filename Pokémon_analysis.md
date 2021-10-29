# Pokémon Database 



# Question 1 : What's the most common type in the Pokémon world? 

There's 18 unique types, an elemental property of a Pokémon and their moves, in the Pokémon series. Each Pokémon has at least one type, and can have up to two different types (a Primary type and Secondary type). In fact, according to this database I found, about 52.9% of the total Pokémon has secondary type. 

Since I'm curious of what's the most common type used in the series,  I've decided to include both Primary and Secondary types of a Pokémon. For example, a WATER/ICE type Pokémon will be counted both as a WATER type and ICE type. 

![type_piechart](C:\Users\Hydra\Desktop\LDSBC\BYU-i\Fall2021\Applied Programming(CSE310)\analysis\type_piechart.png)





![type_count](C:\Users\Hydra\Desktop\LDSBC\BYU-i\Fall2021\Applied Programming(CSE310)\analysis\type_count.png)



It seems like WATER type is the most commonly seen type in the pokemon series with 154 pokemon with WATER type (either as a Primary type or Secondary type). This makes it about 10% of the pokemon. The next most common types were NORMAL, FLYING, and PSYCHIC types, all at almost 7.5~7.9% range. 



## Question 2: TOP 10 Pokemon with highest base stats? Average Base Stats for each types? 

Each pokemon has 6 different stats: Attack, Special Attack, HP, Defense, Special Defense, and Speed. The base stats I will be talking about will be sum of these numbers for each Pokemon. Here's the graph of top 10 highest base stats: 

![top10_pkmn](C:\Users\Hydra\Desktop\LDSBC\BYU-i\Fall2021\Applied Programming(CSE310)\analysis\top10_pkmn.png)



How about base stats for each types? For this question, I've decided to simplify the question a little bit by only looking at the main type category(Primary type) of each Pokémon. Please do note that the bar might look different if we added in Secondary type. 



![type_basestats](C:\Users\Hydra\Desktop\LDSBC\BYU-i\Fall2021\Applied Programming(CSE310)\analysis\type_basestats.png)

Dragon types seems to be the Pokémon type with the highest base stats, regardless of the fact that it makes up only about 4% of the all Pokémon. This makes more sense because most of the legendary Pokémon's are in this group. 



## Question 3: Dragon Type Pokémon's characteristics



|         | Attack  | Defense | HP      | Sp.Attack | Sp.Defense | speed   |
| ------- | ------- | ------- | ------- | --------- | ---------- | ------- |
| Psychic | 76.2658 | 72.3418 | 73.6709 | 99.0759   | 87.6835    | 80.3165 |
| Dragon  | 107.024 | 83.9268 | 85.2439 | 91.7317   | 84.0976    | 84.3415 |



It seems like Dragon type pokemons tend to be physical attacker, with about 107 as an average Attack stats. They have higher Defense stats and HP as well. Psychic types are more focused on Special attacks, and they are, on average, low on Defense and HP. 