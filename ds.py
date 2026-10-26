import os
import keyword

print(keyword.kwlist)
#list
course=["Linux","AWS","Python","Docker","Kubernetes"]


#dictionary key value pair

my_info={
"name":"Arun",
"age":30,
"course":"Python",
"native":"India"
}

my_info.update({"course":course})
print(my_info)

#sets does not  allow duplicate values and it is unordered
my_set={1,2,3,4,5,5,5,5,5,5,5,}
print(my_set)
my_set1={1,2,3,4,5,6,7,8,9}
print(my_set1.union(my_set))
print(my_set1.intersection(my_set))
#tuple is immutable and ordered
days_of_week=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print(days_of_week) 