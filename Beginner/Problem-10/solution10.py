data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]

cleaned_data = [item for item in data_list if isinstance(item,int)]

print(cleaned_data)
