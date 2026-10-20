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
  
  







