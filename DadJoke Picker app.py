import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format('DAD JOKE 2022')
header = colored(header, color = 'magenta')
print(header)

user_input = input('What would you like to search for? ')
url = 'https://icanhazdadjoke.com/search'
res = response = requests.get(
    url,
    headers = {'Accept': 'application/json'},
    params = {
        'term': user_input
    }
).json()

num_jokes = res['total_jokes']
results = res['results']

if num_jokes > 1:
    print(f'There are {num_jokes} jokes about "{user_input}". Here`s one: ')
    print(choice(results)['joke'])
elif num_jokes == 1:
    print(f'There is only one joke about "{user_input}"')
    print(results['joke'])
else:
    print(f'Sorry! There are NO jokes with your term "{user_input}"')





# print(res)