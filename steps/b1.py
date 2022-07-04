from itertools import combinations


modules = {
    "auth_provider_1": [3, 4, 17, 19],
    "auth_provider_2": [1, 6, 8, 10, 13, 14, 16, 18],
    "auth_provider_3": [0, 7, 11, 12, 15],
    "auth_provider_4": [2, 5, 9],
    "cont_provider_1": [4, 14],
    "cont_provider_2": [8, 9, 13, 15, 16, 17],
    "cont_provider_3": [2, 3, 5, 10, 11, 18],
    "cont_provider_4": [0, 1, 6, 7, 12, 19]
}
module_list = ["auth_provider_1", "auth_provider_2", "auth_provider_3", "auth_provider_4",
               "cont_provider_1", "cont_provider_2", "cont_provider_3", "cont_provider_4"]
user_list = [0, 1, 2, 3, 4, 5, 6, 7, 8,
             9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
req_min_user = 4

comb_user_list = combinations(user_list, req_min_user)
# print(type(module_set))
for user_tuple in comb_user_list:
    # print(userpaths_tuple)
    copy_module_list = module_list.copy()
    # print(copy_module_set)
    min_users = []
    for user_ in user_tuple:
        # print(userpath_)
        for mod, users in modules.items():
            for user in users:
                if user_ == user:
                    # print(f"{user_} --- {user} -- {mod}")
                    try:
                        copy_module_list.remove(mod)
                    except ValueError:
                        continue
                if user_ not in min_users:
                    min_users.append(user_)
                    # print(min_users)
    if not copy_module_list:
        print(min_users)
