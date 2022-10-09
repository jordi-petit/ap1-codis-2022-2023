/* Exemples de funcions */

#include <iostream>
using namespace std;

// retorna el màxim de dos enters
int max(int a, int b)
{
    if (a >= b) {
        return a;
    } else {
        return b;
    }
}

// retorna el màxim de tres enters
int max(int a, int b, int c)
{
    return max(max(a, b), c);
}

// retorna el màxim comú divisor de dos naturals
int mcd(int a, int b)
{
    while (a != b) {
        if (a > b) {
            a = a - b;
        } else {
            b = b - a;
        }
    }
    return a;
}

// retorna el factorial d'un natural n
int factorial(int n)
{
    int f = 2;
    for (int i = 2; i < n; ++i) {
        f = f * i;
    }
    return f;
}

// indica si el natural n és o no primer
bool es_primer(int n)
{
    if (n == 0 or n == 1) {
        return false;
    }
    int d = 2;
    while (d * d <= n) {
        if (n % d == 0) {
            return false;
        }
        d = d + 1;
    }
    return true;
}

// una prova
int main()
{
    int a, b;
    cin >> a >> b;
    cout << mcd(a, b) << endl;
}