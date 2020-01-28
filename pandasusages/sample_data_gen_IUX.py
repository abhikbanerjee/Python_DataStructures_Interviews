import pandas as pd
import random
from random import randint


suggestion_ids = pd.read_csv("/Users/abhikbanerjee/Desktop_Abhik/suggestion_ids.txt")
rules = pd.read_csv("/Users/abhikbanerjee/Desktop_Abhik/rule_names.txt")
outputpathStr = "/Users/abhikbanerjee/Desktop_Abhik/synthetic_data_IUX.csv"

user_count = 10

recomm_dict ={}
user_count = 10

for user in range(1,user_count+1):
    num = [i for i in range(0,suggestion_ids.shape[0])]
    random.shuffle(num)
    resp_list = []
    for i in num:
        dict_store = {}
        rule_rnd_num = randint(0, rules.shape[0]-1)
#         print(rule_rnd_num)
        dict_store["suggestionId"]=suggestion_ids.iloc[i]["Suggestion_ids"]
        dict_store["rule"]=rules.iloc[rule_rnd_num]["rules"]
        resp_list.append(dict_store)
    user_name_str = "user_"+ str(user)
    recomm_dict[user_name_str] = resp_list

print(recomm_dict)
