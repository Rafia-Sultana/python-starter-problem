dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}
dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}

common_keys = set(dict1.keys()) & set(dict2.keys())

for key in common_keys:
    print(f"{key}: dict1 -> {dict1[key]}, dict2 -> {dict2[key]}")
