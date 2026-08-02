num = int(input("Enter number of students: "))

stu_dict = ["name", "roll", "math", "physics", "chemistry"]
all_student = []

for i in range(num):
    stu_data = {}

    for key in stu_dict:
        value = input(f"Enter {key}: ")

        if key in ["math","physics","chemistry"]:
            value = int(value)
        stu_data[key] = value

    all_student.append(stu_data)

search = input("Enter roll no for details: ")

found = False
for student in all_student:
    if student["roll"] == search:
        average = ((student["math"]+student["physics"]+student["chemistry"])/3)
        print(student)
        print(average)
        found = True
if found == False:
    print("Can't find any details")