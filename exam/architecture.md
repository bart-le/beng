# TECHNIKI I ARCHITEKTURA KOMPUTERÓW

## Model architekturalny komputera wg. von Neumanna a model obliczeniowy komputera na podstawie maszyny Turinga i ich rola w informatyce

Oba modele odgrywają kluczową rolę w rozwoju i zrozumieniu informatyki. Model Turinga dostarcza teoretycznych podstaw rozumienia obliczeń, podczas gdy model von Neumanna opisuje praktyczną architekturę większości używanych dzisiaj komputerów.

### Model obliczeniowy Turinga

Model obliczeniowy opracowany przez Alana Turinga, stanowiący abstrakcyjne przedstawienie procesu obliczeniowego.

-   **Uniwersalność**

    Maszyna Turinga jest w stanie symulować działanie każdej innej maszyny Turinga, co klasyfikuje ją jako uniwersalny model obliczeń.

-   **Elementy składowe**

    -   Skończony zbiór symboli, które można zapisywać na taśmie.
    -   Nieskończona w jednym kierunku taśma podzielona na komórki, każda przechowująca jeden symbol.
    -   Głowica zdolna do odczytywania i zapisywania symboli na taśmie oraz przesuwania się w lewo lub prawo.
    -   Skończony zbiór stanów maszyny, w tym stan początkowy i stany końcowe.
    -   Tablica przejść, która dla każdego stanu i odczytanego symbolu określa, jaki symbol zapisać, w którym kierunku przesunąć głowicę i do jakiego stanu przejść.

-   **Zastosowanie**

    Chociaż jest to model teoretyczny, posłużył do zdefiniowania kluczowych pojęć w teorii obliczeń i jest nadal używany do analizy problemów obliczeniowych.

### Model obliczeniowy von Neumanna

Architektura komputera, w której jednostka przetwarzająca i pamięć są rozdzielone, a dane i instrukcje są przechowywane w tej samej pamięci.

-   **Zintegrowana pamięć**

    Kluczową cechą jest wspólna pamięć dla danych i programów, co umożliwia modyfikację programu podczas jego wykonywania.

-   **Elementy składowe**

    -   **Pamięć komputera**: Przechowuje zarówno dane, jak i instrukcje.
    -   **Jednostka sterująca**: Interpretuje i wykonuje instrukcje, kontroluje przepływ informacji.
    -   **Jednostka arytmetyczno/logiczna (ALU)**: Wykonuje operacje matematyczne i logiczne.
    -   **Urządzenia wejścia/wyjścia**: Umożliwiają komunikację komputera z otoczeniem.

-   **Sterowanie**

    Kolejność instrukcji jest kontrolowana przez licznik rozkazów, który może być modyfikowany zarówno sekwencyjnie, jak i na podstawie instrukcji skoku.

-   **Zastosowanie**

    Model von Neumanna stał się podstawą dla większości współczesnych komputerów.

## Logika boolowska i jej zastosowania w warstwie sprzętowej komputerów

Logika boolowska, będąca podstawą matematyki operującej na wartościach prawda/fałsz (często reprezentowanych jako 1/0), stanowi kluczowy element w projektowaniu i funkcjonowaniu sprzętu komputerowego. Bramki logiczne tworzą podstawowe bloki budowlane układów scalonych, takich jak procesory, pamięć RAM i układy FPGA. Pozwalają one na wykonywanie obliczeń, kontrolę przepływu danych oraz realizację różnorodnych funkcji w sprzęcie komputerowym.

### Tabele prawdy dla bramek logicznych

|   A   |   B   |  AND  |  OR   |  XOR  | NAND  |  NOR  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|   0   |   0   |   0   |   0   |   0   | **1** | **1** |
|   0   | **1** |   0   | **1** | **1** | **1** |   0   |
| **1** |   0   |   0   | **1** | **1** | **1** |   0   |
| **1** | **1** | **1** | **1** |   0   |   0   |   0   |

|   A   |  NOT  |
| :---: | :---: |
|   0   | **1** |
| **1** |   0   |

### Zastosowania w warstwie sprzętowej komputerów

