test_dict={
'name': 'Serge',
'age': 50,
'profession': 'Sr DevOps Engineer',
'courses': ['aws', 'python', 'docker']
}

for key,value in test_dict.items():
    print(f"{key}: {value}")

for k in test_dict.keys():
    print (k)

print(test_dict.get('courses'))
