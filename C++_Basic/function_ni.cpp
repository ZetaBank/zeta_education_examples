#include <iostream>
#include <sstream>
#include <cmath>

using namespace std;

int calculateSum(int x, int y);
int calculateDiff(int x, int y);
void NietzscheQuotes(int sum, int diff);

int main() {
  for(int i = 0; i < 2; i++) {
    string input1, input2;
    int x, y;

    cout << "Round " << (i + 1) << ": Welcome to Nietzsche's Wisdom Chamber!\n";
    cout << "Type two numbers, and let's uncover some wisdom: ";

    cin >> input1 >> input2;
    cin.ignore();

    stringstream ss1(input1);
    stringstream ss2(input2);

    if ((ss1 >> x) && (ss2 >> y)) {
      int sum = calculateSum(x, y);
      int diff = calculateDiff(x, y);
      cout << "With the numbers " << x << " and " << y << ", ";
      NietzscheQuotes(sum, diff);
    } else {
      cout << "Those aren't numbers! Nietzsche would be disappointed, try again.\n";
    }
  }

  cin.get();
}

int calculateSum(int x, int y) {
  return x + y;
}

int calculateDiff(int x, int y) {
  return abs(x - y);
}

void NietzscheQuotes(int sum, int diff) {
  if(sum < 10) {
    cout << "Nietzsche says: 'He who has a why to live for can bear almost any how.'\n";
  } else if(sum >= 10 && sum < 20) {
    cout << "Nietzsche says: 'That which does not kill us makes us stronger.'\n";
  } else if(sum >= 20 && sum < 30) {
    cout << "Nietzsche says: 'Invisible threads are the strongest ties.'\n";
  } else if(sum >= 30 && sum < 40) {
    cout << "Nietzsche says: 'You have your way. I have my way. As for the right way, it does not exist.'\n";
  } else if(diff <= 5) {
    cout << "Nietzsche says: 'Freedom is the will to be responsible to ourselves.'\n";
  } else if(diff > 5 && diff <= 15) {
    cout << "Nietzsche says: 'The earth has a skin and that skin has diseases; one of its diseases is called man.'\n";
  } else {
    cout << "Nietzsche says: 'Art is the proper task of life.'\n";
  }
}
