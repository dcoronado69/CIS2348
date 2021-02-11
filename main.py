service1_cost = 0
service2_cost = 0
print("Davy's auto shop services")
print("Oil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n")
service1 = input("Select first service: \n")
service2 = input("Select second service: ")
if service1 == "Oil change":
    service1_cost = 35
elif service1 == "Tire rotation":
    service1_cost = 19
elif service1 == "Car wash":
    service1_cost = 7
elif service1 == "Car wax":
    service1_cost = 12
elif service1 == "-":
    service1 = "No service"
    service1_cost = 0
if service2 == "Oil change":
    service2_cost = 35
elif service2 == "Tire rotation":
    service2_cost = 19
elif service2 == "Car wash":
    service2_cost = 7
elif service2 == "Car wax":
    service2_cost = 12
elif service2 == "-":
    service2 = "No service"
    service2_cost = 0
print("- - -")
print("Davy's auto shop invoice")
print("Service 1: " + service1 + " costs $" + str(service1_cost))
print("Service 2: " + service2)
print("Total: $" + str(service1_cost + service2_cost))
