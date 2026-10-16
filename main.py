
class User:
  def __init__(self, name, email, school_id):
    self.name = name
    self.email = email
    self.school_id = school_id


class Student(User):
  def __init__(self, name, email, school_id, course):
    super.__init__(name, email, school_id)
    self.course = course


class Staff(User):
  def __init__(self, name, email, school_id):
    super.__init__(name, email, school_id)



def main():
  print("Welcome to the Lost and Found Management System")


if __name__ == "__main__":
  main()
  
  







