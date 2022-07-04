import os
import json


def main():
    """
    This function reads user json files from the given path,
    creates a dictionary for modules,
    creates a dictionary for each module names,
    creates a list as value for each module name keys,
    appends the user json file path to proper list in proper module names
    """

    path = "./json/"
    provider = 'provider'
    auth_module = 'auth_module'
    content_module = 'content_module'
    modules = {}

    for file in os.listdir(path):
        user_json_filepath = path + file
        with open(user_json_filepath) as f:
            data = json.load(f)
            auth_mod_name = data[provider][auth_module]
            content_mod_name = data[provider][content_module]

            # auth_module operations
            if auth_module not in modules.keys():
                modules[auth_module] = {}
            if auth_mod_name not in modules[auth_module]:
                modules[auth_module][auth_mod_name] = [user_json_filepath]
            else:
                modules[auth_module][auth_mod_name].append(user_json_filepath)

            # content_module operations
            if content_module not in modules.keys():
                modules[content_module] = {}
            if content_mod_name not in modules[content_module]:
                modules[content_module][content_mod_name] = [user_json_filepath]
            else:
                modules[content_module][content_mod_name].append(user_json_filepath)

    print(json.dumps(modules, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
