import requests

if __name__ == '__main__':

    url = 'https://akabab.github.io/superhero-api/api/all.json'

    intelligence = -1

    persons = requests.get(url).json()
    for i in range(len(persons)):
        if persons[i]['name'] in ('Hulk', 'Captain America', 'Thanos'):
            if persons[i]['powerstats']['intelligence'] > intelligence:
                intelligence = persons[i]['powerstats']['intelligence']
                person = persons[i]['name']
    print(f'Персонаж {person} является самым умным из тройки Hulk, Captain America, Thanos')
