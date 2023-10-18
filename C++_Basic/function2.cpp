#include <iostream>
#include <sstream>

using namespace std;

int makeYear(int x, int y);
void famousQuote(int year);

int main() {
  for(int i = 0; i < 2; i++) {  // Loop twice to get two pairs of numbers
    string input1, input2;
    int x, y;

    cout << "Round " << (i + 1) << ": Welcome to the 'Wisdom Through Time'!\n";
    cout << "Type two numbers, and let's uncover some wisdom: ";

    cin >> input1 >> input2;
    cin.ignore();

    stringstream ss1(input1);
    stringstream ss2(input2);

    if ((ss1 >> x) && (ss2 >> y)) {
      int year = makeYear(x, y);
      cout << "You've just created the year " << year << ". Let's hear some wisdom from that era!\n";
      famousQuote(year);
    } else {
      cout << "Those aren't numbers! Try again, wisdom is waiting!\n";
    }
  }

  cin.get();
}

int makeYear(int x, int y) {
  return x * 100 + y;
}

void famousQuote(int year) {
  if(year < 1000) {
    cout << "Socrates: 'I know that I am intelligent, because I know that I know nothing.'\n";
  } else if(year < 1250) {
    cout << "Rumi: 'The wound is the place where the Light enters you.'\n";
  } else if(year < 1500) {
    cout << "Leonardo da Vinci: 'Learning never exhausts the mind.'\n";
  } else if(year < 1750) {
    cout << "Voltaire: 'I disapprove of what you say, but will defend to the death your right to say it.'\n";
  } else if(year < 2000) {
    cout << "Albert Einstein: 'Imagination is more important than knowledge.'\n";
  } else {
    cout << "Steve Jobs: 'Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work.'\n";
  }
}
