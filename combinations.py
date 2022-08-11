import pandas as pd
var1 = [item for item in range(41,60)]
var2 = [item for item in range(45,68)]
var3 = [item for item in range(53,70)]

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

print(dict[0])
print(len(dict))

df = pd.DataFrame({'combinations': dict})
df.to_csv("combinations.csv")