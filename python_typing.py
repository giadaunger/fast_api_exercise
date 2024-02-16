name: str = "Giada"
age: int = 21
teacher: bool = False
price: float = 30.5
students: list[str] = []
student: set[str] = {"Giada", "Miranda", "Giada"}
student: dict[str, str] = {}
student: tuple[str, str, int] = ("Giada", 21, True)

student: list[dict[str, dict[str, str]]]
# Eller (Man behöver ej definera vad en dict ska innehålla)
student: list[dict]

def say_hello(name: str, age: int):
	print(f"Hello {name}, you are {age} years old")

def print_students(students: list[str]):
	for student in students:
		print(student.capitalize())
		
def divide(num1: int | float, num2: int | float) -> float:
	return num1 / num2



def print_number(number: str | int = 0): # <--- default
		print(number)

print_number(10)
print_number("10")
print_number() # <--- default value appliceras
print_number(None) # <--- NOPE, inte OK



def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

# Alla fungerar / är OK
say_hi("tobias")
say_hi(None) # helt OK, vi sa ju att typen får vara None. 
say_hi() # <--- default value blir None, vilket är OK eftersom typen kan vara None



class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name