#include <iostream>

using namespace std;

int main()
{
  int age;

  cout << "Please input your age: ";
  cin >> age;
  cin.ignore();

  if (age < 10) {
    cout << "Wow, you're a kid! Do you like cartoons?\n";
  } else if (age < 20) {
    cout << "Ah, the teenage years. Exciting times, huh?\n";
  } else if (age < 30) {
    cout << "You're in your 20s? Time to explore the world!\n";
  } else if (age < 40) {
    cout << "In your 30s? Life is just getting good!\n";
  } else if (age < 50) {
    cout << "40s? That's the new 30s, you know.\n";
  } else if (age < 100) {
    cout << "A wise soul, aren't you?\n";
  } else if (age == 100) {
    cout << "A century old! That's amazing!\n";
  } else {
    cout << "You're how old? You must be a time traveler!\n";
  }

  cin.get();
}
