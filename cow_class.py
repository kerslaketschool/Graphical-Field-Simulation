from animal_class import*

class Cow(Animal):
    """A Cow"""

    def __init__(self,name):
        super().__init__(1,3,6,name)
        self._type = "Cow"

def main():
    name = input("What name")
    new_cow = Cow(name)
    print(new_cow.report())
    manual_grow(new_cow)
    print(new_cow.report())
    manual_grow(new_cow)
    print(new_cow.report())

if __name__ == "__main__":
    main()
    
