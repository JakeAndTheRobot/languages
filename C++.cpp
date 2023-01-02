#include <iostream>
using namespace std;

// Main function
int main() {
  cout << "Hello, world!" << endl;
  return 0;
}

// Variables
int x;
float y;
char c;

// Arrays
int a[10];
float b[5];
char d[20];

// Constants
const int SIZE = 10;

// Functions
void print() {
  cout << "Hello, world!" << endl;
}

int sum(int x, int y) {
  return x + y;
}

// Control structures
if (x > y) {
  cout << "x is greater than y" << endl;
} else if (x < y) {
  cout << "x is less than y" << endl;
} else {
  cout << "x is equal to y" << endl;
}

for (int i = 0; i < 10; i++) {
  cout << i << endl;
}

while (x < 10) {
  cout << x << endl;
  x++;
}

do {
  cout << x << endl;
  x++;
} while (x < 10);

switch (x) {
  case 1:
    cout << "x is 1" << endl;
    break;
  case 2:
    cout << "x is 2" << endl;
    break;
  default:
    cout << "x is not 1 or 2" << endl;
    break;
}

// Classes
class Point {
  private:
    int x;
    int y;
  public:
    void setX(int newX) {
      x = newX;
    }
    void setY(int newY) {
      y = newY;
    }
    int getX() {
      return x;
    }
    int getY() {
      return y;
    }
};

// Object
Point p;
p.setX(10);
p.setY(20);

int x = p.getX();
int y = p.getY();
