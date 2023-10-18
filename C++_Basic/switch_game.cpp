#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int lastGuessedNumber = 0;  // For storing the last guessed number in playgame

void playgame() {
    int random_number, guess;

    srand(time(0));
    random_number = rand() % 100 + 1;

    cout << "Guess the number between 1 and 100: ";

    do {
        cin >> guess;
        lastGuessedNumber = guess;  // Save the last guessed number

        if(guess > random_number) {
            cout << "Too high! Try again: ";
        } else if(guess < random_number) {
            cout << "Too low! Try again: ";
        } else {
            cout << "Congratulations! You guessed it!\n";
        }
    } while(guess != random_number);
}

void loadgame() {
    cout << "Your last guessed number was " << lastGuessedNumber << ". Use it wisely!\n";
}

void playmultiplayer() {
    int random_number, guess;
    srand(time(0));
    random_number = rand() % 100 + 1;

    cout << "Multiplayer time! Guess the number between 1 and 100.\n";

    for(int player = 1; ; player = 3 - player) {
        cout << "Player " << player << ", it's your turn: ";
        cin >> guess;

        if(guess > random_number) {
            cout << "Too high! Next player's turn.\n";
        } else if(guess < random_number) {
            cout << "Too low! Next player's turn.\n";
        } else {
            cout << "Congratulations Player " << player << "! You guessed it!\n";
            break;
        }
    }
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
