student_data = {'id_1':
    {'name': ['Daquavis'], 'class':['V'], 'subject_integration':['english, math, science']},
'id_2':
    {'name': ['Dream'], 'class':['V'], 'subject_integration':['english, math, science']},
'id_3':
    {'name': ['Technoblade'], 'class':['V'], 'subject_integration':['english, math, science']},
'id_4':
    {'name': ['SmartiePie'], 'class':['V'], 'subject_integration':['english, math, science']}
}
result={}
for key, value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)