# Presentació AP1

## Professors

- Jordi Petit, jordi.petit-silvestre@upc.edu (Teoria)
- Jordi Puig, jordi.puig@upc.edu (Laboratori)

Consultes: quedem per correu electrònic. Les consultes es faran presencialment o per Google Meet usant els comptes UPC.

Important: Comuniqueu-vos amb els vostres professors amb el correu *oficial* de la universitat (`@estudiantat.upc.edu`), no amb comptes personals.


## Fonts d'informació

- [Racó](https://raco.fib.upc.edu): Repasseu els avisos freqüentment! Crec que hi ha un sistema d'alertes automàtiques que podeu configurar.

- [FIB](https://www.fib.upc.edu/ca/estudis/graus/grau-en-ciencia-i-enginyeria-de-dades): Informació del GCED
  - Horaris i aules
  - Exàmens
  - Pla d'estudis

- [Guia docent](https://www.fib.upc.edu/ca/estudis/graus/grau-en-ciencia-i-enginyeria-de-dades/pla-destudis/assignatures/AP1-GCED)

- [Jutge](https://jutge.org): Problemes i exàmens
  - Llista de problemes del curs AP-1
  - Llista de problemes del curs *Learning to program* (centenars de problemes extres per practicar)

- GitHub
  - Els codis escrits a l'ordinador durant les classes de teoria es podran anar trobant
    a https://github.com/jordi-petit/ap1-codis-2022-2023, organitzats per data i temes.

  - Els codis de cursos passast són a
    https://github.com/jordi-petit/ap1-codis-2017-2018,
    https://github.com/jordi-petit/ap1-codis-2018-2019,
    https://github.com/jordi-petit/ap1-codis-2019-2020,
    https://github.com/jordi-petit/ap1-codis-2020-2021,
    https://github.com/jordi-petit/ap1-codis-2021-2022.

  - Utilitzeu les *issues* per comunicar qualsevol errada als codis o,
    millor!, creu una *pull request* per esmenar-les.

- [Transparències d'en Jordi Cortadella](https://www.cs.upc.edu/~jordicf/Teaching/FME/Informatica/index.html)

- [Lliçons](https://lliçons.jutge.org)

  - Introducció a la Programació 
  - Eines de Programació
  - Ús del Terminal

- [Dipòsit d'Exàmens](https://examens.upc.edu/curs/270204/1280): Exàmens de cursos passats (amb algunes possibles solucions)


## Temari

1. Conceptes bàsics de programació.
   - Introducció a conceptes bàsics de programació: algorisme, programa, variables, expressions, assignacions.
   - Instruccions condicionals (`if`) i iteratives (`while`, `for`).
   - Resolució de problemes amb dades escalars: màxim de dos nombres, nombres primers, màxim comú divisor...
2. Funcions i recursivitat.
   - Funcions: disseny i pas de paràmetres.
   - Exemples de disseny de funcions.
   - Disseny recursiu.
   - Exemples de recursivitat simple (factorial, escriure la representació d'un nombre en binari).
   - Exemples de recursivitat múltiple (Fibonacci, Hanoi).
3. Vectors.
   - Representació d'estructures de dades amb vectors.
   - Algorismes de recorregut i cerca.
   - Algorismes d'ordenació de vectors: inserció, sel.lecció i fusió.
   - Anàlisi de la seva complexitat.
4.  Invariants i anàlisi de complexitat.
    - Disseny i raonament de bucles amb invariants.
    - Anàlisi de complexitat d'algorismes.
    - Notació O Gran.
    - Exemples d'anàlisi de complexitat amb iteracions i recursivitat.
5.  Matrius i tuples.
    - Algorismes bàsics sobre matrius (suma, simètrica, transposada, multiplicació). Cerca en matrius. Tuples, disseny d'estructures de dades i exemples d'utilització.
6.  Càlculs amb nombres reals.
    - Representació de nombres reals. Algorismes amb nombres reals: suma de sèries, mètode de Newton-Raphson, aproximació d'integrals definides. Polinomis: representació i operacions bàsiques.
7.  Algorismes bàsics de càlcul.
    - Algorismes amb complexitat logarítmica (potència, Fibonacci).
    - Algorismes geomètrics: puntes, rectes i poligons.
    - Sistemes d'equacions: eliminació Gaussiana.
8.  Algorismes combinatoris.
    - Generació de permutacions.
    - Cicles en permutacions.
    - Subseqüències que sumin una constant.
    - Camins en una graella.
    - Resolució d'un sudoku.

Pràctiques en Python i C++.


## Avaluació
    
Actes:
  - Examen parcial
    - en ordinador, amb Jutge (**PL**)
  - Examen final
    - en paper (**FT**)
    - en ordinador, amb Jutge (**FL**)

Nota: 0,6 max{0,3 PL + 0,7 FL, FL} + 0,4 FT.

Dates:
  - PL: dx 2 de nov, 08:00 a 11:00
  - FT: dl 17 de gen, 08:00 a 11:00
  - FL: dl 17 de gen, 15:00 a 18:00


## Exàmens amb Jutge

Caldrà resoldre alguns problemes de programació davant de l'ordinador, amb el
sistema d'exàmens del Jutge i els ordinadors de les aules informàtiques
(sistemes Linux). Sense apunts ni Internet. Els problemes s'hauran de resoldre
en Python i/o C++ (l'enunciat ho establirà).

Abans del PL, es crearà un examen de prova, que podreu fer a casa, perquè veieu
com funciona el sistema.

Per fer l'examen haureu de conèixer la vostra contrasenya de la universitat (per
entrar als ordinadors) i la vostra contrasenya del Jutge (per entrar a la web
d'examen). *No password, no exam.*


## Metodologia

La metodologia docent és molt pràctica i progressiva. Algunes consignes:

- Repasseu els apunts abans de la propera classe.

- Resoleu els problemes de les llistes del Jutge a temps.

- No deixeu els dubtes per més endavant. Pregunteu!

- Utilitzeu les construccions que us ensenyen els professors. Eviteu usar-ne d'altres.

- Obtenir un verd només vol dir que el programa passa els jocs de proves! Intenteu millorar
  el vostre programa, fent-lo més senzill i llegible. Ensenyeu-lo al professor.

- Col·laboreu amb els companys, però no els copieu o us hi repenjeu.  

Penseu que gran pes de l'avaluació consisteix en resoldre problemes com els de
les llistes del Jutge. No hi ha millor preparació que practicar, practicar i practicar.

