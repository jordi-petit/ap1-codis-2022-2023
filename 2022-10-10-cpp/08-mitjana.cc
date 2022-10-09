/* Mitjana d'una seqüència de reals */

#include <iostream>
using namespace std;

int main()
{
    int n = 0;
    double s = 0;
    double x;
    while (cin >> x) {
        n = n + 1;
        s = s + x;
    }
    cout << s / n << endl;
}
