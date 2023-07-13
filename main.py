import random
import requests


def random_poke():
    poke_num = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(poke_num)
    response = requests.get(url)
    poke = response.json()

    return {
        'name': poke['name'],
        'id': poke['id'],
        'height': poke['height'],
        'weight': poke['weight'],
        'base stat': poke['stats'][0]['base_stat'],
        'experience': poke['base_experience']
    }


def duel():
    player_one = random_poke()
    print('Your pokemon is {}'.format(player_one['name']))
    player_two = random_poke()
    print('Your opponent\'s pokemon is {}'.format(player_two['name']))

    stat_chosen = input('Which stat do you use(id, height, weight, base stat, experience)?')
    stat_one = player_one[stat_chosen]
    stat_two = player_two[stat_chosen]

    if stat_one > stat_two:
        print('Hurray!!!🤩')
    elif stat_one < stat_two:
        print('Try again..😔')
    else:
        print('There must be a winner! Play again?')

    print('Your stat: {}\nOpponent stat: {}'.format(stat_one, stat_two))


duel()
