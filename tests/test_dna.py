import sys
from io import StringIO
from unittest import TestCase, mock

from dna.dna import main, populate_database, count_matches


class TestDNA(TestCase):

    @staticmethod
    def get_output_from_main():
        with mock.patch('sys.stdout', new=StringIO()) as fake_output:
            main()
        output = fake_output.getvalue().strip()
        return output

    def test_reading_the_database(self):
        database = populate_database('../databases/small.csv')
        expectation = {
            'AGATC': {
                2: ['Alice'],
                4: ['Bob'],
                3: ['Charlie']
            },
            'AATG': {
                8: ['Alice'],
                1: ['Bob'],
                2: ['Charlie']
            },
            'TATC': {
                3: ['Alice'],
                5: ['Bob', 'Charlie']
            }
        }
        self.assertEqual(expectation, database)

    def test_reading_sequence_1(self):
        expectation = {
            'AGATC': 4,
            'AATG': 1,
            'TATC': 5
        }
        result = count_matches('../sequences/1.txt', ('AGATC', 'AATG', 'TATC'))
        self.assertEqual(expectation, result)

    def test_reading_sequence_2(self):
        expectation = {
            'AGATC': 0,
            'AATG': 1,
            'TATC': 0
        }
        result = count_matches('../sequences/2.txt', ('AGATC', 'AATG', 'TATC'))
        self.assertEqual(expectation, result)

    # def test_output_that_is_hopefully_cleaner(self):
    #     output = self.get_output_from_main()
    #     self.assertEqual('hello', output)
    #
    # def test_everything(self):
    #     command_line_argument = 'Bob'
    #     sys.argv.append(command_line_argument)
    #     output = self.get_output_from_main()
    #     self.assertEqual(command_line_argument, output)

    def test_sequence_1_is_bob(self):
        sys.argv.extend(['../databases/small.csv', '../sequences/1.txt'])
        output = self.get_output_from_main()
        self.assertEqual('Bob', output)

    def test_sequence_2_is_no_match(self):
        sys.argv.extend(['../databases/small.csv', '../sequences/2.txt'])
        output = self.get_output_from_main()
        self.assertEqual('No match', output)

    def test_sequence_3_is_no_match(self):
        sys.argv.extend(['../databases/small.csv', '../sequences/3.txt'])
        output = self.get_output_from_main()
        self.assertEqual('No match', output)

    def test_sequence_4_is_alice(self):
        sys.argv.extend(['../databases/small.csv', '../sequences/4.txt'])
        output = self.get_output_from_main()
        self.assertEqual('Alice', output)

    def test_sequence_5_is_lavender(self):
        sys.argv.extend(['../databases/large.csv', '../sequences/5.txt'])
        output = self.get_output_from_main()
        self.assertEqual('Lavender', output)

    def test_sequence_6_is_luna(self):
        sys.argv.extend(['../databases/large.csv', '../sequences/6.txt'])
        output = self.get_output_from_main()
        self.assertEqual('Luna', output)

    def test_sequence_7_is_ron(self):
        sys.argv.extend(['../databases/large.csv', '../sequences/7.txt'])
        output = self.get_output_from_main()
        self.assertEqual('Ron', output)

    def test_sequence_8_is_ginny(self):
        sys.argv.extend(['../databases/large.csv', '../sequences/8.txt'])
        output = self.get_output_from_main()
        self.assertEqual('Ginny', output)

    def test_sequence_9_is_draco(self):
        sys.argv.extend(['../databases/large.csv', '../sequences/9.txt'])
        output = self.get_output_from_main()
        self.assertEqual('Draco', output)

    def test_sequence_10_is_albus(self):
        sys.argv.extend(['../databases/large.csv', '../sequences/10.txt'])
        output = self.get_output_from_main()
        self.assertEqual('Albus', output)

    def test_sequence_11_is_hermione(self):
        sys.argv.extend(['../databases/large.csv', '../sequences/11.txt'])
        output = self.get_output_from_main()
        self.assertEqual('Hermione', output)

    def test_sequence_12_is_lily(self):
        sys.argv.extend(['../databases/large.csv', '../sequences/12.txt'])
        output = self.get_output_from_main()
        self.assertEqual('Lily', output)

    def test_sequence_13_is_no_match(self):
        sys.argv.extend(['../databases/large.csv', '../sequences/13.txt'])
        output = self.get_output_from_main()
        self.assertEqual('No match', output)

    def test_sequence_14_is_severus(self):
        sys.argv.extend(['../databases/large.csv', '../sequences/14.txt'])
        output = self.get_output_from_main()
        self.assertEqual('Severus', output)

    def test_sequence_15_is_sirius(self):
        sys.argv.extend(['../databases/large.csv', '../sequences/15.txt'])
        output = self.get_output_from_main()
        self.assertEqual('Sirius', output)

    def test_sequence_16_is_no_match(self):
        sys.argv.extend(['../databases/large.csv', '../sequences/16.txt'])
        output = self.get_output_from_main()
        self.assertEqual('No match', output)

    def test_sequence_17_is_harry(self):
        sys.argv.extend(['../databases/large.csv', '../sequences/17.txt'])
        output = self.get_output_from_main()
        self.assertEqual('Harry', output)

    def test_sequence_18_is_no_match(self):
        sys.argv.extend(['../databases/large.csv', '../sequences/18.txt'])
        output = self.get_output_from_main()
        self.assertEqual('No match', output)

    def test_sequence_19_is_fred(self):
        sys.argv.extend(['../databases/large.csv', '../sequences/19.txt'])
        output = self.get_output_from_main()
        self.assertEqual('Fred', output)

    def test_sequence_20_is_no_match(self):
        sys.argv.extend(['../databases/large.csv', '../sequences/20.txt'])
        output = self.get_output_from_main()
        self.assertEqual('No match', output)
