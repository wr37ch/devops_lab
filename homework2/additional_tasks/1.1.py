# You have a record of N students. Each record contains the student's name,
# and their percent marks in Maths, Physics and Chemistry. The marks can be floating values.
# The user enters some integer N followed by the names and marks for N students.
# You are required to save the record in a dictionary data type.
# The user then enters a student's name. Output the average percentage marks obtained by that student,
# correct to two decimal places.


student_marks = {}
count = int(input("Enter the number of students: "))
for x in range(count):
    name, *line = input("Enter the name and marks: ").split()
    scores = list(map(float, line))
    student_marks[name] = scores

student=input("Choose a student: ")
result = (sum(student_marks[student]) / len(student_marks[student]))


print(student_marks)
print("{0:.2f}".format(result))
