def flatten(d, parent_key=''):
    result = {}
   
    for key in d:
        if parent_key == '':
            new_key = key
        else:
            new_key = parent_key + '.' + key
       
        if (type(d[key])) == dict:
            inside = flatten(d[key], new_key)
            result.update(inside)
        else:
            result[new_key] = d[key]
           
    return result
   
data = {"a":{"b":1}, "x":2}
print(f"Flattened JSON : {flatten(data)}")