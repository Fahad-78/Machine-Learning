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

def average(student):
    return (student["math"] + student["physics"] + student["chemistry"]) / 3

search = input("\nEnter roll no for details: ")

found = False
for student in all_student:
    if student["roll"] == search:
        print("\nname:", student["name"])
        print("roll:", student["roll"])
        avg = average(student)
        print("Average:", avg)
        found = True
if found == False:
    print("Can't find any details")