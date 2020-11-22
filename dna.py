import re
from collections import defaultdict
from csv import DictReader
from sys import argv


def main():
    if len(argv) < 3:
        print('Incorrect number of command-line arguments')
        exit()

    database = populate_database(argv[1])
    matches = count_matches(argv[2], tuple(database))

    suspects = []

    for sequence, number in matches.items():
        if number in database[sequence]:
            list_of_local_suspects = database[sequence][number]
            if not suspects:
                suspects = list_of_local_suspects
            else:
                suspects = list(set(suspects) & set(list_of_local_suspects))
        else:
            print('No match')
            return False

    if len(suspects) == 1:
        print(suspects[0])
    else:
        print('No match')

    return True


def populate_database(file_name):
    with open(file_name) as file:
        database = {}
        my_dict_reader = DictReader(file)

        for row in my_dict_reader:
            name = row['name']
            for sequence, number in row.items():
                if sequence == 'name':
                    continue
                if sequence not in database:
                    database[sequence] = defaultdict(list)
                number = int(number)
                database[sequence][number].append(name)

        for key, value in database.items():
            database[key] = dict(value)

    return database


def count_matches(file_name, strs):
    with open(file_name) as file:
        full_sequence = file.read()

    matches = {}
    for item in strs:
        pattern = f'(?:{item})+'
        result = re.findall(pattern, full_sequence)

        result = list(map(len, result))

        if not result:
            matches[item] = 0

        else:
            number_of_repetitions = max(result) / len(item)

            matches[item] = number_of_repetitions

    return matches