robiul = {
    'name' : 'Robiul',
    'age' : 24,
    'university' : 'New York University'
}
robiul['university'] = 'NPI University'

# print(robiul.keys())
# print(robiul.values())

# for i in robiul.keys():
#     print(robiul[i])

# for i in robiul.items():
#     print(i)

#convert list

# x = list(robiul.keys())
# print(x)
# y = list(robiul.values())
# print(y)

#print key, value handy trick

# for k,v in robiul.items():
#     print(f'Key : {k} Value : {v}')

#check if key is present in dict

# print('name' in robiul)
# print('name' in robiul.keys())
# print('Robiul' in robiul.values())

#get method

# print(str(robiul.get('name', 'Robiul')))
# print(str(robiul.get('height', '5.4"')))

#setdefault
print(robiul.setdefault('name', 'Robiul'))
print(robiul.setdefault('height', '5.4"'))
print(robiul)