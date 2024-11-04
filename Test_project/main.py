import datetime

class User:
    def __init__(self, first_name: str, last_name: str, age: int):
        #Run validations to the received arguments
        assert age >= 0, f"Age {age} is not greater or equal to zero"
        
        # Assign to self object
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def calculate_year_of_birth(self):
        now = datetime.date.today().year

        return print(now-self.age)
    

user1 = User("Harry", "Potter", 12)
user1.calculate_year_of_birth()