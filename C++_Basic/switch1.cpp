#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

void playgame() {
    int random_number, guess;

    // Random number generation
    srand(time(0));
    random_number = rand() % 100 + 1;

    cout << "Guess the number between 1 and 100: ";

    do {
        cin >> guess;

        if(guess > random_number) {
            cout << "Too high! Try again: ";
        }
        else if(guess < random_number) {
            cout << "Too low! Try again: ";
        }
        else {
            cout << "Congratulations! You guessed it!\n";
        }
    } while(guess != random_number);
}

void loadgame() {
    cout << "Loading game (not really, this is a simple example)...\n";
}

void playmultiplayer() {
    cout << "Multiplayer would be here if this were more than a simple example.\n";
}

int main() {
  int input;

  cout << "1. Play game\n";
  cout << "2. Load game\n";
  cout << "3. Play multiplayer\n";
  cout << "4. Exit\n";
  cout << "Selection: ";
  cin >> input;

  switch(input) {
    case 1:
      playgame();
      break;
    case 2:
      loadgame();
      break;
    case 3:
      playmultiplayer();
      break;
    case 4:
      cout << "Thank you for playing!\n";
      break;
    default:
      cout << "Error, bad input, quitting\n";
      break;
  }

  cin.get();
}
