import csv

with open("EmployeePay.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    first_name_index = header.index("EmpFName")
    last_name_index = header.index("EmpLName")
    salary_index = header.index("Salary")
    bonus_index = header.index("Bonus")

    data = []
    for values in reader:
        data.append([values[first_name_index], values[last_name_index], values[salary_index],values[bonus_index]])
print("First Name", "Last Name", "Salary","Bonus", sep="  ")
for row in data:
    print(*row, sep="      ")
file.close()
