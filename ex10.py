# escaping single and double quotes in python

# "I "understand" joe." -->this creates confusion as where the double quotes starts and ends , inorder to avoid this confusion we using escaping of double and single quotes

height = "I am 6'2\" tall."  #escaped 2" by adding a backlash
my_height = 'I am 6\'2" tall.' #escaped 6' by adding a backlash

print(height)
print(my_height)

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)
