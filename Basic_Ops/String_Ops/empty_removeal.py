str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print("Original List: \n",str_list)
res_list = [] # result list

for s in str_list:
    if s:
        res_list.append(s)

print("After the removal of None values:")
print(res_list)

print("--------------------------------")
# Solution 2
new_list = list(filter(None,str_list))
print(new_list)
