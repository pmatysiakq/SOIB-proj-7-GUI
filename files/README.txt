1. Topologia pola komutacyjnego jest reprezentowana przez odpowiednie polaczenia wielu komutatorow 2x2
2. Topologia powinna byc zdefiniowana w postaci:

<N: liczba sekcji>
<Kn: komutatorow_w_sekcji_1 komutatorow w sekcji_2 komutatorow_w_sekcji_N>
<pusta linia>
<definicja komutatora 1.1>
<definicja komutatora 2.1>
<definicja komutatora K.1>

<definicja komutatora 1.2>
<definicja komutatora K.2>

<definicja komutatora 1.N>
<definicja komutatora K.N>

3. Definicja komutatora to 8 cyfr
-> Pierwsze dwie to definicja wejscia pierwszego
-> Dwie kolejne to definicja wejscia drugiego
-> Nastepnie dwie definiuja wyjscie pierwsze
-> I dwie ostatnie definiuja wyjscie drugie

4. Definicja polega na wskazaniu do jakiego komutatora i jakiego wyjscia/wejscia dane wejscie/wyjscie jest podlaczone.
5. Jezeli definiujemy wejscia w sekcji pierwszej lub wyjscia w sekcji ostatniej - zamiast ID podajemy 0 i zamiast
numeru linku danego komutatora (1/2) wskazujemy numer wejscia/wyjscia, gdyz numeracja jest ciagla

Przyklad:
3
2 2 2

0 1 0 2 1 1 2 1
0 3 0 4 1 2 2 2

1 1 2 1 1 1 2 1
1 2 2 2 1 2 2 2

1 1 2 1 0 1 0 2
1 2 2 2 0 3 0 4

LINK: https://ibb.co/BBKFwcS