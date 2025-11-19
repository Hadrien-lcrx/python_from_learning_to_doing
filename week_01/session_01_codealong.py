# Introduction to Python Syntax - Group 2
# Data types in Python
# Creating a text variable (string)
employee_name = "Michael Scott"
print(f"The employee is {employee_name}")
print(f"The type of the employee_name variable is {type(employee_name)}")

# Creating a whole number variable (integer)
employee_age = 50
print(f"{employee_name} is {employee_age}")
print(f"The type of the employee_age variable is {type(employee_age)}")

# Creating a decimal number variable (float)
employee_salary = 3500.00
print(f"{employee_name} earns ${employee_salary}")
print(f"The type of the employee_salary variable is {type(employee_salary)}")

# Creating True / False values (boolean)
is_branch_director = True
print(f"{employee_name} is a branch director: {is_branch_director}")
print(f"The type of the is_branch_director variable is {type(is_branch_director)}")

# Data structures in Python
# Creating lists in Python
employee_info = [employee_name, employee_salary, employee_age, is_branch_director]
dwight_info = ["Dwight Schrute", 2500.70, 39, False]
print(employee_info)
print(dwight_info)
print(f"{dwight_info[0]} is {dwight_info[2]} years old.")

# Creating tuples in Python
company_info = ("Dunder Mifflin", "Paper distribution", 1949, True)
print(f"{company_info[0]} is in the {company_info[1]} business")

# Trying to change a value in a list
dwight_info[2] = 40
print(dwight_info)

# Trying to change a value in a tuple
company_info_list = list(company_info)
company_info_list[-1] = False
company_info = tuple(company_info_list)

# Creating sets in Python
employee_set = {employee_name, dwight_info[0], "Pam Weasley",
                "Jim Hopper", "Ryan Howard", "Ryan Howard", 89765}
print(employee_set)

# Creating dictionaries in Python
employee_info_dict = {
    "name": employee_name,
    "age": employee_age,
    "salary": employee_salary,
    "is_branch_director": is_branch_director
}

import pprint as pp
pp.pprint(employee_info_dict)

print(f"{employee_info_dict["name"]} is {employee_info_dict["age"]} years old.")
print(list(employee_info_dict.items()))

company_info_dict = {
    "employee_01": employee_info_dict,
    "employee_02": {
        "name": dwight_info[0],
        "age": dwight_info[2],
        "salary": dwight_info[1],
        "is_branch_director": dwight_info[3]
    },
}

pp.pprint(company_info_dict)
print(company_info_dict["employee_02"]["name"])

