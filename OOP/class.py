class Car:
  color = "red"
  brand = "Toyota"
c1=Car() #object creation(memory allocated)
print(c1.color)
#here c1 is a reference variable and Car() is an object of the class Car
#A reference variable stores the address (reference) of an object, not the actual object
#class is a blueprint and object is an instance of the class
#Class variables like color,brand are shared by all objects of the class