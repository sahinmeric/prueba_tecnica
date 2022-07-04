import os
import json


path = "./json/"
provider = 'provider'
auth_module = 'auth_module'
content_module = 'content_module'
modules = {}  # create empty dict for auth and content modules

for file in os.listdir(path):
    user_json_filepath = path + file
    with open(user_json_filepath) as f:
        data = json.load(f)
        auth_module_name = data[provider][auth_module]
        content_module_name = data[provider][content_module]

        if auth_module not in modules.keys():  # if 'auth_module' doesn't exist in 'modules' keys
            modules[auth_module] = {}  # create 'auth_module' key with empty dictionary value in 'modules' dict
        if auth_module_name not in modules[auth_module]:  # if 'auth_module_name' doesn't exist in 'auth_module' dict
            modules[auth_module][auth_module_name] = []  # create 'auth_module_name' key with empty list value
            modules[auth_module][auth_module_name].append(user_json_filepath)  # append 'user_json_filepath' to 'auth_module_name' list
        else:  # if 'auth_module' exists in 'modules' keys
            modules[auth_module][auth_module_name].append(user_json_filepath)  # append 'user_json_filepath' to 'auth_module_name' list

        if content_module not in modules.keys():  # if 'content_module' doesn't exist in 'modules' keys
            modules[content_module] = {}  # create 'content_module' key with empty dictionary value in 'modules' dict
        if content_module_name not in modules[content_module]:  # if 'content_module_name' doesn't exist in 'content_module' dict
            modules[content_module][content_module_name] = []  # create 'content_module_name' key with empty list value
            modules[content_module][content_module_name].append(user_json_filepath)  # append 'user_json_filepath' to 'content_module_name' list
        else:  # if 'content_module' exists in 'modules' keys
            modules[content_module][content_module_name].append(user_json_filepath)  # append 'user_json_filepath' to 'content_module_name' list

print(json.dumps(modules, sort_keys=True, indent=2))
