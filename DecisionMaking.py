road_condition = input("Enter Road Condition: ")

if road_condition.lower() == "poor":
    print("Immediate maintenance required.")
elif road_condition.lower() == "fair":
    print("Schedule maintenance soon.")
else:
    print("Road is in good condition.")