#question 4

student_1_marks=int(input("marks of student_1  "))
student_2_marks=int(input("marks of student_2  "))
student_3_marks=int(input("marks of student_3  "))
student_4_marks=int(input("marks of student_4  "))
student_5_marks=int(input("marks of student_5  "))

marks_list=[student_1_marks,student_2_marks,student_3_marks,student_4_marks,student_5_marks]

print("list :")
print(marks_list)
print("sorted list(decreasing order)")
marks_list.sort(reverse=True)
print(marks_list)

