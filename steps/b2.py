import os
import json

from itertools import combinations


def get_min_users():
    path = "./json/"
    provider = "provider"
    auth_module = "auth_module"
    content_module = "content_module"
    req_min_user = 4

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

    comb_userpath_list = combinations(userpath_list, req_min_user)
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
            print(min_users)
            # TODO: append result to a file


def main():
    """ The main function of the script"""
    get_min_users()


if __name__ == "__main__":
    main()
