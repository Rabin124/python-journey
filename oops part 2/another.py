class Person:
  __name = "anonymous"

  def __hello(self):
    print("Hello, I am a person")

  def welcome(self):
    self.__hello()

p1 = Person()

print(p1.welcome())  # This will raise an AttributeError because __name is private