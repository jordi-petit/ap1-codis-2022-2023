/* Arrel digital */

#include <iostream>
#include <string>
using namespace std;

int suma_digits(int n)
{
    if (n == 0) {
        return 0;
    } else {
        return n % 10 + suma_digits(n / 10);
    }
}

int arrel_digital(int n)
{
    if (n < 10) {
        return n;
    } else {
        return arrel_digital(suma_digits(n));
    }
}

int main()
{
    cout << arrel_digital(87619) << endl;
}
