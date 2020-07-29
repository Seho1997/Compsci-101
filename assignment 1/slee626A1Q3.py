"""
Name: Se Ho Lee
Username: slee626
Student Id: 890218467
Description: A program which calculates the minimum number
of vehicles required to transport a given number of passengers,
and the cost of transporting that number of passengers.(4 marks)     
"""

passengers_per_shuttle = 20
passengers_per_van = 9
passengers_per_car = 4
passengers_per_motorcycle = 1
price_per_shuttle = 85
price_per_van = 45
price_per_car = 25
price_per_motorcycle = 15

number_of_passengers = int(input("Number of people: "))
print("")

result_title = "You will need:"
border_line = ("=" * 19)
shuttles_outcome_title = (" " * 2 + str("Shuttles:"))
vans_outcome_title = (" " * 2 + str("Vans:"))
cars_outcome_title = (" " * 2 + str("Cars:"))
motorcycles_outcome_title = (" " * 2 + str("Motorcycles:"))
total_title = "Total cost: $"

number_of_shuttles = (number_of_passengers // passengers_per_shuttle)
number_of_vans = ((number_of_passengers - (number_of_shuttles * passengers_per_shuttle)) // passengers_per_van)
number_of_cars = ((number_of_passengers - ((number_of_shuttles * passengers_per_shuttle) + (number_of_vans * passengers_per_van))) // passengers_per_car)
number_of_motorcycles = ((number_of_passengers - (((number_of_shuttles * passengers_per_shuttle) + (number_of_vans * passengers_per_van)) + (number_of_cars * passengers_per_car))) // passengers_per_motorcycle)
total_price = ((number_of_shuttles * price_per_shuttle) + (number_of_vans * price_per_van) + (number_of_cars * price_per_car) + (number_of_motorcycles * price_per_motorcycle))

print(result_title)
print(border_line)
print(shuttles_outcome_title, number_of_shuttles)
print(vans_outcome_title, number_of_vans)
print(cars_outcome_title, number_of_cars)
print(motorcycles_outcome_title, number_of_motorcycles)
print("")
print(total_title, total_price, sep = "")
print(border_line)



