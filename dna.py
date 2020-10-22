from sys import argv
from csv import reader, DictReader
import os


def main():
    if len(argv) < 3:
        print('Incorrect number of command-line arguments')
        exit()
    print('No match')

    return True


def populate_database(file_name):
    with open(file_name) as file:

        my_dict_reader = DictReader(file)
        print('dict reader:')
        for row in my_dict_reader:
            print(row)

        database = {}

    return database


print('dna.py has been run')
