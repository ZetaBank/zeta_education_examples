#include <iostream>
using namespace std;

class Animal {
public:
    Animal() : protectedData(1), privateData(2) {}
    void showAnimalData() {
        cout << "Animal class: " << endl;
        cout << "Protected Data: " << protectedData << endl;
        cout << "Private Data: " << privateData << endl;
    }
protected:
    int protectedData;
private:
    int privateData;
};

class Cat : public Animal {
public:
    void showCatData() {
        cout << "Cat class: " << endl;
        //cout << "Protected Data: " << protectedData << endl;
        cout << "Private Data: " << privateData << endl; // This line would cause a compilation error
    }
};

int main() {
    Animal myAnimal;
    myAnimal.showAnimalData();

    Cat myCat;
    myCat.showCatData();

    return 0;
}
