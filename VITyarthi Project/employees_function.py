import json
import os
from data import employees , Salary , Bonus , admin_password

def net_pay():
    return(Salary + Bonus)

def create_id(name , department):
    count = len(employees["Id"]) + 1
    return name.lower().split()[0] + department[:3].lower() + str(count)

def register_employees():
    while True:
     name = input("Enter Your Name : ").upper()
     if name != "":
        break
     else :
        continue
    
    while True:
     department =  input("Choose One Of These . \n 1.Sales \n 2.Management \n 3.Advertisment \n Enter Your Department : ").lower()
     if department in ["sales" , "management" , "advertisment"]:
        break
     else :
        continue
    password = input("Enter Your Password : ")
    new_id = create_id(name , department)

    employees["Id"].append(new_id)
    employees["Name"].append(name)
    employees["Department"].append(department)
    employees["Salary"].append(net_pay())
    employees["Password"].append(password)
    save_data()

def list_employees():
   for i in range(len(employees["Id"])):
      print([i+1])
      print("Name :" , employees["Name"][i])
      print("ID :" , employees["Id"][i])
      print("Department :" , employees["Department"][i])
      print("Salary :" , employees["Salary"][i])
      print()

def find_employees(emp_id):
   for i in range(len(employees["Id"])):
      if employees["Id"][i] == emp_id :
         return i
   return -1

def show_employees(emp_id):
   i = find_employees(emp_id)
   if i == -1:
      print("Employee Not Found")
   else:
      print("Name :" , employees["Name"][i])
      print("ID :" , employees["Id"][i])
      print("Department :" , employees["Department"][i])
      print("Salary :" , employees["Salary"][i])

def delete_employees(emp_id , current_user):
   i = find_employees(emp_id)
   if i == -1:
      print("Employee Not Found")
      return
   if current_user != "admin" and current_user != emp_id:
         print("You Can Only Change Your Own")
         return
   employees["Id"].pop(i)
   employees["Name"].pop(i)
   employees["Department"].pop(i)
   employees["Salary"].pop(i)
   save_data()
   print("Employee Deleted ")

def update_employees(emp_id , current_user):
   i = find_employees(emp_id)
   if i == -1:
      return ("Employee Not Found ")
   if current_user != "admin" and current_user != emp_id:
      print("You Can Only Change Your Own")
      return
   a = input("Choose What You Want To Update \n 1.Name \n 2.Department \n 3.Password \n 4.Salary(Admin Only)").lower()
   if a == "name":
      employees["Name"][i] = input("Enter Your New Name :  ")
   elif a == "department":
      employees["Department"][i] = input("Enter Your New Department :  ")
   elif a == "password":
      employees["Password"][i] = input("Enter Your New Password : ")
   elif a == "salary":
      if current_user == "admin":
         employees["Salary"][i] = float(input("Enter New Salary : "))
      else:
         print("You Are Not Admin")
   save_data()

def login():
  while True: 
   emp_id = input("Enter Your Employee ID : ")
   if emp_id == "admin":
      if input("Password : ") == admin_password:
       print("Welcome Admin")
       return "admin" 
      else:
       print("Incorrect Password")
       continue
   i = find_employees(emp_id)
   if i == -1:
      print("Employee Not Found ")
      continue
   elif input("Password : ") == employees["Password"][i]:
      print("Welcome" , employees["Name"][i])
      return emp_id
   else:
      print("Incorrect Password")
      continue

def payroll():
   total = 0
   for i in range (len(employees["Salary"])):
      total = total + employees["Salary"][i]
   return total

def department_total():
   total={}
   for i in range (len(employees["Department"])):
     depart = employees["Department"][i]
     salary = employees["Salary"][i]
     if depart in total:
        total[depart] = total[depart] + salary
     else:
        total[depart] = salary
   return total

def save_data():
   with open("employees.json" , "w") as file:
      json.dump(employees , file)
        
def load_data():
   global employees
   if os.path.exists("employees.json"):
      with open("employees.json" , "r") as file:
         loaded = json.load(file)
      employees.clear()
      employees.update(loaded)