/* Factorial d'un natural */

#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int f = 1;
    for (int i = 2; i <= n; ++i) {
        f = f * i;
    }

    /*
    {
        int i = 2;
        while (i <= 2) {
            f = f * i;
            i = i + 1;
        }
    }
    */

    cout << f << endl;
}