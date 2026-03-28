from models import Animal, Dog, Cat


def main():
   
    animal = Animal("Generic", 5, "Unknown")
    dog = Dog("Nurik", 47, "Golden Retriever")
    cat = Cat("Mukhtar", 1, "White")

   
    animals = [animal, dog, cat]

    
    for a in animals:
        print(a)  
        print(a.get_info())
        print("Sound:", a.speak()) 
        print("-" * 30)


    print(dog.fetch())
    print(cat.scratch())


if __name__ == "__main__":
    main()