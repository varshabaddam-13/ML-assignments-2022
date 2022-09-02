weightsInLBS = []
N = int(input("total number of students:"))

for i in range(0, N):
    print("enter weight in lbs for student", (i+1) , ":")
    # the line below takes input from the user
    weight = int(input())
    # adding the user entered weights to weightsInLBS
    weightsInLBS.append(weight)
    print("the weight of student in LBS : ", weightsInLBS)
    # converting each student weight in weightsInLBS from lbs to kilograms
    weightsInKGS = [item/2.205 for item in weightsInLBS]
    print("the weight of students in KGS : ", weightsInKGS)



