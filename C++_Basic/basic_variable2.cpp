#include <iostream>

using namespace std;

int main()
{
  int thisisanumber;

  cout << "Please enter a number: ";
  cin >> thisisanumber;

  if (cin.fail()) {
    cin.clear();
    cin.ignore(1000, '\n');  // 버퍼를 클리어합니다.
    cout << "That was not a number.You are a very interesting person or person with excellent agility .\n";
  } else {
    cin.ignore();
    cout << "You entered: " << thisisanumber << "\n";
  }

  cin.get();
}
