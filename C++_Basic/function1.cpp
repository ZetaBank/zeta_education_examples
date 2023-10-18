#include <iostream>
#include <sstream>

using namespace std;

int mult(int x, int y);

int main() {
  string input1, input2;
  int x, y;

  cout << "Welcome to the 'Not-So-Ordinary Multiplication Show'!\n";
  cout << "Please type two 'so-called' numbers to be multiplied: ";

  cin >> input1 >> input2;
  cin.ignore();

  stringstream ss1(input1);
  stringstream ss2(input2);

  if ((ss1 >> x) && (ss2 >> y)) {
    cout << "Alrighty then, " << x << " multiplied by " << y << " is... Drumroll... " << mult(x, y) << "!\n";
  } else {
    cout << "Ha! Nice try, but \"" << input1 << "\" and \"" << input2 << "\" aren't exactly what mathematicians call 'numbers.' \nLet's get numerical, shall we?\n";
  }

  cin.get();
}

int mult(int x, int y) {
  return x * y;
}
