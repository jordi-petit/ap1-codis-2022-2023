#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Provincia {
    string nom;
    string capital;
    int habitants;
    int area;
    double pib;
};

struct Pais {
    string nom;
    string capital;
    vector<Provincia> provs;
};

using Paisos = vector<Pais>;
// typedef vector<Pais> Paisos;

//  Retorna la suma dels productes interiors bruts de totes les províncies amb densitat estrictament superior a d de tots els països en paisos que comencin per la lletra c.

double pib1(const Paisos& paisos, char c, double d)
{
    double s = 0;
    for (int i = 0; i < paisos.size(); ++i) {
        if (paisos[i].nom[0] == c) {
            for (int j = 0; j < paisos[i].provs.size(); ++j) {
                if (paisos[i].provs[j].habitants / double(paisos[i].provs[j].area) > d) {
                    s += paisos[i].provs[j].pib;
                }
            }
        }
    }
    return s;
}

double pib2(const Paisos& paisos, char c, double d)
{
    double s = 0;
    for (const Pais& pais : paisos) {
        if (pais.nom[0] == c) {
            for (const Provincia& prov : pais.provs) {
                if (prov.habitants / double(prov.area) > d) {
                    s += prov.pib;
                }
            }
        }
    }
    return s;
}

int main()
{
    Provincia prov = { "Barcelona", "Barcelona", 3000000, 100, 7456367 };
}