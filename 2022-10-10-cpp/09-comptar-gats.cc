/* Compta quantes paraules gat hi ha a l'entrada */

#include <iostream>
#include <string>
using namespace std;

int main()
{
    int c = 0;
    string x;
    while (cin >> x) {
        if (x == "gat") {
            c = c + 1;
        }
    }
    cout << c << endl;
}