# Mathematical operators in Python
a = 10
b = 3
print(a + b) # 13
print(a - b) # 7
print(a * b) # 30
print(round(a / b, 2)) # 3.33
print(a // b) # 3
print(a % b) # 1
print(a ** b) # 1000

age = 18
if not age > 17 and age < 19:
    print("Freshly adult")
else:
    print("At least one of the conditions is False")

if 17 < age < 19:
    print("Freshly adult")
else:
    print("At least one of the conditions is False")

c = 10
c += 1 # c = c + 1
print(c)

passed_styleguide = True
passed_pull_request = True

if passed_styleguide == 1 and passed_pull_request == 1:
    print("App ready to deploy")
else:
    print("Some verifications are still required")

# Creating conditions in Python
age = 18
if age < 18:
    print("Minor")
elif age == 18:
    print("Freshly major")
    print("and")
    print("very happy")
    print("and driving a car")
elif age < 20:
    print("Not completely mature yet")
else:
    print("Major")

for key in employee_info_dict.keys():
    print(key.upper())

salary = 2500
while salary < 2600:
    print(f"{salary}€ is not enough! Please give me more.")
    salary += 10
print("Happy with my salary")

i = 0
while i < 10:
    print(i)
    i += 1

for i in range(10, 0, -2): # range(start, end, step)
    print(i)

decimals = []
for i in range(0, 10, 1):
    decimals.append(i / 10)
print(decimals)

import numpy as np
for i in np.arange(0, 1, 0.1):
    print(i)
    if i == 0.4:
        break

employees = list(employee_set)
for employee in employees:
    print(employee)

print(employees)
print(employees[::-1])
print(employee_name[::-1])

# List methods
new_employee = "Kevin Malone"
employees.append(new_employee)
print(employees)

new_employees = ["Andy Bernard", "Robert California", "Oscar Martinez", "Angela Martin"]
employees.append(new_employees)
print(len(employees))
print(employees)
print(employees[-1][0])

employees.extend(new_employees)
print(employees)

employees.insert(2, "Meredith Palmer")

print(employees.count("Ryan Howard"))

employees.remove("Ryan Howard")

#removed = employees.pop(-5)
del employees[-5]
print(employees)
print(f"Index of Michael Scott: {employees.index('Michael Scott')}")
#print(removed)
employees.pop(employees.index(89765))
print(employees)
employees.sort()
print(employees)
employees.sort(reverse=True)
print(employees)
print("THIS IS WHERE WE USE THE KEY")
employees.sort(key=lambda x: x.split(" ")[1])
print(employees)
employees.clear()
print(employees)
del employees


last_name = employee_name.split(" ")[1]
print(last_name)

splitted_name = employee_name[:4]
print(splitted_name)

michael = "Michael Scott of Whatever"
print(michael.split(" ")[1:])
print(employee_name.split(" ")[1:])

completed_order_ids = {"001", "002", "003", "004"}
invoiced_order_ids = {"002", "003", "006"}
completed_order_ids.add("005")
print(completed_order_ids)
completed_order_ids.remove("001")
#completed_order_ids.remove("201") # gives an error
completed_order_ids.discard("201") # doesn't give an error
print(completed_order_ids)
all_orders = completed_order_ids.union(invoiced_order_ids)
print(all_orders)
valid_orders = completed_order_ids.intersection(invoiced_order_ids)
print(valid_orders)
uninvoiced_orders = completed_order_ids.difference(invoiced_order_ids)
print(uninvoiced_orders)
invalid_orders = invoiced_order_ids.difference(completed_order_ids)
print(invalid_orders)
unique_orders = completed_order_ids.symmetric_difference(invoiced_order_ids)
print(unique_orders)
disorganized_commercial_orders = {"005", "006", "007"}
completed_order_ids.update(disorganized_commercial_orders)
print(completed_order_ids)
print(completed_order_ids.issuperset(disorganized_commercial_orders))
print(disorganized_commercial_orders.issubset(completed_order_ids))
print(completed_order_ids.isdisjoint(invoiced_order_ids))

# Dictionary methods
print(employee_info_dict.keys())
keys = ["name", "age", "salary", "status", "is_branch_director"]
for key in keys:
    print(employee_info_dict.get(key, "No key found"))

for k, v in employee_info_dict.items():
    print(f"They key {k} has value {v}")

employee_info_dict.update({
    "city": "Scranton"
})
print(employee_info_dict)
deleted = employee_info_dict.pop("city")
print(employee_info_dict)
print(deleted)
deleted = employee_info_dict.pop("status", None) # raises a key error if no alternate value provided
last_item = employee_info_dict.popitem()
print(last_item)

# Handling errors in Python
# Syntax error
#if x == 5

# Indentation error
#if x == 5:

# Type error
# print(1 + "42")

# Name error
# print(variable_that_doesnt_exit)

# Index error
#print(dwight_info[4])

# Key error
#print(company_info_dict["status"])

# Value error
#employee_new_name = int(employee_name)

# Zero division error
#quotient = 10 / 0

# Attribute error
#for i in range(0, 10, 8):
#    print(i)

try:
    print(employee_info_dict["age"])
except NameError as e:
    print(e)
    variable_that_doesnt_exit = "default value"
except KeyError as e:
    print(e)
    employee_info_dict["status"] = "best boss ever"
except Exception as e:
    print(e)
    # do something else
else:
    print("success")
finally:
    print("operation is over")


print(employee_info_dict)