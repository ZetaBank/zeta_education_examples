#include <iostream>

using namespace std;

struct database {
  int id_number;
  int age;
  float salary;
};

int main() {
  database employee;  // There is now an employee variable that has modifiable variables inside it.
  
  employee.age = 22;
  employee.id_number = 1;
  employee.salary = 12000.21;

  // 출력하여 변수 값을 확인
  cout << "Employee Information:" << endl;
  cout << "ID Number: " << employee.id_number << endl;
  cout << "Age: " << employee.age << endl;
  cout << "Salary: " << employee.salary << endl;
}
