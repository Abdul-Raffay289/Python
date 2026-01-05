test_dic = {
    'Codingal': 2,
    'is' : 2,
    'best': 2,
    'for' : 2,
    'Coding' : 1,
}
print("original_dictionary is " +str(test_dic))
K=1
res = 0
for key in test_dic:
    if test_dic[key]==1:
        res = res +1
print("2 key Values are", res)