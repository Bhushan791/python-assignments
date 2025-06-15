from abc import ABC, abstractmethod

# Base Animal Class
class Animal(ABC):
    def __init__(self, name, species, age, feeding_time):
        self.name = name
        self.species = species
        self.age = age
        self.feeding_time = feeding_time
    
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def feed(self):
        pass
    
    def get_details(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Feeding Time: {self.feeding_time}"

class Lion(Animal):
    def make_sound(self):
        return "Roar!!"
    
    def feed(self):
        return f"{self.name} the Lion has been fed at {self.feeding_time}"

class Elephant(Animal):
    def make_sound(self):
        return "Trumpet!"
    
    def feed(self):
        return f"{self.name} the Elephant has been fed at {self.feeding_time}"

class Parrot(Animal):
    def make_sound(self):
        return "Squawk!"
    
    def feed(self):
        return f"{self.name} the Parrot has been fed at {self.feeding_time}"

# Zoo class
class Zoo:
    def __init__(self):
        self.animals = []

zoo = Zoo()

def View_All_Animals():
    counter=1
    print("\n" + "*"*50)
    print("Here Is The List Of All Animals In Zoo")
    print("*"*50)
    
    if len(zoo.animals)==0:
        print("No animals in the zoo currently.")
    else:
        for i in zoo.animals:
            print(f"{counter}) Name: {i.name} {(' ') *15} Species: {i.species} {(' ') *10}Age: {i.age}  {(' ') *8} Feeding Time: {i.feeding_time} {(' ') *5} Sound: {i.make_sound()}")
            counter+=1
    print("*"*50 + "\n")

def Add_Animal():
    print("\n" + "*"*50)
    animal_name= input("Enter The Name of The Animal: ")
    animal_age = input("Enter The Age of Animal: ")
    feeding_time_input= input("Enter Feeding Time (e.g. 3 PM): ")
    
    if animal_name and animal_age and feeding_time_input:
        try:
            age_num = int(animal_age)
        except:
            print("Age must be a number!!")
            print("*"*50 + "\n")
            return
            
        print("Choose Animal Type:")
        print("1) Lion")
        print("2) Elephant") 
        print("3) Parrot")
        type_choice= input("Enter Type (1-3): ")
        
        if type_choice=="1":
            animal_type="Lion"
            new_animal = Lion(animal_name, "Lion", age_num, feeding_time_input)
        elif type_choice=="2": 
            animal_type="Elephant"
            new_animal = Elephant(animal_name, "Elephant", age_num, feeding_time_input)
        elif type_choice=="3":
            animal_type="Parrot" 
            new_animal = Parrot(animal_name, "Parrot", age_num, feeding_time_input)
        else:
            print("Invalid animal type, try Again!!")
            print("*"*50 + "\n")
            return
            
        decision = input(f"Are You Sure Want To Add This {animal_type}?(y/n) : ").lower()
        if decision== "y":
            zoo.animals.append(new_animal)
            print(f"{animal_type} named '{animal_name}' added to the zoo Successfully!!")
        else:
            print("Invalid Choice, try Again!!")
    else:
        print("Please fill all fields!!")
    print("*"*50 + "\n")

def Feed_All_Animals():
    print("\n" + "*"*50)
    print("Feeding All Animals")
    print("*"*50)
    
    if len(zoo.animals)==0:
        print("No animals to feed.")
    else:
        for j in zoo.animals:
            print(j.feed())
    print("*"*50 + "\n")

def Search_Animal():
    print("\n" + "*"*50)
    animal_found= False
    search_keyword= input("Enter Keyword To Search: ").lower()
    for k in zoo.animals:
        if search_keyword in k.name.lower() or search_keyword in k.species.lower():
            print("We Found Following From Your Search: ")
            print(f"Name: {k.name}, Species: {k.species}, Age: {k.age}, Feeding Time: {k.feeding_time}, Sound: {k.make_sound()}")
            animal_found= True

    if animal_found==False:    
        print(f"Sorry The Animal Like This Is Not Available")
    print("*"*50 + "\n")

def User_Actions():
    print("\n" + "*"*50)
    print("ZOO MANAGEMENT SYSTEM")
    print("Choose an action:")
    print("1) Add Animal")
    print("2) View All Animals")
    print("3) Feed All Animals")
    print("4) Search Animal")
    print("0) Exit")
    print("*"*50)

while True:
    User_Actions()
    try:
        user = int(input("Action You Want To perform: "))
    except:
        print("Please enter a valid number.")
        continue
    
    if user==0:
        print("Bye!!")
        break
    elif user==1:
        Add_Animal()
    elif user==2:
        View_All_Animals()
    elif user==3:
        Feed_All_Animals()
    elif user==4:
        Search_Animal()
    else:
        print("Invalid choice, please select a valid action.")