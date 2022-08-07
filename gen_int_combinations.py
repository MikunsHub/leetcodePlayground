import pandas as pd
const = [37,40] # might be ignored first of all

var1 = [51,52,53,54,55,56,57,58,59]

var2 = [52,53,54,55,56,57,58,59,60,61,62,63,64,65,66]

var3 = [60,61,62,63,64,65,66,67,68]

# [51,52,60]

"""
if i pick 51 my next value must be greater than 51 and that next value has to be greater than the one picked
while I am in the len of var1:
    if choice_var1 == 51:
        pick_from_var2()
            if pick_from_var2() < choice_var1:
                invalid pick
            else:
                pick_from_var3()
                if pick_from_var3() < pick_from_var2:
                invalid pick
"""
"""def pick_from_var(var1[i],len(var2)):
    pass
"""

"""for i in range(len(var1)):
    var1[i] < var2[i] < var3[i]"""



def match_nums(num,num1,var3):
    match_dict = []
    match_dict_str = []
    
    temp1 = None
    temp2 = None
    for i in range(len(var3)):
        if num < num1:
            match_list = [37,40,num,num1]
            match_list_str = []
            if num1 < var3[i]:

                temp = str(37) + str(40) + str(num) + str(num1) + str(var3[i])
                match_list.append(var3[i])
                match_list_str.append(temp)
                
            if len(match_list) > 4:
                # print(len(match_list))
                match_list_temp_str = list(map(str,match_list)    )
                match_list_temp = ''.join(match_list_temp_str)
                match_dict.append(match_list_temp)
                match_dict_str = match_list_str
    return match_dict

dict = []
for i in range(len(var1)):
    for j in range(len(var2)):
        dict.append(match_nums(var1[i],var2[j],var3))


print(len(dict))


df = pd.DataFrame({'combinations': dict})
df.to_csv("new_combinations.csv")




        
