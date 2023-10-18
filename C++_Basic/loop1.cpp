#include <iostream>

using namespace std;

int main()
{
  cout << "Counting has never been this fun!\n";

  for (int x = 0; x < 10; x++) {
    switch (x) {
      case 0:
        cout << x << " - Starting from zero, the hero!\n";
        break;
      case 1:
        cout << x << " - One is the loneliest number.\n";
        break;
      case 2:
        cout << x << " - Two's company.\n";
        break;
      case 3:
        cout << x << " - Three's a crowd.\n";
        break;
      case 4:
        cout << x << " - Four leaf clover, lucky you!\n";
        break;
      case 5:
        cout << x << " - Five golden rings!\n";
        break;
      case 6:
        cout << x << " - Six degrees of separation.\n";
        break;
      case 7:
        cout << x << " - Seventh heaven.\n";
        break;
      case 8:
        cout << x << " - Eight is great!\n";
        break;
      case 9:
        cout << x << " - Nine, feeling fine.\n";
        break;
    }
  }

  cout << "That was exhilarating!\n";

  cin.get();
}
