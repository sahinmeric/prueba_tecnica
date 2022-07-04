import unittest

from os import remove, listdir, stat
from os.path import exists, isdir

from part_b import get_min_users


class TestPartB(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        try:
            remove('min_users.txt')
        except FileNotFoundError:
            pass
        finally:
            return super().tearDown()

    def test_get_module_users(self):
        """Tests if output file has content"""
        get_min_users()
        hasContent = stat('min_users.txt').st_size > 0
        self.assertTrue(hasContent, True)

    def test_module_users_file(self):
        """Tests if min_users.txt file exists"""
        get_min_users()
        isFileExists = exists('min_users.txt')
        self.assertTrue(isFileExists, True)

    def test_json_dir(self):
        """Tests if json dir exists"""
        isJsonDirExists = isdir('json')
        self.assertTrue(isJsonDirExists, True)

    def test_json_dir_files(self):
        """Tests if json dir contains files"""
        isJsonDirContainsFiles = listdir('json')
        self.assertTrue(isJsonDirContainsFiles, True)

    def test_json_dir_contains_json(self):
        """Tests if files in the json dir are JSON files"""
        substr = '.json'
        for file in listdir('json'):
            isJson = substr in file
            self.assertTrue(isJson, True)


if __name__ == '__main__':
    unittest.main()
