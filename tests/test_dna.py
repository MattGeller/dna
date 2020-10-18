import contextlib
from io import StringIO
from unittest import TestCase

from dna.dna import main


class TestDNA(TestCase):
    def test_main(self):
        temp_stdout = StringIO()

        with contextlib.redirect_stdout(temp_stdout):
            main()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, 'Hello, world!')
