#include <iostream>

using namespace std;

// General Animal class
class Animal {
public:
    Animal();  // Constructor
    void makeSound();  // General behavior for all animals
    
};

Animal::Animal() {
    cout << "An animal is created.\n";
}

void Animal::makeSound() {
    cout << "The animal makes a sound.\n";
}

// Cat class that inherits from Animal
class Cat : public Animal {
public:
    Cat();  // Constructor
    void makeSound();  // Behavior specific to cats
    
};

Cat::Cat() {
    cout << "A cat is created.\n";
}

void Cat::makeSound() {
    cout << "The cat meows.\n";
}

int main() {
    cout << "Creating an Animal object:\n";
    Animal myAnimal;
    myAnimal.makeSound();
    
    cout << "\nCreating a Cat object:\n";
    Cat myCat;
    myCat.makeSound();  // Note this overrides the general animal sound
    
    return 0;
}
