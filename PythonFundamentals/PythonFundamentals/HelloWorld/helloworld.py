# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello ", name)	# with a comma
print("Hello " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello ", name)	# with a comma
print("Hello " + str(name))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
# print( your code here ) # with .format()
# print( your code here ) # with an f string

# favorite foods
fav1 = "pizza"
fav2 = "biryani" # Indian dish

# 4a format method for string interpolation
print("I love to eat {} and {}." .format(fav1, fav2))

# 4b f method for string interpolation
print(f"I love to eat {fav1} and {fav2}.")