#include <iostream>
#include <vector>
using namespace std;

vector<int> suma(const vector<int>& v1, const vector<int>& v2)
{
    int n = v1.size();
    vector<int> r(n);
    for (int i = 0; i < n; ++i) {
        r[i] = v1[i] + v2[i];
    }
    return r;
}

void doblar(const vector<int>& v)
{
    for (int& x : v) {
        x *= 2;
    }
}

int main()
{
    // Creació d'un vector amb 3 posicions
    vector<int> v1 = { 10, 20, 30 };

    // Creació d'un vector buit
    vector<int> v2;

    // Afegir elements al final d'un vector
    v2.push_back(1);
    v2.push_back(2);
    v2.push_back(3);
    v2.push_back(4);

    // Treure element al final d'un vector
    v2.pop_back();

    // Crida a una funció amb dos vector que retorna un vector
    vector<int> v3 = suma(v1, v2);

    // Crida a una acció
    doblar(v3);

    // Recorregut
    for (int x : v3) {
        cout << x << endl;
    }
}
