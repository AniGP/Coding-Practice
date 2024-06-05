# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

num_students=int(input())
Students=namedtuple('Students',input().split())

total_marks=0

for i in range(num_students):
    
    student_input=input().split()    
    student=Students(*student_input)    
    total_marks+=int(student.MARKS)
    
avg=total_marks/num_students

print(avg)