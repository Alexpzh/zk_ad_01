import pandas as pd

# data = [1,2,3,4,5]
#
# series = pd.Series(data)
#
# print(series)
def dz1():
    # data = {
    #     'Name': ['Alice', 'Bob', 'Roma', 'Anna'],
    #     'Age': [23, 45, 17, 24],
    #     'City': ['New York', 'LA', 'Chicago', 'Moscow']
    # }
    #
    # df = pd.DataFrame(data)
    #
    # df.to_csv('output.csv', index=False)
    print('\n\nЗадача 1\nИнформация по участникам ЕВРО 2024\n')

    df = pd.read_csv('euro2024_players.csv')
    print('\nЗабито голов:')
    print(df.sort_values(by='Goals', ascending=False).head(10))
    print('\nСтоимость контрактов:')
    print(df.sort_values(by='MarketValue', ascending=False).head(10))
    print('\nПредставительство клубов по числу игроков:')
    cnt = df.groupby('Club')['Club'].count()
    print(cnt.sort_values(ascending=False).head(10))
    print('\nСамые дорогие сборные:')
    cnt = df.groupby('Country')['MarketValue'].sum()
    print(cnt.sort_values(ascending=False).head(10))
    #print(cnt.sort_values(by=ascending=False).head(10))
    #df['Club_cnt'] = df['Club'].count()
    #print(df.sort_values(by='Club_cnt', ascending=False).head(10))
    print('\nИнфо:')
    print(df.info())
    print('\nОписание:')
    print(df.describe())

def dz2():
    print('\n\nЗадача 2\n')
    df = pd.read_csv("dz.csv")
    df.fillna({'City' : 'Не указан'}, inplace = True)
    df.fillna({'Salary': 0}, inplace = True)
    print(df)
    print('\nСредняя зарплата (всего):')
    print(round(df[['Salary']].mean(),2))
    print('\nСредняя зарплата по городам:')
    # Группировка по городам
    #print([gr for gr in df if df['City'] != 'Не указан'])
    df1 = df[df['City'] != 'Не указан']
    group = round(df1.groupby('City')['Salary'].mean(),2)
    print(group)
    #print (group.loc['City'])

dz1()
dz2()