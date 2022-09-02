
#given list
ages=[19,22,19,24,20,25,26,24,25,24]

#sorting by using sort method
ages.sort()
print("Sorted List : ",end='')
print(ages)

#finding min and max value
min_value=ages[0]
max_value=ages[-1]
print("Min value is : "+str(min_value))
print("Max value is : "+str(max_value))

#adding min and max values to list
ages.append(min_value)
ages.append(max_value)
print("Modified list : ",end='')
print(ages)

#finding the median age
if len(ages)%2!=0:
    median=ages[len(ages)//2]
else:
    median=(ages[len(ages)//2]+ages[(len(ages)//2)-1])/2
print("Median is : "+str(median))

#finding average age
average_age=sum(ages)//len(ages)
print("Average age is : "+str(average_age))

#finding range of ages
range_of_age=max(ages)-min(ages)
print("Range of ages is : "+str(range_of_age))
