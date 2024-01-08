cars = 100 # declaring a variable cars and assigning value 100 to it
space_in_a_car = 4.0 # declaring a variable space_in_a_car where underscore acts as spaces and assigning value 4.0 a float value if we assign 4 it will be an int data type 
drivers = 30 # declaring a variable drivers and assigning value 30 to it
passengers = 90 # # declaring a variable passengers and assigning value 90 to it
cars_not_driven = cars - drivers #declaring a variable cars_not_driven and evaluating it's value based on difference between variables cars - drivers 
cars_driven = drivers # assigning the value of cars_driven into drivers
carpool_capacity = cars_driven * space_in_a_car # declaring a variable carpool_capacity and evaluating it's value based on expression cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven # declaring a variable average_passengers_per_car and evaluating it's value based on expression passengers / cars_driven

print("There are" , cars , "cars_available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We have" , passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
 
