import unittest
import json

from os import remove, listdir
from os.path import exists, isdir

from part_a import get_module_users


class TestPartA(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        try:
            remove('module_users.json')
        except FileNotFoundError:
            pass
        finally:
            return super().tearDown()

    def test_get_module_users(self):
        """Tests if get_module_users() returns a dict convertible json"""
        isInstanceofDict = json.loads(get_module_users())
        self.assertTrue(isInstanceofDict, True)

    def test_module_users_file(self):
        """Tests if module_users.json file exists"""
        get_module_users()
        isFileExists = exists('module_users.json')
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

    def test_result_has_all_users(self):
        """Tests if the result file contains all the users"""
        path = "./json/"
        users = []
        module_users_json = "module_users.json"
        module_users = []
        for file in listdir(path):
            users.append(path + file)

        get_module_users()

        with open(module_users_json, 'r') as f:
            data = json.load(f)
            for v in data.values():
                for val in v.values():
                    for user in val:
                        module_users.append(user)
        result = all(elem in module_users for elem in users)
        self.assertTrue(result, True)


if __name__ == '__main__':
    unittest.main()
