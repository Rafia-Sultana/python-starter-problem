student_1 = [40, 35, 70, 90, 56]
student_2 = [57, 45, 80, 98, 46]

def check_average(marks):
    failed = False
    for mark in marks:
        if mark < 40:
            print('FAILED')
            failed = True
            break

    if not failed:
         total = sum(marks)
         count = len(marks)
         average = total/count
         print("Average Marks:", average)

print("Student 1:")
check_average(student_1) 

print("Student 2")
check_average(student_2)

