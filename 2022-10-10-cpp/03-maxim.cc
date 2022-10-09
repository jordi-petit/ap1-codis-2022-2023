/* Màxim de dos enters */

#include <iostream>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;
    int m;
    if (a >= b) {
        m = a;
    } else {
        m = b;
    }
    cout << m << endl;
}