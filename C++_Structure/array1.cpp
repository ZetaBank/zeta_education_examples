#include <iostream>

using namespace std;

int main() {
  string array[8][8]; // Declares an 8x8 array

  // Initialize the array with "😱" and "🐭"
  for (int x = 0; x < 8; x++) {
    for (int y = 0; y < 8; y++) {
      if (x == 3 && y == 3) {
        array[x][y] = "😱";
      } else {
        array[x][y] = "🐭";
      }
    }
  }

  cout << "Frightened Cat Surrounded by Mice:\n";
  for (int x = 0; x < 8; x++) {
    for (int y = 0; y < 8; y++) {
      cout << array[x][y] << ' ';
    }
    cout << "\n";
  }

  cin.get();
  return 0;
}
