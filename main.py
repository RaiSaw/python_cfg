import random
import requests
import csv
# dict to store the results
# pokemon_table = {}

# random choices for player
def random_pokes():
    for _ in range(5):
        poke_num = random.randint(1, 151)
        print(poke_num)

    poke_choice = input('Which pokemon do you choose?\n')
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(poke_choice)
    response = requests.get(url)
    poke = response.json()

    pokemon_dict = {
        'name': poke['name'],
        'id': poke['id'],
        'height': poke['height'],
        'weight': poke['weight'],
        'stat': poke['stats'][0]['base_stat'],
        'experience': poke['base_experience']
    }
    return pokemon_dict
    # print(pokemon_dict)
    # with open('pokemon.txt', 'w+') as text_file:
    # pokemon_table = pokemon_table + poke_dict
    # text_file.write(pokemon_table)

#random poke for opponent
def opponent_random():
    opp_num = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(opp_num)
    response = requests.get(url)
    poke = response.json()

    pokemon_opponent = {
        'name': poke['name'],
        'id': poke['id'],
        'height': poke['height'],
        'weight': poke['weight'],
        'stat': poke['stats'][0]['base_stat'],
        'experience': poke['base_experience']
    }
    return pokemon_opponent
    # print('Your opponent chose: {}'.format(poke['name'].capitalize()))

#def random_stat():
 #   random_number = random.randint(1, 2)
  #  if random_number == 1:
   #     player_one = 0
    #else:
     #   player_two = 1
    #return


# ready, play, logic
def duel():
    player_one = random_pokes()
    player_two = opponent_random()

    print('You chose pokemon: {}\n'.format(player_one['name'].capitalize()))
    print('{}\n'.format(player_one))

    stat_choice = input('Which stat do you use(id, height, weight, stat, experience)?\n')
    stat_one = player_one[stat_choice]
    stat_two = player_two[stat_choice]

    print('Your opponent chose pokemon: {}\n'.format(player_two['name'].capitalize()))
    print('{}\n'.format(player_two))

    if stat_one > stat_two:
        print('Hurray! You won!🤩')

    elif stat_one < stat_two:
        print('Oh-oh! Try again..😔')

    else:
        print('It\'s a tie!🤝')

    print('Your {}: {}\nOpponent {}: {}'.format(stat_choice, stat_one, stat_choice, stat_two))



duel()

#record data from game
#poke_duel = ['player', 'poke', 'stat', 'stat_value', 'winner']
#data = [
    #{'player': 1, 'poke': 'Jigglypuff', 'stat': 'id', 'stat_value': 90, 'winner': 'true'},
#]
#with open('poke.csv', 'w+') as csv_file:
    #spreadsheet = csv.DictWriter(csv_file, fieldnames=poke_duel)
    #spreadsheet.writeheader()
    #spreadsheet.writerows()
