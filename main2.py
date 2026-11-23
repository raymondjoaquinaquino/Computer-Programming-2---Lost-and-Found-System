from statistics import mode
import time
import csv
import json
import os
from datetime import datetime, date

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
  def __init__(self, item_id, name, description, date_reported, date_time_found, location_found
               , image_path, is_found, is_returned, status, reported_by_user_id, return_id):
    self.item_id = item_id
    self.name = name
    self.description = description
    self.date_reported = date_reported
    self.date_time_found = date_time_found
    self.location_found = location_found
    self.image_path = image_path
    self.is_found = is_found
    self.is_returned = is_returned
    self.status = status
    self.reported_by_user_id = reported_by_user_id
    self.return_id = return_id

   


  def itemInfo(self):
     print(f"Item ID: {self.item_id}")
     print(f"Item Name: {self.name}")
     print(f"Item Description: {self.description}")
     print(f"Date Reported: {self.date_reported}")
     print(f"Date time found: {self.date_time_found}")
     print(f"image_path: {self.image_path}")
     print(f"Found: {self.is_found}")
     print(f"Status: {self.status}")
     print(f"Report by user id: {self.reported_by_user_id}")
     print(f"Return id: {self.return_id}")


class ReturnRecord:
  def __init__(self, datereturned, item_id, is_returned: bool = False):
    self.datereturned = datereturned
    self.item_id = item_id
    self.is_returned = is_returned


class information(User):
  def __init__(self, name, email, school_id):
    pass
  
def main():
    print("Welcome to the Lost and Found Management System")
    time.sleep(3)
    while True:
      ask = input("Are you a staff or a student: ")
      if ask == "":
        print("Error, try again")

      elif ask not in ["Student","Staff"]:
         print("This is invalid")
         print("Please follow the correct format")

      else:
        break
    if ask == "Staff":
        print("Please enter the following information: ")
        time.sleep(2)

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
       time.sleep(2)

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
  
  answer = input("What would you like to do?: ")
  while answer != "Quit":
    if answer not in ["Report", "Search"]:
      print("Action is not valid")
      break
    else:
      if answer == "Search":
        print("Prompt to the search")

        ans = int(input("Enter the item ID: "))
    
        with open("LostItem (2).csv", mode = "r", newline = "", encoding = "utf-8") as csv_file:
          read = csv.reader(csv_file)
          for row in read:
            if str(ans) in row:
              print("Item Found")
              print(f"Item ID: {row[0]}")
              print(f"Item Name: {row[1]}")
              break
        select = input("Would you like to request to retrieve the item? (Y/N): ")
        if select == "Y":
          print("Retrieving Item...")
          time.sleep(2)
          print("Item Retrieved")
          

       
        elif select == "N":
          print("Item not retrieved")
      elif answer == "Report":
        print("Recording Item")
        print("Please enter the information of the item you found: ")
        time.sleep(3)
        item_id = int(input("Enter Item ID: "))
        item_name = input("Enter the Item name: ")
        item_description = input("Enter the item description: ")
        date_reported_item = input("Enter date reported: ")
        date_time_found = input("Enter time reported: ")
        image_path = "images"
        item_location = input("Enter the location of the found item: ")
        item_isfound = True
        item_isreturned = False
        item_status = input("input the status: ")
        report_user_id = int(input("Enter your user ID: "))
        return_recorded_id = int(input("Enter return record id: "))



        print("=======================")
        item_info = LostItem(item_id, item_name, item_description, date_reported_item, 
                           date_time_found, item_location, image_path,
                           item_isfound, item_isreturned, item_status, report_user_id, return_recorded_id)
        item_info.itemInfo()
        print("=======================")
        print("Adding to the lost and found file.....")
        time.sleep(3)
        head = ["item_id", "name", "description", "date_reported", 
              "date_time_found", "location_found", "image_path", 
              "is_found", "is_returned", "status", "reported_by_user_id", "return_record_id"]
        exist = os.path.isfile("LostItem (2).csv")


        with open("LostItem (2).csv", mode = "a", newline = "", encoding = "utf-8") as csv_file:
            write = csv.writer(csv_file)
            if not exist:
              write.writerow(head)
       
            write.writerow([item_id, item_name, item_description, date_reported_item
                        , date_time_found, item_location, image_path, item_isfound, item_status, report_user_id])
            with open("LostItem (2).csv", mode = "r", newline = "", encoding = "utf-8") as csv_file:
              read = csv.reader(csv_file)


            print(read)
            print("Save complete")
    loop = input("Would you like to continue (Y/N): ")
    if loop == "":
          print("Error")
    elif loop == "N":
       print("Thank you for using the system")
       break
   
    else:
       if loop == "Y":
        answer = input("What would you like to do?: ")


    

   

  


