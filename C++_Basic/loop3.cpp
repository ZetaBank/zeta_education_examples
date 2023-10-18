#include <iostream>

using namespace std;

int main()
{
  int x = 0;
  int attempts = 0;

  cout << "Welcome to the 'Guess the Magic Number' game!\n";
  
  do {
    cout << "Guess the magic number (it's between 0 and 10): ";
    cin >> x;
    cin.ignore();

    if (x != 7) {
      cout << "Nope, that's not it! Try again!\n";
      attempts++;
    }

  } while (x != 7 && attempts < 3);

  if (x == 7) {
    cout << "You did it! 7 is the magic number!\n";
  } else {
    cout << "Aww, you've run out of attempts! Better luck next time!\n";
  }

  cin.get();
}
