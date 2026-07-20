road_condition = input("Enter Road Condition: ")

if road_condition.lower() == "poor":
    print("Maintenance Priority: HIGH")
    print("Immediate maintenance required.")

elif road_condition.lower() == "fair":
    print("Maintenance Priority: MEDIUM")
    print("Schedule maintenance soon.")
else:
    print("Maintenance Priority: LOW")
    print("Continue routine inspection.")