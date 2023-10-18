#include <iostream>
#include <limits> 
 
using namespace std;
 
int main()
{
  int thisisanumber;
 
  cout<<"Please enter a number: ";
  cin>> thisisanumber;

 if (cin.fail()) {
    cin.clear();
    cin.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
    cout << "That was not a number. You are a very curious person.\n";
  } else {
    cin.ignore();
    cout << "You entered: " << thisisanumber << "\n";
  }
  cin.get();
}
