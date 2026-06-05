name = str(input("Enter the name of employe:"))
salary = int(input("Etner the salary of employe:"))

hra = salary*0.2
da = salary*0.5

gross_salary = salary + hra + da

print(f"Name of employe:{name} \n HRA:{hra} \n DA:{da} \n Gross Salary:{gross_salary}")