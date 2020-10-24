from sys import argv
from csv import reader, DictReader
import os
from collections import defaultdict


def main():
    if len(argv) < 3:
        print('Incorrect number of command-line arguments')
        exit()
    print('No match')

    return True


def populate_database(file_name):
    with open(file_name) as file:
        database = {}
        my_dict_reader = DictReader(file)

        for row in my_dict_reader:
            print(row)
            name = row['name']
            for key, number in row.items():
                if key == 'name':
                    continue
                if key not in database:
                    database[key] = defaultdict(list)
                number = int(number)
                database[key][number].append(name)

        for key, value in database.items():
            database[key] = dict(value)

    return database


print('dna.py has been run')
