from io import StringIO
from unittest import TestCase, mock

from dna.dna import main


class TestDNA(TestCase):

    @staticmethod
    def get_output_from_main():
        with mock.patch('sys.stdout', new=StringIO()) as fake_output:
            main()
        output = fake_output.getvalue().strip()
        return output

    def test_output_that_is_hopefully_cleaner(self):
        output = self.get_output_from_main()
        self.assertEqual('hello', output)