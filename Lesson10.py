import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
#data.loc[data['whoAmI'], index=['human', 'robot']
data.loc[data['whoAmI'] == 'robot', 'robot']  = '1'
data.loc[data['whoAmI'] != 'robot', 'robot']  = '0'
data.loc[data['whoAmI'] == 'human', 'human']  = '1'
data.loc[data['whoAmI'] != 'human', 'human']  = '0'
#data[['human','robot']]
data.head(10)
