# Dictionary-Assignment
#  1. Access the Name and Position of Employee with ID 103.
# Given the employee dictionary: # Task: Retrieve the name and position of the employee with ID 103.
# employees = {
#     101: {"name": "John Doe", "position": "Software Engineer", "salary": 80000},
#     102: {"name": "Jane Smith", "position": "Product Manager", "salary": 95000},
#     103: {"name": "Sam Brown", "position": "Data Scientist", "salary": 90000}
# }
# print(employees[103]['name'],employees[103]['position'])



#  2. Check if an Employee with ID 106 Exists. If Not, Print "Employee not found."
#  Given dictionary
# employees = {
#     101: {"name": "John Doe", "position": "Software Engineer", "salary": 80000},
#     102: {"name": "Jane Smith", "position": "Product Manager", "salary": 95000},
#     103: {"name": "Sam Brown", "position": "Data Scientist", "salary": 90000}
# }

# if employees.get(106)==None:
#     print("Employee not found")


#  3. Update the Salary of Employee 101 to 85000.

# Task: Update the salary of employee 101 to 85000.
#  Given dictionary
# employees = {
#     101: {"name": "John Doe", "position": "Software Engineer", "salary": 80000},
#     102: {"name": "Jane Smith", "position": "Product Manager", "salary": 95000},
#     103: {"name": "Sam Brown", "position": "Data Scientist", "salary": 90000}
# }
# employees[101]['salary']=85000
# print(employees[101])


#  4. Add a New Employee with ID 106. The Employee Has the Name "Lisa Green", Position "UX Designer", and Salary 78000.
#  Given dictionary
# employees = {
#     101: {"name": "John Doe", "position": "Software Engineer", "salary": 80000},
#     102: {"name": "Jane Smith", "position": "Product Manager", "salary": 95000},
#     103: {"name": "Sam Brown", "position": "Data Scientist", "salary": 90000}
# }
# employees[106]={'name':"Lisa Green","Position":"UX Designer","Salary":78000}
# print(employees[106])













#  5. Remove Employee 104 from the Employee Data.

# #  Given dictionary
# employees = {
#     101: {"name": "John Doe", "position": "Software Engineer", "salary": 80000},
#     102: {"name": "Jane Smith", "position": "Product Manager", "salary": 95000},
#     103: {"name": "Sam Brown", "position": "Data Scientist", "salary": 90000}
# }
# employees.pop(104)

# print(employees)




#  6. Retrieve All the Names of Employees Using keys().

#  Given dictionary
# employees = {
#     101: {"name": "John Doe", "position": "Software Engineer", "salary": 80000},
#     102: {"name": "Jane Smith", "position": "Product Manager", "salary": 95000},
#     103: {"name": "Sam Brown", "position": "Data Scientist", "salary": 90000}
# }
# print(employees.keys())




#  7. Get All the Positions of Employees Using values().

#  Given dictionary
# employees = {
#     101: {"name": "John Doe", "position": "Software Engineer", "salary": 80000},
#     102: {"name": "Jane Smith", "position": "Product Manager", "salary": 95000},
#     103: {"name": "Sam Brown", "position": "Data Scientist", "salary": 90000}
# }
# print(employees.values())







#  8. List All Employee ID and Name Pairs Using items().

#  Given dictionary
# employees = {
#     101: {"name": "John Doe", "position": "Software Engineer", "salary": 80000},
#     102: {"name": "Jane Smith", "position": "Product Manager", "salary": 95000},
#     103: {"name": "Sam Brown", "position": "Data Scientist", "salary": 90000}
# }
# print(employees.items())


#  9. Find the Highest Salary Among All Employees and Print It.

#  Given dictionary
# employees = {
#     101: {"name": "John Doe", "position": "Software Engineer", "salary": 80000},
#     102: {"name": "Jane Smith", "position": "Product Manager", "salary": 95000},
#     103: {"name": "Sam Brown", "position": "Data Scientist", "salary": 90000}
# }
# if employees[101]['salary']>employees[102]['salary']:
#     if employees[101]['salary']>employees[103]['salary']:
#         print(employees[101]['salary'])
#     else:
#         print(employees[103]['salary'])
# else:
#     if employees[102]['salary']>employees[103]['salary']:
#         print(employees[102]['salary'])
#     else:
#         print(employees[103]['salary'])


#  10. Check if Any Employee Has a Position "Software Engineer". If So, Print Their Name.

#  Given dictionary
# employees = {
#     101: {"name": "John Doe", "position": "Software Engineer", "salary": 80000},
#     102: {"name": "Jane Smith", "position": "Product Manager", "salary": 95000},
#     103: {"name": "Sam Brown", "position": "Data Scientist", "salary": 90000}
# }

# if employees[101]['position']=="Software Engineer":
#     print(employees[101]['name'])
# elif employees[102]['position']=="Software Engineer":
#     print(employees[102]['name'])
# elif employees[103]['position']=="Software Engineer":
#     print(employees[103]['name'])






















#  11. Using if elif else, Print a Message About an Employee's Salary Range:
# - If salary is more than 90,000, print "High Salary."
# - If salary is between 75,000 and 90,000, print "Medium Salary."
# - If salary is less than 75,000, print "Low Salary."
# Task: For each employee, use if elif else to print the salary range.
#  Given dictionary
# employees = {
#     101: {"name": "John Doe", "position": "Software Engineer", "salary": 80000},
#     102: {"name": "Jane Smith", "position": "Product Manager", "salary": 95000},
#     103: {"name": "Sam Brown", "position": "Data Scientist", "salary": 90000}
# }
# if employees[101]['salary']>90000:
#     print(employees[101]['name'], 'Higher Salary')
# elif employees[101]['salary']>75000 and employees[101]['salary']<=90000:
#      print(employees[101]['name'], 'Medium Salary')
# elif employees[101]['salary']<75000:
#     print(employees[101]['name'], 'Low Salary')

# if employees[102]['salary']>90000:
#     print(employees[102]['name'], 'Higher Salary')
# elif employees[102]['salary']>75000 and employees[102]['salary']<=90000:
#      print(employees[102]['name'], 'Medium Salary')
# elif employees[102]['salary']<75000:
#     print(employees[102]['name'], 'Low Salary')

# if employees[103]['salary']>90000:
#     print(employees[103]['name'], 'Higher Salary')
# elif employees[103]['salary']>75000 and employees[103]['salary']<=90000:
#      print(employees[103]['name'], 'Medium Salary')
# elif employees[103]['salary']<75000:
#     print(employees[103]['name'], 'Low Salary')


#  12. Slice the Employee Dictionary to Retrieve the First 3 Employees.

#  Given dictionary
employees = {
    101: {"name": "John Doe", "position": "Software Engineer", "salary": 80000},
    102: {"name": "Jane Smith", "position": "Product Manager", "salary": 95000},
    103: {"name": "Sam Brown", "position": "Data Scientist", "salary": 90000},
    104: {"name": "Emily White", "position": "HR Manager", "salary": 75000},
    105: {"name": "David Clark", "position": "Marketing Director", "salary": 105000}
}
print(employees[101],employees[102],employees[103])

# Task: Slice the dictionary to get the first 3 employees based on their employee IDs.
