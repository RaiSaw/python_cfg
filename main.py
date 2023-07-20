import random
import requests
import csv

# data to dict stored in file
pokemon_table = {}


# random pokemon id
def random_poke():
    poke_id = random.randint(1, 151)

    if poke_id in pokemon_table:
        return pokemon_table[poke_id]
    else:
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(poke_id)
    response = requests.get(url)
    poke = response.json()

    pokemon = {
        'name': poke['name'],
        'id': poke['id'],
        'height': poke['height'],
        'weight': poke['weight'],
        'stat': poke['stats'][0]['base_stat'],
        'experience': poke['base_experience']
    }
    pokemon_table[poke_id] = pokemon
    return pokemon


# play the game
def duel():
    player_one = random_poke()
    player_two = random_poke()

    print('Your pokemon is: {}\nId: {}\nHeight: {}\nWeight: {}\nStat: {}\nExperience: {}\n'.format(
        player_one['name'].capitalize(), player_one['id'], player_one['height'],
        player_one['weight'], player_one['stat'], player_one['experience']))

    # reading csv file to let previous round winner choose stat
    with open('poke.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        data = []
        for row in spreadsheet:
            data.append(row)

        prev_one_result = data[0]['result']
        prev_opp_result = data[1]['result']

    if prev_one_result > prev_opp_result or prev_one_result == prev_opp_result:
        stat_choice = input('Which stat do you use(id, height, weight, stat, experience)?\n')
    else:
        stats_opp = ['id', 'height', 'weight', 'stat', 'experience']
        stat_choice = random.choice(stats_opp)
        print('Opponent selected: {}\n'.format(stat_choice.capitalize()))

    stat_one = player_one[stat_choice]
    stat_two = player_two[stat_choice]

    print('Opponent chose pokemon: {}'.format(player_two['name'].capitalize()))
    print('Id: {}\nHeight: {}\nWeight: {}\nStat: {}\nExperience: {}\n'.format(player_two['id'], player_two['height'],
                                                                              player_two['weight'], player_two['stat'],
                                                                              player_two['experience']))

    if stat_one > stat_two:
        print('Hurray! You won this round!🤩\n')
        player_one = 1
        player_two = 0

    elif stat_one < stat_two:
        print('Oh-oh! Try again..😔\n')
        player_one = 0
        player_two = 1
    else:
        print('It\'s a tie!🤝\n')
        player_one = 0
        player_two = 0
    print('Your {}: {}\nOpponent {}: {}\n'.format(stat_choice, stat_one, stat_choice, stat_two))

    # player result
    player_one = {
        'player': 1,
        'stat_score': stat_one,
        'result': player_one
    }
    # opponent result
    player_two = {
        'player': 2,
        'stat_score': stat_two,
        'result': player_two,
    }

    poke_duel = ['player', 'stat_score', 'result']
    rec = [
        player_one,
        player_two
    ]

    # writing csv file
    with open('poke.csv', 'w+') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=poke_duel)
        spreadsheet.writeheader()
        spreadsheet.writerows(rec)

        # for row in rec:
        # print('Player:{} score:{}'.format(row['player'], row['result']))

    # reading csv file
    with open('poke.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        stat_scores = []
        for row in spreadsheet:
            scores = row['stat_score']
            stat_scores.append(scores)
    # high_score = max(stat_scores)
    # print('High score: ', high_score)


duel()

pokemon_data = []
# writing data retrieved from API
with open('pokemon.txt', 'r') as text_file:
    pokemon_data = text_file.read()

pokemon_data = pokemon_data + str(pokemon_table) + ',\n'
with open('pokemon.txt', 'w+') as text_file:
    text_file.write(pokemon_data)
