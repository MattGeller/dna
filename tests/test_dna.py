import contextlib
from io import StringIO
from unittest import TestCase
import sys

from dna.dna import main


class TestDNA(TestCase):
    # def setUp(self) -> None:
    #     self.temp_stdout = StringIO()
    #     contextlib.redirect_stdout(self.temp_stdout)

    # def getOutput(self):
    #     return self.temp_stdout.getvalue().strip()

    def test_output(self):
        temp_stdout = StringIO()
        contextlib.redirect_stdout(temp_stdout)
        main()
        output = temp_stdout.getvalue().strip()
        self.assertEqual('hello', output)

    def test_output_preserve(self):
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            main()
        output = temp_stdout.getvalue().strip()
        self.assertEqual('hello', output)

    def test_the_test(self):
        command_line_argument = 'this is a command line argument'
        sys.argv.append(command_line_argument)

        main()

        print('here is the output:')
        print(self.getOutput())
        self.assertTrue(True)

    def test_main(self):
        temp_stdout = StringIO()

        with contextlib.redirect_stdout(temp_stdout):
            main()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, 'Hello, world!')
