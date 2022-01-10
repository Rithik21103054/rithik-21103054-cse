from typing import MutableMapping


SID=int(input("enter your sid"))
NAME=str(input("enter your name"))
GENDER=str(input("enter your gender"))
if(GENDER=='M'):
    GENDER=("male")
if(GENDER=='F'):
    GENDER("female")
if(GENDER=='U'):
    GENDER("unknown")
COURSE_NAME=str(input("enter your course name"))
CGPA=float(input("enter your cgpa"))
STUDENT=[SID,NAME,GENDER,COURSE_NAME,CGPA]
print(STUDENT)

