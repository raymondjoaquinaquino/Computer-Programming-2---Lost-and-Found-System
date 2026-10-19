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
  def __init__(self, item_id, name, description):
    self.item_id = item_id
    self.name = name
    self.description = description

class ReturnRecord:
  def __init__(self, datereturned, item_id):
    self.datereturned = datereturned
    self.item_id = item_id
  
def main():
  print("Welcome to the Lost and Found Management System")
     
  ask = input("Are you a staff or a student: ")
  while ask == "":
      print("Error")
      print("")
      ask = input("Are you a staff or a student: ")
      if ask == "Staff".casefold():
            print("Teacher")
        elif ask == "Student".casefold():
            print("Student")


if __name__ == "__main__":
  main()
  
  







