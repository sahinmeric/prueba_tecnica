import os
import json


path = "./json/"
auth_m = {'auth_module': {}}  # dict for auth_module
cont_m = {'content_module': {}}  # dict for content_module

for file in os.listdir(path):
    filepath = path + file  # user filepath, './json/u0.json'
    with open(filepath) as f:  # open each json file
        data = json.load(f)  # load json data into dictionary

        auth_mod = data['provider']['auth_module']  # hold 'auth_module' value, 'authn.provider_3'
        cont_mod = data['provider']['content_module']  # hold 'content_module' value, 'authz.provider_4'

        for key, val in auth_m.items():  # search 'auth_mod' value 'authn.provider_3' in 'auth_m' dict
            if auth_mod not in val:  # if 'authn.provider_3' doesn't exist in 'auth_m' dict
                val[auth_mod] = []  # create 'authn.provider_3' key with empty list value
                val[auth_mod].append(filepath)  # add filepath './json/u0.json' to list
            else:  # if 'authn.provider_3' exists in 'auth_m' dict
                val[auth_mod].append(filepath)  # add filepath './json/u0.json' to list

        for key, val in cont_m.items():  # search 'cont_mod' value 'authz.provider_4' in 'cont_m' dict
            if cont_mod not in val:  # if 'authz.provider_4' doesn't exist in 'cont_m' dict
                val[cont_mod] = []  # create 'authz.provider_4' key with empty list value
                val[cont_mod].append(filepath)  # add filepath './json/u0.json' to list
            else:  # if 'authz.provider_4' exists in 'cont_m' dict
                val[cont_mod].append(filepath)  # add filepath './json/u0.json' to list

modules = {**auth_m, **cont_m}  # merge two dictionaries with unpack operator(**)
print(json.dumps(modules, sort_keys=True, indent=2))
