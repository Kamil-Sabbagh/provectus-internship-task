import pandas as pd
import os


if 'output.csv' not in os.listdir() :
    os.mknod('output.csv')


df = pd.DataFrame( columns= ['user_id' , 'first_name' , 'last_name', 'birthts' , 'img_path'])

for file in os.listdir('02-src-data/') :
    if 'csv' in file :
        data = pd.read_csv(f'02-src-data/{file}')
        id = file[:file.find('.')]
        img = 'Not found'
        if f'02-src-data/{id}.png' in os.listdir('02-src-data/'):
            img = f'02-src-data/{id}.png'
        add = {'user_id': id , 'first_name': data.iloc[0 , 0]  , 'last_name':data.iloc[0 , 1] , 'birthts':data.iloc[0 , 2], 'img_path':f'02-src-data/{id}.png'}
        df = df.append(add , ignore_index=True)


df = df.sort_values('user_id')
df.to_csv('output.csv', index=False)
