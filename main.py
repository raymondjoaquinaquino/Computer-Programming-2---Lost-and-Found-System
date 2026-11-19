import time
import csv
import os
import json


class User:
  def __init__(self, name, email, school_id):
    self.name = name
    self.email = email
    self.school_id = school_id

class Student(User):
  def __init__(self, name, email, school_id, course):
    super().__init__(name, email, school_id)
    self.course = course

  
  def info(self):
    print(f"Name: {self.name}")
    print(f"Email: {self.email}")
    print(f"School ID: {self.school_id}")
    print(f"Course: {self.course}")

class Staff(User):
  def __init__(self, name, email, school_id, status):
    super().__init__(name, email, school_id)
    self.status = status
    
  def info(self):
    print(f"Name: {self.name}")
    print(f"Email: {self.email}")
    print(f"School ID: {self.school_id}")
    print(f"Employee Status: {self.status}")

class LostItem:
  def __init__(self, item_id, name, description, is_found: bool = False):
    self.item_id = item_id
    self.name = name
    self.description = description
    self.is_found = is_found

class ReturnRecord:
  def __init__(self, datereturned, item_id, is_returned: bool = False):
    self.datereturned = datereturned
    self.item_id = item_id
    self.is_returned = is_returned
  
def main():
  print("Welcome to the Lost and Found Management System")
  while True:
    ask = input("Are you a staff or a student: ")
    if ask == "":
      print("Error, try again")
    elif ask not in ["Student", "Staff"]:
      print("This is invalid")
      print("Please follow the correct format")
      
    else:
      break
  if ask == "Staff":
    print("Please enter the following information: ")
    name = input("Enter name: ")
    email = input("Email: ")
    id = input("School ID: ")
    status = input("Enter Status: ")
    print("============================")
    a = "Information"
    print(a.center(30))
    print("============================")

    staff = Staff(name, email, id, status)
    staff.info()
  elif ask == "Student":
    print("Enter the following information: ")
    name = input("Enter name: ")
    email = input("Email: ")
    id = input("School ID: ")
    course = input("Enter your course: ")
    print("============================")
    a = "Information"
    print(a.center(30))
    print("============================")
    student = Student(name, email, id, course)
    student.info()
  else:
    print("User not identified")
    


if __name__ == "__main__":
  main()
  while True:
    answer = input("What would you like to do?: ")
    if answer == "":
      print("Error. Please input an action")
    elif answer not in ["Report", "Search"]:
      print("Action is not valid")
    else:
      break
  if answer == "Search":
    print("Prompt to the search")
    ans = int(input("Enter the item ID: ")
    with open("LostItem.csv", mode = "r", newline = "", encoding = "utf-8") as csv_file:
      read = csv.reader(csv_file)
      for row in read:
        if str(ans) in row:
          print("Item Found")
          print(f"Item ID: {row[0]}")
          print(f"Iten Name:{row[1]}")
          break
    select = input("Would you like to retrieve the item? (Y/N): ")
    if select == "Y":
      print("Retrieving Item...")
      time.sleep(2)
      print("Item Retrieved")
    elif select == "N":
      print("Item not retrieved")

  




  
  elif answer == "Report":
    print("Prompt the reported item")
    print("Please enter the information of the item you found: ")
    time.sleep(3)
    item_id = int(input("Enter Item ID: "))
    item_name = input("Enter the Item name: ")
    item_description = input("Enter the item description: ")
    item_isfound = True

    print("=======================")
    item_info = LostItem(item_id, item_name, item_description, item_isfound)
    item_info.itemInfo()
    print("=======================")
    print("Adding to the lost and found file.....")
    time.sleep(3)
    head = ["item_id", "name", "description"]
    exist = os.path.isfile("LostItem.csv")

    with open("LostItem (2).csv", mode = "a", newline = "", encoding = "utf-8") as csv_file:
      write = csv.writer(csv_file)
      if not exist:
        write.writerow(head)
       
      write.writerow([item_id, item_name, item_description])
      with open("LostItem.csv", mode = "r", newline = "", encoding = "utf-8") as csv_file:
         read = csv.reader(csv_file)


      print(read)
      print("Save complete")







  
  else: 
    print("Error")
  
  







