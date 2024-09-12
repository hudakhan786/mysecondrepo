file = open("customers.csv", "r")
header = file.readline().strip().split(",")
first_name_index = header.index("FirstName")
last_name_index = header.index("LastName")
country_index = header.index("Country")

data = []
for line in file:
    values = line.strip().split(",")
    data.append([values[first_name_index], values[last_name_index], values[country_index]])

file.close()

file = open("customer_country.csv", "w")
total_employees = len(data)
file.write(f"Total Employees: {total_employees}\n")
file.write("FirstName,LastName,Country\n")
for item in data:
    file.write(f"{item[0]},{item[1]},{item[2]}\n")


file.close()

