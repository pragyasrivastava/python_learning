formatter = "{} {} {} {}" # declaring a formatter variable with 4 place holders

print(formatter.format(1, 2, 3, 4)) # Assigning the int value 1,2,3,4 using format function to formatter variable
print(formatter.format("one", "two", "three", "four")) # Assigning the string value one,two,three,four using format function to formatter variable
print(formatter.format(True, False, False, True)) # Assigning the boolean value true,false using format function to formatter variable
print(formatter.format (formatter, formatter, formatter, formatter)) # passing formatter variable as argument in the format function
print(formatter.format( 
      "Try your",
      "Own text here",
      "Maybe a poem",
      "Or a song about fear"
)) # Passing the string value using format function to formatter variable
