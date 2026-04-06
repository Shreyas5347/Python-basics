class Student:
    #__init__ is a constructor which is used to initialize the object    
    #it is called automatically when an object is created

    def __init__(self): 
        #self is a reference variable which is pointing  to the current object
        #it is used to access current object within the class
        #it is not compulsory to write self keyword but it is a convention to use it
        self.name="Shreyas"
        self.age=21
    def talk(self):
        print("hello my name is",self.name)
        print("my age is",self.age)
s1=Student() 
s1.talk()