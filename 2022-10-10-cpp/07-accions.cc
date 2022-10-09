#include <iostream>
using namespace std;

// intercanvia els valors de x i de y
void swap(int& x, int& y)
{
    int z = x;
    x = y;
    y = z;
}

// suma un segon a la hora d'un rellotge de 24h
void suma1seg(int& h, int& m, int& s)
{
    s = s + 1;
    if (s == 60) {
        s = 0;
        m = m + 1;
        if (m == 60) {
            m = 0;
            h = h + 1;
            if (h == 24) {
                h = 0;
            }
        }
    }
}

int main()
{
    int a, b;
    cin >> a >> b;
    swap(a, b);
    cout << a << " " << b << endl;
}