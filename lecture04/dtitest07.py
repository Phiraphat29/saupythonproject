emp_id = input("Insert Employee ID: ")
emp_name = input("Employee Name: ")
emp_salary = float(input("Salary: "))

tax_minus = emp_salary - (emp_salary * 7 / 100) - 500
tax_minus_lowerfloat = "%.2f" % tax_minus

print(f"ID {emp_id} Mr/Miss {emp_name} Your salary is {tax_minus_lowerfloat}")