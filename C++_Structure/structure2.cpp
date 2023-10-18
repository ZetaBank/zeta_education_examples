#include <iostream>

using namespace std;

struct Beauty {
  string name;
  int age;
  float height; // in cm
  string eyeColor;
  string nationality;
};

int main() {
  Beauty person;
  Beauty *ptr;

  // 세계적인 미인, 예를 들어, 'Marilyn Monroe'의 데이터를 넣습니다.
  person.name = "Marilyn Monroe";
  person.age = 36;  // Age at the time of her death
  person.height = 166.0; // in cm
  person.eyeColor = "Blue";
  person.nationality = "American";

  ptr = &person;

  // 출력하여 변수 값을 확인
  cout << "World Famous Beauty Information:" << endl;
  cout << "Name: " << ptr->name << endl;
  cout << "Age: " << ptr->age << endl;
  cout << "Height: " << ptr->height << " cm" << endl;
  cout << "Eye Color: " << ptr->eyeColor << endl;
  cout << "Nationality: " << ptr->nationality << endl;

  cin.get();
  
  return 0;
}
