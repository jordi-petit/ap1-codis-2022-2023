#include <cstdlib>
#include <ctime>
#include <iostream>
#include <vector>
using namespace std;

double now()
{
    return clock() / double(CLOCKS_PER_SEC);
}

// Ordena v[esq..dre] sabent que v[esq..mig] està ordenat
// i sabent que v[mig+1..dre] està ordenat.
void merge(vector<int>& v, int esq, int mig, int dre)
{
    vector<int> r;
    int i = esq;
    int j = mig + 1;
    while (i <= mig and j <= dre) {
        if (v[i] <= v[j]) {
            r.push_back(v[i]);
            ++i;
        } else {
            r.push_back(v[j]);
            ++j;
        }
    }
    while (i <= mig) {
        r.push_back(v[i]);
        ++i;
    }
    while (j <= dre) {
        r.push_back(v[j]);
        ++j;
    }
    for (int k = 0; k < dre - esq + 1; ++k) {
        v[k + esq] = r[k];
    }
}

// Ordena v[esq..dre].
void mergesort_rec(vector<int>& v, int esq, int dre)
{
    if (esq < dre) {
        int mig = (esq + dre) / 2;
        mergesort_rec(v, esq, mig);
        mergesort_rec(v, 1 + mig, dre);
        merge(v, esq, mig, dre);
    }
}

// Ordena la llista L per fusió.
void mergesort(vector<int>& v)
{
    mergesort_rec(v, 0, v.size() - 1);
}

// Mesura el temps per ordenar llistes amb elements aleatoris.
int main()
{
    for (int n = 50000; n < 1000001; n += 50000) {
        vector<int> v(n);
        for (int& x : v) {
            x = rand() % n;
        }
        double t1 = now();
        mergesort(v);
        double t2 = now();
        cout << n << " " << t2 - t1 << endl;
    }
}
