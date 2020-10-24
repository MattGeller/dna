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


def count_matches(file_name):
    with open(file_name) as file:
        full_sequence = file.read()
    strs = ('AGATC', 'AATG', 'TATC')

    matches = {}
    for item in strs:
        matches[item] = full_sequence.count(item)
        
    return matches


print('dna.py has been run')
