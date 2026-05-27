from collections import namedtuple
n=int(input())
# read columns
columns = input().split()
# Create namedtuple
Student=namedtuple('Student',columns)
total=0
for _ in range(n):
    
    data = input().split()
    #Store each student
    student =Student(*data)
    #add Marks
    total +=int(student.MARKS)
#compute average
print(total/n)    