Współczesne komputery i urządzenia cyfrowe są złożone z miliardów tranzystorów, które działają jako bramki logiczne. Dzięki logice boolowskiej możliwe jest projektowanie i realizacja tych zaawansowanych systemów. Jej fundamentalna rola w informatyce i inżynierii elektronicznej sprawia, że jest niezbędna w kształceniu każdego inżyniera w tych dziedzinach.

-   **Bramki logiczne**

    Są to podstawowe bloki budujące wszystkie układy cyfrowe. Umożliwiają one realizację podstawowych operacji, takich jak AND, OR, NOT, XOR, NAND, NOR itp. W połączeniu bramki te tworzą skomplikowane układy, które wykonują różne funkcje.

-   **Układy kombinacyjne**

    Są to układy, których wyjście zależy wyłącznie od aktualnego stanu wejść, bez uwzględnienia poprzednich stanów. Przykładami mogą być multipleksery, demultipleksery, dekodery, kodery, sumatory czy porównywarki.

-   **Układy sekwencyjne**

    W przeciwieństwie do układów kombinacyjnych, wyjście układów sekwencyjnych zależy nie tylko od aktualnych wejść, ale także od ich poprzednich stanów. Rejestry, liczniki czy automaty skończone to przykłady układów sekwencyjnych.

-   **Pamięć**

    Logika boolowska jest używana do projektowania układów pamięciowych, takich jak RAM (Random Access Memory) czy ROM (Read-Only Memory). Operacje odczytu i zapisu są sterowane za pomocą logiki boolowskiej.

-   **Procesory**

    Centralna jednostka przetwarzająca (CPU) komputera, która wykonuje operacje arytmetyczne i logiczne, jest skonstruowana na bazie logiki boolowskiej. Operacje takie jak dodawanie, odejmowanie, porównywanie wartości czy testowanie bitów są realizowane przez układy bazujące na logice boolowskiej.

-   **Układy sterujące**

    Wiele systemów wbudowanych i mikrokontrolerów wykorzystuje logikę boolowską do sterowania działaniem innych urządzeń lub systemów, takich jak silniki, czujniki czy wyświetlacze.

-   **Projektowanie układów FPGA**

    FPGA (ang. Field-Programmable Gate Array) to układy, które można programować po ich wyprodukowaniu. Projektanci FPGA wykorzystują logikę boolowską do definiowania zachowania układu.

-   **Optymalizacja układów**

    Narzędzia takie jak mapy Karnaugh'a służą do upraszczania funkcji boolowskich w celu zminimalizowania liczby używanych bramek logicznych i zoptymalizowania wydajności układu.

-   **Schematy logiczne**

    Są to graficzne reprezentacje układów cyfrowych, które przedstawiają połączenia między różnymi bramkami logicznymi. Umożliwiają one projektantom lepsze zrozumienie i analizę projektowanego układu.

## Zapis binarny liczb całkowitych, zapis zmiennoprzecinkowy liczb rzeczywistych, arytmetyka komputerowa

### Zapis binarny liczb całkowitych

Zapis binarny liczb całkowitych jest sposobem przedstawienia liczb całkowitych za pomocą dwóch cyfr: `0` i `1`. Istnieją różne metody zapisu liczb binarnych w zależności od tego, czy liczba jest dodatnia czy ujemna oraz w jaki sposób chcemy ją reprezentować. Oto kilka podstawowych sposobów zapisu:

1. **Bez znaku (unsigned)**

    W tej reprezentacji tylko liczby dodatnie są możliwe do przedstawienia. Każdy bit reprezentuje potęgę liczby 2.

    > $3_{10} = 0011_{2}$, bo $2^1 + 2^0 = 3$

2. **Kod znaku i wartości (Sign and Magnitude)**

    Najstarszy bit (najbardziej znaczący) reprezentuje znak (0 dla dodatnich, 1 dla ujemnych), a pozostałe bity reprezentują wartość liczby w formie bez znaku.

    > $+3_{10} = 0011_{2}$
    >
    > $-3_{10} = 1011_{2}$

