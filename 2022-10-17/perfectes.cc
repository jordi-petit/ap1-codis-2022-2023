#include <iostream>
using namespace std;

bool es_primer(int n)
{
    if (n <= 1) {
        return false;
    }
    int c = 2;
    while (c * c <= n) {
        if (n % c == 0) {
            return false;
        }
        c = c + 1;
    }
    return true;
}

int suma_digits(int n)
{
    if (n < 10) {
        return n;
    } else {
        return suma_digits(n / 10) + n % 10;
    }
}

int es_primer_perfecte(int n)
{
    return (n < 10 or es_primer_perfecte(suma_digits(n))) and es_primer(n);
}

int main()
{
    int n;
    while (cin >> n) {
        cout << es_primer_perfecte(n) << endl;
    }
}