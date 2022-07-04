"""This script reads all the user JSON files in the given path
and outputs the list of minimum users to test all existing modules.

Each JSON file contains the modules that the user uses
and has the following structure:
e.g:
    path: ./json
    filename: u0.json
    filepath: ./json/u0.json
    structure:

    {
        "name": "User 0",
        "provider": {
            "content_module": "authz.provider_3",
            "auth_module": "authn.provider_1"
        }
    }

example output:
    ['./json/u1.json', './json/u15.json', './json/u4.json', './json/u5.json']
    ['./json/u10.json', './json/u12.json', './json/u4.json', './json/u9.json']
    ['./json/u10.json', './json/u4.json', './json/u7.json', './json/u9.json']

This file can also be imported as a module and contains the following
functions:

    * get_min_users - reads user JSON files and outputs the list of minimum users needed to test all modules
    * main - the main function of the script
"""

import os
import json

from itertools import combinations


def get_min_users():
    """
    This function reads user JSON files from the given path,
    creates a user module dictionary that contains all the users
    and the set of modules each user uses,
    creates a set of modules from unique module names,
    creates a list of users (user file paths),
    creates an iterable from combinations of the list of users,
    iterates each user combination over user modules,
    creates a copy of the module set,
    creates an empty list for minimum users,
    finds what modules uses each user
    and removes that module from the copy of the module set,
    and adds the user to the list of minimum users
    after each user combination iterates over
    checks if the copy of the module set is empty,
    if it is empty adds the list of user combination to the output file
    if not iterates the next user combination.
    """

    path = "./json/"
    provider = "provider"
    auth_module = "auth_module"
    content_module = "content_module"
    min_users_file_name = 'min_users.txt'

    user_modules = dict()
    module_set = set()
    userpath_list = list()

    for file in os.listdir(path):
        userpath = path + file
        with open(userpath) as f:
            data = json.load(f)

            auth_mod = data[provider][auth_module]
            cont_mod = data[provider][content_module]

            user_modules[userpath] = set()
            user_modules[userpath].add(auth_mod)
            user_modules[userpath].add(cont_mod)

            if auth_mod not in module_set:
                module_set.add(auth_mod)
            if cont_mod not in module_set:
                module_set.add(cont_mod)
            if userpath not in userpath_list:
                userpath_list.append(userpath)

    req_min_user = 0
    for i in range(req_min_user, len(userpath_list)):
        comb_userpath_list = combinations(userpath_list, req_min_user)
        try:
            os.remove(min_users_file_name)
        except FileNotFoundError:
            pass
        finally:
            for userpaths_tuple in comb_userpath_list:
                copy_module_set = module_set.copy()
                min_users = []
                for userpath_ in userpaths_tuple:
                    for key in user_modules.keys():
                        if userpath_ == key:
                            copy_module_set.difference_update(user_modules[key])
                        if userpath_ not in min_users:
                            min_users.append(userpath_)
                if not copy_module_set:
                    with open(min_users_file_name, 'a') as file:
                        file.write(str(min_users))
                        file.write('\n')

            if os.path.exists(min_users_file_name):
                print(f"Minimum user list found for required minimum users = {req_min_user} and {min_users_file_name} file created.")
                break  # TODO: Return list of lists?
            else:
                # print(f"No user list found for required minimum users = {req_min_user}")
                req_min_user += 1


def main():
    """ The main function of the script"""
    get_min_users()


if __name__ == "__main__":
    main()
