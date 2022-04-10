

x = [ [5,2,3], [10,8,9] ] 
listHolder = x.pop() # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
print(listHolder)
listHolder[0] = 15
x.append(listHolder)
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
listHolder1 = students.pop(0) # Change the last_name of the first student from 'Jordan' to 'Bryant'
print(listHolder1)
listHolder1["last_name"] = "Bryant"
students.insert(0, listHolder1)
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sportsHolder = sports_directory["soccer"]
print(sportsHolder)
sportsHolder[0] = "Andres"
dictHolder = {"soccer": sportsHolder}
sports_directory.update(dictHolder)
# sports_directory["soccer"] = sportsHolder
print(sports_directory)


# Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
zHolder = z.pop()
zHolder["y"] = 30
z.append(zHolder)
print(z)

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each 
# dictionary in the list and prints each key and the associated value. For example, given the following list:
def dictListPrinter(arr):
    for i in range(len(arr)):
        temp = arr[i]
        print("first_name - " + temp["first_name"] + ", last_name - " + temp["last_name"])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

dictListPrinter(students)

# iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)copy
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - T

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function 
# prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should 
# output:

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        temp = some_list[i]
        print(temp[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key 
# along with the size of its list, and then prints the associated values within each key's list. 

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    keys = some_dict.keys()
    for i in range(len(keys)):
        temp = some_dict[keys[i]]
        print(str(len(temp)) + keys[i].upper())
        temp2 = some_dict[keys[i]]
        for j in range(len(temp2)):
            print(temp2[j])
    #     for i in range(len(some_dict["keys[i]"])):
    #         temp2 
    #         print()

printInfo(dojo)
# output:
# For example:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon