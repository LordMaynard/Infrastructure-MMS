road_score = int(input("Enter road condition score (0-100): "))

if road_score >= 90:
    print("Condition: Excellent")
    print("Recommendtion: Routine Monitoring")
elif road_score >= 70:
    print("Condition: Average")
    print("Recommendation: Minor Maintenance")
elif road_score >= 50:
    print("Condition: Fair")
    print("Recommendation: Schedule Maintenance")
elif road_score >= 30:
    print("Condition: Poor")
    print ("Recommendation: Immediate maintenance")
elif road_score >= 0:
    print("Condition: Critical")
    print("Recommendation: Emergency Rehabilitation")
else:
    print("Invalid Score")