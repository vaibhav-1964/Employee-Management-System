from data import employees
from employees_function import (register_employees , list_employees , find_employees ,
                                 show_employees , delete_employees , update_employees ,
                                 login , payroll , department_total , save_data , load_data)

def main():
   load_data()
   while True:
      print("\n Employee Management".center(210))
      print("\n 1.Register \n 2.Login \n 3.Exit")
      choice = input("\n Choose An Option : ").lower()
      if choice == "1" or choice == "register":
         register_employees()
         continue
      elif choice == "2" or choice == "login":
         user = login()
         if user == "":
            continue
         while True:
            print("\n Logged In As" , user , "")
            print("\n 1.List Of All Employees \n 2. Show My Detail \n 3.Update \n 4.Delete \n 5.Reports \n logout")
            choice1 = input("\n Choose Your Option : ").lower()
            if choice1 == "1" or choice1 == "list of all employees":
               list_employees()
            elif choice1 == "2" or choice1 == "show my detail":
               show_employees(user)
            elif choice1 == "3" or choice1 == "update":
               person = input("Enter Your ID : ")
               if person == user or person == "admin":
                update_employees(person , user)
               else:
                  print("You Can Only Change Your Own")
            elif choice1 == "4" or choice1 == "delete":
               person1 = input("Enter Your ID : ")
               if person1 == user or person1 == "admin":
                  delete_employees(person1 , user)
                  if person1 == user:
                   break
               else:
                  print("You Can Only Delete Your Own")
            elif choice1 == "5" or choice1 == "reports":
               if user == "admin":
                  print("Total Payroll: " , payroll())
                  print("By Department: " , department_total())
               else:
                  print("Admin Only")
            elif choice1 == "logout":
               print("You Are LOgged Out")
               break
            else:
               print("Invalid Input")
               continue
      elif choice == "3" or choice == "exit":
         print("GoodBye")
         break
      else:
         print("Invalid Choice ")
         continue

main()