3. **Kod U1 (One's Complement)**

    Liczby dodatnie są takie same jak w reprezentacji bez znaku. Aby uzyskać reprezentację liczby ujemnej, odwracamy wszystkie bity jej wartości dodatniej.

    > $+3_{10} = 0011_{2}$
    >
    > $-3_{10} = 1100_{2}$

4. **Kod U2 (Two's Complement)**

    Tak jak w kodzie U1, ale do uzyskania liczby ujemnej dodajemy 1 do odwrotności jedynkowej (U1) liczby dodatniej. Jest to najpowszechniej używana metoda w komputerach.

    > $+3_{10} = 0011_{2}$
    >
    > $-3_{10} = 1101_{2}$

5. **Kod BCD (Binary-Coded Decimal)**

    W tym przypadku każda cyfra liczby dziesiętnej jest reprezentowana przez jej 4-bitowy odpowiednik binarny.

    > $19_{10} = 0001\ 1001_{2}$

6. **Kod Gray'a**

    Jest to binarny kod numeryczny, w którym dwie kolejne wartości różnią się tylko jednym bitem. Jest używany w niektórych systemach cyfrowych, ale nie służy bezpośrednio do standardowej arytmetyki binarnej.

### Zapis liczb ułamkowych

1. **Zapis stałoprzecinkowy**

    Zapis stałoprzecinkowy dzieli liczbę binarną na dwie części: część całkowitą i ułamkową. Miejsce przecinka jest stałe i z góry określone.

    > Liczba $101.011_{2}$ będzie miała wartość $1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 + 0 \times 2^{-1} + 1 \times 2^{-2} + 1 \times 2^{-3}$

2. **Zapis zmiennoprzecinkowy**

Liczby zmiennoprzecinkowe w reprezentacji binarnej składają się z trzech głównych części: znaku, mantysy i wykładnika. Głównym celem takiego zapisu jest reprezentacja szerokiego zakresu wartości z różnym stopniem precyzji.

-   **Znak (Sign)**

    Określa, czy liczba jest dodatnia (0) czy ujemna (1).

-   **Wykładnik (Exponent)**

    Przesunięcie wartości mantysy. Jest on zazwyczaj reprezentowany w formie przesuniętej, co oznacza, że pewna wartość jest dodawana do faktycznego wykładnika, aby unikać ujemnych wartości.

-   **Mantysa (Fraction)**

    Reprezentuje rzeczywistą wartość liczby w formie ułamkowej.

-   **IEEE 754**

    To standard, który definiuje formaty zmiennoprzecinkowe dla liczby bitów o różnych długościach (np. 32 bity, 64 bity). Najpopularniejsze wersje to pojedyncza precyzja (32 bity) i podwójna precyzja (64 bity).

    -   Pojedyncza precyzja (32 bity)

        -   **Znak (Sign)**: 1 bit
        -   **Wykładnik (Exponent)**: 8 bitów
        -   **Mantysa (Fraction)**: 23 bity

    -   Podwójna precyzja (64 bity)

        -   **Znak (Sign)**: 1 bit
        -   **Wykładnik (Exponent)**: 11 bitów
        -   **Mantysa (Fraction)**: 52 bity

    > -   Konwersja części całkowitej:
    >
    >     $6_{10}$ jest równoważne $110_2$ w systemie binarnym.
    >
    > -   Konwersja części ułamkowej:
    >
    >     -   $0.75_{10}$ w systemie dziesiętnym to $0.11_2$ w systemie binarnym.
    >     -   $0.75 \cdot 2 = 1.5$ (Pierwszy bit po przecinku to 1)
    >     -   $0.5 \cdot 2 = 1.0$ (Drugi bit po przecinku to 1)
    >     -   $6.75_{10} = 110.11_2$
    >
    > -   Reprezentacja w standardzie IEEE 754 (pojedyncza precyzja)
    >
    >     -   Zamiana $110.11_2$ na $1.1011_2 \cdot 2^2$.
    >     -   Ponieważ $6.75$ jest liczbą dodatnią, bit znaku to: 0.
    >     -   Pojedyncza precyzja IEEE 754 używa przesuniętego wykładnika z offsetem 127. Dlatego rzeczywisty wykładnik to: $2 + 127 = 129$. 129 w systemie dziesiętnym to $10000001_2$.
    >     -   Po normalizacji, część po przecinku to: $1011$. W przypadku IEEE 754 mantysa ma 23 bity, więc resztę wypełniamy zerami.
    >     -   w formacie pojedynczej precyzji $6.75_{10} = 0\ 10000001\ 10110000000000000000000_{2}$

### Arytmetyka komputerowa

#### Dodawanie i odejmowanie

1. **Dopasowanie wykładników**

    Przed dodaniem dwóch liczb, ich wykładniki muszą być takie same. To oznacza przesunięcie mantysy jednej z liczb, aby obie miały ten sam wykładnik.

2. **Dodanie mantys**

    Po dostosowaniu wykładników, mantysy obu liczb są dodawane.

3. **Normalizacja**

    Wynik może wymagać normalizacji. Oznacza to, że może być konieczne przesunięcie wyniku tak, aby miał on poprawną formę dla reprezentacji zmiennoprzecinkowej.

4. **Zaokrąglenie**

    Jeśli wynik mantysy przekroczy dostępną precyzję, może być konieczne zaokrąglenie.

#### Mnożenie

1. **Mnożenie mantys**

    Mantysy obu liczb są mnożone, co daje mantysę wynikową.

2. **Dodawanie wykładników**

    Wykładniki obu liczb są dodawane razem.

3. **Normalizacja i zaokrąglenie**

    Tak jak w przypadku dodawania, wynik może wymagać normalizacji i/lub zaokrąglenia.

#### Dzielenie

1. **Dzielenie mantys**

    Mantysa jednej liczby jest dzielona przez mantysę drugiej liczby.

2. **Odejmowanie wykładników**

    Wykładniki są odejmowane od siebie.

3. **Normalizacja i zaokrąglenie**

    Potrzebne, podobnie jak w przypadku innych operacji.

## Miary efektywności obliczeniowej procesorów, pojemności pamięci komputerowej oraz wydajności systemów obliczeniowych

### Miary efektywności obliczeniowej procesorów

#### Cechy architekturalne

-   **Liczba i cechy bloków wykonawczych**

    Dotyczy ilości jednostek w procesorze, które wykonują operacje określone w instrukcjach programu.

-   **Struktura i parametry pamięci**

    Obejmuje liczbę poziomów pamięci, w tym pamięci podręcznej oraz organizację przechowywanych danych.

-   **Cechy i parametry listy rozkazów**

    Typy instrukcji, dostępne tryby adresowania, oraz sposób realizacji instrukcji wejścia/wyjścia.

-   **Liczba i rozmiary rejestrów danych**

-   **Liczba i rozmiary rejestrów adresowych**

-   **Szerokość szyn danych i adresów**

-   **Cechy układu przerwań**

-   **Dołączalne koprocesory**

#### Parametry techniczne

-   **Częstotliwość zegara**

    Kluczowy parametr określający, jak szybko procesor może wykonywać operacje

-   **Technologia wytwarzania**

    Charakteryzująca się stopniem scalenia układu i liczbą tranzystorów na chipie

-   **Liczba tranzystorów**

    Wskazuje na stopień zaawansowania i miniaturyzacji technologii wytwarzania procesora

-   **Napięcie zasilania**

-   **Pobór mocy**

-   **Obudowa**

#### Miary wydajności

-   **MIPS (Millions of Instructions per Second)**

    Ilość instrukcji stałoprzecinkowych wykonywanych w ciągu sekundy.

-   **MFLOPS (Millions of Floating Point Operations per Second)**

    Ilość operacji zmiennoprzecinkowych wykonywanych w ciągu sekundy.

### Pojemność pamięci komputerowej

Maksymalna ilość informacji, którą urządzenie może przechować.

Jednostki pojemności:

-   **Bit (b)**: Najmniejsza jednostka
-   **Bajt (B)**: Składa się z 8 bitów
-   **Kilobajt (kB)** lub **kibibajt (KiB)**: 1000 bajtów lub 1024 bajtów ($2^{10}$)
-   **Megabajt (MB)** lub **mebibajt (MiB)**: 1 000 000 bajtów lub 1 048 576 bajtów ($2^{20}$)
-   **Gigabajt (GB)** lub **gibibajt (GiB)**: 1 miliard bajtów lub $2^{30}$ bajtów
-   **Terabajt (TB)** lub **tebibajt (TiB)**: 1 bilion bajtów lub $2^{40}$ bajtów
-   **Petabajt (PB)** lub **pebibajt (PiB)**: 1000 terabajtów lub $2^{50}$ bajtów

### Wydajność systemów obliczeniowych

-   W rzeczywistości, miary takie jak MIPS i MFLOPS mogą być także traktowane jako wskaźniki wydajności systemów obliczeniowych, ale ponieważ odnoszą się bezpośrednio do operacji wykonanych przez procesor, umieściłem je w kategorii procesorów.

-   Istnieją także inne, bardziej złożone miary wydajności, takie jak czasy odpowiedzi systemów, przepustowość, wydajność w rzeczywistych aplikacjach itp., ale te wymagają bardziej szczegółowego rozpatrzenia i często są specyficzne dla konkretnego zastosowania lub systemu.

## Prawo Moore'a i implikacje z niego wynikające w kontekście rozwoju sprzętu komputerowego

Prawo empiryczne, oparte na obserwacji, zakłada, że ekonomicznie optymalna ilość tranzystorów na układzie scalonym wzrasta w ciągu kolejnych lat zgodnie z wykładniczym trendem (podwajając się w niemal równych odstępach czasu). Prawo to jest przypisywane Gordonowi Moore'owi, jednemu z założycieli firmy Intel, który w 1965 roku zauważył, że **liczba tranzystorów podwajała się** co około 18 miesięcy. Później prawo zostało dostosowane, i obecnie uważa się, że liczba tranzystorów w mikroprocesorach podwaja się co około 24 miesiące. Analogicznie, zasada Moore'a jest również stosowana w odniesieniu do innych parametrów sprzętu komputerowego, takich jak pojemność dysków twardych czy wielkość pamięci operacyjnej.

To prawo jest kluczowym czynnikiem kształtującym rozwój sprzętu komputerowego i ma wiele ważnych implikacji:

-   **Wydajność**

    Prawo Moore'a oznacza, że nowe generacje procesorów i układów scalonych są zazwyczaj znacznie bardziej wydajne niż ich poprzednicy. To pozwala na rozwijanie bardziej zaawansowanych aplikacji, które wymagają większej mocy obliczeniowej.

-   **Miniaturyzacja**

    Aby zachować tempo zgodne z prawem Moore'a, producenci muszą zmniejszać rozmiary tranzystorów na układach scalonych. To prowadzi do coraz mniejszych i bardziej kompaktowych urządzeń elektronicznych, co jest szczególnie ważne w przypadku laptopów, smartfonów i innych przenośnych urządzeń.

-   **Innowacje w projektowaniu**

    Konieczność umieszczania coraz większej liczby tranzystorów na mniejszej przestrzeni wymaga ciągłego doskonalenia technik produkcji i projektowania układów scalonych. To z kolei pobudza innowacje w branży elektronicznej.

-   **Wzrost wydajności energetycznej**

    Przy zachowaniu tempa opisanego w prawie Moore'a, nowe generacje procesorów są zazwyczaj bardziej energooszczędne w porównaniu do poprzednich. To pozwala na wydłużenie życia baterii w urządzeniach przenośnych i zmniejszenie zużycia energii.

-   **Wpływ na rozwój oprogramowania**

    Wydajność nowych układów scalonych zgodnych z prawem Moore'a otwiera drzwi do tworzenia bardziej zaawansowanych i wymagających aplikacji. Programiści mogą wykorzystać dostępną moc obliczeniową do rozwoju bardziej zaawansowanych algorytmów i technologii.

-   **Wpływ na ekonomię**
    Prawo Moore'a ma wpływ na globalny rynek technologiczny. Firmy muszą inwestować znaczne środki w badania i rozwój, aby utrzymać tempo związanego z prawem Moore'a wzrostu mocy obliczeniowej. Jednocześnie konkurencja zachęca do innowacji i obniżania cen produktów.
