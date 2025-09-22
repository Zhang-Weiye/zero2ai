import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        full_name = get_formatted_name('king', 'dom')
        self.assertEqual(full_name,'King Dom')

    def test_middle_name(self):
        full_name = get_formatted_name('king', 'dom', 'dom')
        self.assertEqual(full_name, 'King Dom Dom')

unittest.main()