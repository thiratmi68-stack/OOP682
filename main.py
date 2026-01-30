class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print( f"{self.name} is {self.age} years old.")

    def __str__(self):
        return f"{self.name} is {self.age} years old."

def main():
    mydog = Dog("Buddy",3)
    mydog.info()
    yourdog = Dog("Paulie",2)
    yourdog.info()
    print(mydog) #เรียกใช้ __str__()

if __name__ == "__main__":
    main()
