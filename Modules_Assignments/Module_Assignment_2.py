# 1. Hospital Management System  
#    - Create a system to manage patient and doctor information.  
#    - Tasks:  
#      1. Store patient and doctor details (e.g., name, ID, department) using appropriate data structures.  
#      2. Implement a feature to assign patients to doctors based on their department.  
#      3. Use loops to display all patients under a specific doctor.  
#      4. Handle exceptions for invalid department inputs or non-existent doctors.  
#      5. Create modules for patient registration, doctor assignment, and report generation.  
import Patient
import Doctor

#      1. Store patient and doctor details (e.g., name, ID, department) using appropriate data structures. 
doctors = {
    "Dr. John Smith": "Cardiology",'patient':[],
    "Dr. Emily Davis": "Neurology",'patient':[],
    "Dr. Michael Brown": "Orthopedics",'patient':[],
    "Dr. Sarah Wilson": "Pediatrics",'patient':[],
    "Dr. James Taylor": "Dermatology",'patient':[]
}
patients={}
print("""Welcome To Lavanya Hospital 
    1.PaitentResistration
    2.Display Patitens under Doctor
    3.Exit
""")
Id=0
ch=int(input("enter choice "))
while(ch!=3):
    if ch==1:
        
        Patient.patient_register(patients,doctors)
        Doctor.doctor_assignment(patients)
    elif ch==3:
        Doctor.diplay_doctor(doctors)
    ch=int(input("Enter your Choice "))



# 2. E-Commerce Order Management System  
#    - Develop a system to manage orders for an online store.  
#    - Tasks:  
#      1. Maintain product details (e.g., name, price, and stock) using dictionaries or lists.  
#      2. Allow customers to add items to a cart and calculate the total cost.  
#      3. Use conditions to check stock availability before adding items to the cart.  
#      4. Handle exceptions for invalid product selections or insufficient stock.  
#      5. Implement a module to manage checkout and generate a bill.  

# 3. Quiz Management System  
#    - Build a system to conduct a quiz with multiple-choice questions.  
#    - Tasks:  
#      1. Store questions, options, and correct answers using a list of dictionaries.  
#      2. Use loops to ask all questions and record answers from the user.  
#      3. Use conditions to calculate the score based on correct answers.  
#      4. Handle exceptions for invalid option selections.  
#      5. Organize the quiz into modules for question management, scoring, and result display.  

# 4. Employee Payroll System  
#    - Design a system to calculate employee salaries.  
#    - Tasks:  
#      1. Store employee details (e.g., name, ID, basic salary) using appropriate data types.  
#      2. Calculate the gross salary by adding allowances and deducting taxes using conditional statements.  
#      3. Use loops to process salary calculations for multiple employees.  
#      4. Handle exceptions for invalid salary inputs or deductions.  
#      5. Create separate modules for salary calculation, employee data management, and reports.  

# 5. Travel Booking System  
#    - Create a system to manage travel bookings.  
#    - Tasks:  
#      1. Maintain a list of destinations with available packages and costs.  
#      2. Allow users to book travel packages by selecting a destination and number of travelers.  
#      3. Use conditional statements to apply discounts for group bookings.  
#      4. Handle exceptions for invalid destination choices or traveler numbers.  
#      5. Implement a module to manage bookings and generate invoices.  