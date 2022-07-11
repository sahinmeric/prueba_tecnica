"""This script reads all the user JSON files in the given path and
dumps a JSON file that contains modules with the list of users who use each module.

Each JSON file contains the modules that the user uses and has the following structure:
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

The exported file will have the following structure.
e.g:
    {
        "auth_module": {
            "authn.provider_1": ["./json/u0.json", "./json/u1.json"],
            "authn.provider_2": ["./json/u3.json", "./json/u6.json"],
            "authn.provider_3": ["./json/u7.json", "./json/u5.json"],
            "authn.provider_4": ["./json/u4.json", "./json/u2.json"]
        },
        "content_module": {
            "authz.provider_1": ["./json/u4.json", "./json/u1.json"],
            "authz.provider_2": ["./json/u5.json", "./json/u3.json"],
            "authz.provider_3": ["./json/u0.json", "./json/u2.json"],
            "authz.provider_4": ["./json/u6.json", "./json/u7.json"]
        }
    }

This file can also be imported as a module and contains the following
functions:

    * get_module_users - reads user JSON files and creates a module user JSON file
    * main - the main function of the script
"""

import os
import json


def get_module_users():
    """
    This function reads user JSON files from the given path,
    creates a dictionary from modules,
    creates a list of users (user file paths) that use each module,
    dumps modules dictionary as a JSON file
    """

    path = "./json/"
    provider = 'provider'
    auth_module = 'auth_module'
    content_module = 'content_module'
    module_users_json = 'module_users.json'
    modules = {}

    for file in os.listdir(path):
        user_json_filepath = path + file
        with open(user_json_filepath) as f:
            data = json.load(f)
            auth_mod_name = data[provider][auth_module]
            content_mod_name = data[provider][content_module]

            if auth_module not in modules.keys():
                modules[auth_module] = {}
            if auth_mod_name not in modules[auth_module]:
                modules[auth_module][auth_mod_name] = [user_json_filepath]
            else:
                modules[auth_module][auth_mod_name].append(user_json_filepath)

            if content_module not in modules.keys():
                modules[content_module] = {}
            if content_mod_name not in modules[content_module]:
                modules[content_module][content_mod_name] = [user_json_filepath]
            else:
                modules[content_module][content_mod_name].append(user_json_filepath)

    module_users = json.dumps(modules, sort_keys=True, indent=2)
    with open(module_users_json, 'w') as f:
        f.write(module_users)
        # print(f"{module_users_json} file created.")
    return module_users


def main():
    """ the main function of the script"""
    get_module_users()


if __name__ == "__main__":
    main()
