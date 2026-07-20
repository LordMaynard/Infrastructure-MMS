print("=" * 60)
print("ROAD INSPECTION REPORT")
print("=" * 60)

Road_ID = int(input("Enter road id: "))
Road_Name = (input("Enter road name: "))
Location = (input("Enter road location: "))
Length = float(input("Enter road length: "))
Width = float(input("Enter road width: "))
Inspector_Name = (input("Enter Inspector Name: "))
Condition_Score = int(input("Enter condition score (0-100): "))
Estimated_Maintenance_Cost = int(input("Enter estimated maintenance cost: "))

if Condition_Score >= 90:
    print("Road Classification: Excellent")
    print("Recommended Maintenance: Routine Monitoring")
elif Condition_Score >= 70:
    print("Road Classification: Excellent")
