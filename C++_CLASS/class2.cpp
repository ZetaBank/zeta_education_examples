#include <iostream>

using namespace std;

class Animal {
public:
    Animal();
    void makeSound();
    void showAge();
    
protected:
    int age;  // Accessible by derived classes like Cat

private:
    int weight;  // Not accessible by derived classes

};

Animal::Animal() : age(0), weight(0) {
    cout << "An animal is created.\n";
}

void Animal::makeSound() {
    cout << "The animal makes a sound.\n";
}

void Animal::showAge() {
    cout << "Animal age is: " << age << "\n";
}

class Cat : public Animal {
public:
    Cat();
    void makeSound();
    void showCatDetails();

private:
    int whiskerLength;  // Only accessible within Cat class

};

Cat::Cat() : whiskerLength(5) {
    age = 2;  // We can access this because it's 'protected' in Animal
    cout << "A cat is created.\n";
}

void Cat::makeSound() {
    cout << "The cat meows.\n";
}

void Cat::showCatDetails() {
    cout << "Cat whisker length: " << whiskerLength << "\n";
    cout << "Cat age: " << age << "\n";  // Accessible because it's 'protected'
}

int main() {
    cout << "Creating an Animal object:\n";
    Animal myAnimal;
    myAnimal.showAge();  // Should show '0' as age
    //myAnimal.showAge();

    cout << "\nCreating a Cat object:\n";
    Cat myCat;
    myCat.makeSound();  // Overrides the general animal sound
    myCat.showCatDetails();  // Shows cat-specific details
    
    return 0;
}
