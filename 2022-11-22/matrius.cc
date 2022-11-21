#include <iostream>
#include <vector>
using namespace std;

using Fila = vector<double>;
using Matriu = vector<Fila>;

Matriu multiplica(const Matriu& a, const Matriu& b)
{
    int n = a.size();
    Matriu c(n, Fila(n, 0)); // crea matriu de n⨉n zeros
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < n; ++k) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    return c;
}

int main()
{
    Matriu a = {
        { 10, 20, 30 },
        { 15, 22, 25 },
        { 50, 15, 25 }
    };

    Matriu b = multiplica(a, a);
}
