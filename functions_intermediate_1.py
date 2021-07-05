# 1
# x = [[5, 2, 3], [10, 8, 9]]

# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]
# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [{'x': 10, 'y': 20}]


# def change(a, b, c, d):
#     a[b][c] = d


# change(x, 1, 0, 15)
# print(x)


# change(students, 0, 'last_name', 'Bryant')
# print(students)


# change(sports_directory, 'soccer', 0, 'Andres')
# print(sports_directory)

# change(z, 0, 'y', 30)
# print(z)


# 2
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]

# def iterateDictionary(var):
#     for x in var:
#         print(x)

# iterateDictionary(students)


# 3
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]


# def iterateDictionary2(key_name, some_list):
#     for x in students:
#         print(x[key_name])


# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)


# 4
# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }


# def printInfo(data):
#     keyring = list(dojo.keys())
#     for x in range(len(data)):
#         print(f'{len(dojo[keyring[x]])} {keyring[x]}')
#         for y in range(len(dojo[keyring[x]])):
#             print(dojo[keyring[x]][y])
#             continue
#         print("")


# printInfo(dojo)
