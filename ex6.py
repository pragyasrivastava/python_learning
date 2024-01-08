# Strings and text

types_of_people = 10 # assigning 10 to a variable types_of_people
x = f"There are {types_of_people} types of people." # print the statement using a f string --> string inside string
binary = "binary" # assigning a string binary to variable binary as well
do_not = "don't" # assigning a string don't to do_not variable
y = f"Those who know {binary} and those who {do_not}." # printing the value --> string inside string

print(x) # printing the value of x
print(y) # printing the value of y 

print(f"I said : {x}") # printing the value of x using f string -->string inside string
print (f"I also said: '{y}'") # printing the value of y using f string  -->string inside string

hilarious = False # assigning variabe to booelan value
joke_evaluation = "Isn't that joke so funny?! {}" # declaring a string with a placeholder {}

print(joke_evaluation.format(hilarious)) # the format function will replace the placeholder in the joke_evaluation string with the value of variable hilarious, then formatted string is printed --> string inside string

w = "This is the left side of ..." # variable with string value
e = "a string with a right side." # variable with string value

print(w+e) # concatenating 2 strings --> merging two strings and printing new string
