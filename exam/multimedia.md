# MULTIMEDIA

## Modele barw

### RGB

RGB działa na zasadzie addytywnej mieszanki kolorów. W tym modelu, kolory są reprezentowane przez połączenie trzech podstawowych kolorów: czerwonego, zielonego i niebieskiego.

1. **Współrzędne**:
    - R (Czerwony)
    - G (Zielony)
    - B (Niebieski)
2. **Zastosowanie**:
    - Ekran komputera, telewizja, fotografia cyfrowa, oświetlenie sceniczne
3. **Przykład**:
    - Jeśli mamy wartości R=255, G=0, B=0, otrzymamy czysty czerwony kolor.
4. **Wady i zalety**:
    - Zaleta: Prostota, szerokie zastosowanie
    - Wada: Niewielki gamut kolorów w porównaniu z rzeczywistością

### CMYK

Model subtraktywny, stosowany w drukarce. W praktyce, różne odcienie kolorów są uzyskiwane przez nałożenie różnych warstw tuszu.

1. **Współrzędne**:
    - C (Cyan)
    - M (Magenta)
    - Y (Yellow)
    - K (Key/Black)
2. **Zastosowanie**:
    - Druk, zarówno przemysłowy, jak i domowy
3. **Przykład**:
    - Druk ulotek, plakatów, broszur.
4. **Wady i zalety**:
    - Zaleta: Duża precyzja w kontekście drukowanego materiału
    - Wada: Ograniczony gamut kolorów, koszty

### HSV i HSL

Te modele percepcyjne są bardziej zorientowane na ludzkie postrzeganie kolorów i są często używane w narzędziach do edycji grafiki.

1. **Współrzędne**:
    - H (Barwa)
    - S (Nasycenie)
    - V/L (Wartość/Jasność)
2. **Zastosowanie**:
    - Edycja grafiki, programy do obróbki obrazów, web design
3. **Przykład**:
    - Aplikacje takie jak Adobe Photoshop używają modeli HSV/HSL w swoich narzędziach do edycji kolorów.
4. **Wady i zalety**:
    - Zaleta: Intuicyjność, elastyczność
    - Wada: Trudniejsze do zrozumienia dla początkujących

## Techniki cieniowania (shadery)

### Model oświetlenia Phonga

-   **Stałe** $k_a$, $k_d$, $k_s$ - Współczynniki określające własności materiału obiektu; zawierają się w przedziale $\left\langle0; 1\right\rangle$.
-   **$I_a$** - Intensywność światła otoczenia.
-   **$I_p$** - Intensywność światła padającego bezpośrednio od źródła.
-   **$I_s$** - Intensywność światła odbitego zwierciadlanie.
-   **$\alpha$** - Kąt między rzeczywistym kierunkiem odbicia a kierunkiem obserwacji.
-   **Formuła**: $I = k_a \cdot I_a + k_d \cdot I_p \cdot \cos{\theta} + k_s \cdot I_s \cdot \cos^n{\alpha}$

### Cieniowanie siatek wielokątowych

#### Cieniowanie wartością stałą (Flat shading)

-   **Charakterystyka**: Każda ściana ma jednolity kolor.
-   **Przeznaczenie**: Obiekty z ostrymi krawędziami.
-   **Wady**: Efekt Macha, czyli nagłe zmiany koloru na krawędziach.

#### Metoda Gourauda

-   **Charakterystyka**: Interpoluje kolory wierzchołków.
-   **Przeznaczenie**: Gładkie, matowe obiekty.
-   **Wady**: Może nieodpowiednio wygładzać pewne detale.

#### Model Phonga (Phong shading)

-   **Charakterystyka**: Interpoluje wektory normalne, nie kolory.
-   **Przeznaczenie**: Reprezentacja odbłysków i detali.
-   **Wady**: Nie uwzględnia wielu rzeczywistych efektów oświetleniowych.

## Metody kompresji w standardzie MPEG

Standard MPEG (Moving Picture Experts Group) wykorzystuje różnorodne techniki kompresji, aby zoptymalizować przechowywanie i przesyłanie plików multimedialnych. Każda wersja standardu MPEG (np. MPEG-1, MPEG-2, MPEG-4 itd.) może używać różnych kombinacji tych technik, dostosowanych do konkretnych zastosowań, takich jak strumieniowanie wideo czy przechowywanie filmów na dyskach DVD.

1. **Kompresja przestrzenna (spatial compression)**: Wykorzystuje techniki takie jak DCT (Dyskretna Transformata Kosinusowa), które zmieniają piksele na wartości frekwencyjne, łatwiejsze do kompresji.

2. **Kompresja czasowa (temporal compression)**: Polega na analizie różnic między kolejnymi klatkami. Zamiast przechowywać każdą klatkę oddzielnie, przechowuje się tylko różnice między nimi, co znacznie zmniejsza ilość danych.

3. **Predykcja Ruchu (motion prediction)**: Identyfikuje obiekty w sekwencji i oblicza ich ruch między klatkami, co pozwala na przechowywanie tylko informacji o ruchu zamiast całych obiektów.

4. **Kwantyzacja**: Proces zaokrąglania wartości, co prowadzi do utraty niektórych danych, ale znacząco zwiększa efektywność kompresji.

5. **Entropia i kodowanie Huffmana**: Używa statystyk występowania danych w celu ich efektywnego kodowania. Rzadziej występujące fragmenty otrzymują dłuższe kody, a częstsze – krótsze.

6. **Blokowe kompresje i makrobloki**: Obraz jest dzielony na małe bloki, a każdy z nich jest kompresowany oddzielnie, co ułatwia równoczesne kodowanie i dekodowanie.

7. **Multiplekowanie (muxing)**: Kombinuje skompresowane strumienie audio, wideo i metadanych w jednym pliku lub strumieniu.

8. **Psychoakustyczna i psychowizualna optymalizacja**: Usuwa dane, które są mniej prawdopodobnie zauważone przez ludzkie oko lub ucho, dzięki czemu można osiągnąć wyższy poziom kompresji.

## Efekt aliasingu i metody jego zwalczania, aliasing a częstotliwość próbkowania

### Aliasing

Zjawisko zakłóceń powstałych w wyniku dyskretyzacji sygnału, które są szczególnie widoczne w grafice komputerowej wykorzystującej przestrzeń o skończonej rozdzielczości. Zjawisko to jest efektem skończonej częstotliwości próbkowania, co oznacza, że sygnał jest analizowany w regularnych odstępach czasu, prowadząc do pojawienia się artefaktów. Jaskrawym przykładem aliasingu w grafice rastrowej jest efekt "schodkowy" wzdłuż rysowanych linii, szczególnie tych ukośnych.

### Metody Antyaliasingu

Częstotliwość próbkowania odgrywa kluczową rolę w powstawaniu efektu aliasingu. Zgodnie z twierdzeniem Nyquista-Shannona, minimalna częstotliwość próbkowania dla sygnału ciągłego powinna być co najmniej dwa razy większa od najwyższej częstotliwości sygnału, aby uniknąć aliasingu.

-   **Zwiększenie rozdzielczości**: Ta metoda nie eliminuje aliasingu, ale sprawia, że jest on mniej widoczny z pewnej odległości. Wady tego podejścia:

    -   Zwiększenie rozmiaru pamięci obrazu
    -   Wydłużenie czasu rysowania prymitywów
    -   Zwiększenie pasma pamięci i pasma monitora

-   **Metoda z dwoma pikselami w kolumnie**: Jest to rozszerzenie algorytmu Bresenhama, pozwalające na wybór dwóch pikseli do kolorowania zamiast jednego, gdy linia przechodzi między nimi. Odcień dla pikseli NE i E jest ustalany na podstawie długości odcinków [NE, Q] oraz [Q, E], gdzie suma odcieni pozostaje stała. Ta metoda jest efektywna, o ile urządzenie wyświetlające może reprezentować wiele odcieni szarości.

-   **Metoda bezwagowego próbkowania powierzchni**: Jest to metoda precyzyjna, szczególnie efektywna dla linii o grubości różnej od 1 piksela. Kolor (lub odcień) jest określany na podstawie tego, jaki procent powierzchni piksela pokrywa rysowany odcinek. Wymaga to wielobitowej reprezentacji piksela i ustawienia koloru dla kilku pikseli.

    -   **Nadpróbkowanie**: Aby uniknąć obliczeń pola powierzchni, piksel dzieli się na mniejsze jednostki (np. 16 mini-pikseli), a następnie oblicza się, jaki procent mini-pikseli pokrywa linia. Ten procent określa odcień dla całego piksela.

-   **Metoda wagowego próbkowania powierzchni**: Podobna do metody bezwagowego próbkowania, ale wprowadza dodatkowy element w postaci funkcji wagowej. Odcień piksela zależy nie tylko od pokrycia powierzchni, ale również od odległości od środka odcinka. Efekt jest podobny do rysowania stożkowym pisakiem.

### Algorytm Bresenhama

Algorytm Bresenhama jest techniką rysowania linii, okręgów i innych kształtów w grafice rastrowej. W kontekście linii, algorytm ten jest wykorzystywany do efektywnego wyboru pikseli na płaszczyźnie dwuwymiarowej tak, aby najlepiej aproksymować linię między dwoma punktami. Główne zalety tego algorytmu to jego wydajność i prostota. Nie wymaga on użycia arytmetyki zmiennoprzecinkowej, korzystając jedynie z dodawania, odejmowania i porównania.

## Zasady interakcji człowiek-komputer, heurystyka Nielsena-Molicha

Zasady interakcji człowiek-komputer (HCI) to zbiór wytycznych mających na celu zapewnienie efektywnego, satysfakcjonującego i użytecznego doświadczenia dla użytkowników korzystających z interfejsów komputerowych. Jednym z najbardziej znanych zestawów tych zasad jest heurystyka Nielsena-Molicha, która zawiera 10 podstawowych zasad zaprojektowanych tak, aby pomóc w ocenie użyteczności interfejsów. Zastosowanie tych zasad może znacznie poprawić użyteczność i ergonomię systemów komputerowych, co w konsekwencji prowadzi do zwiększenia satysfakcji i efektywności użytkowników.

1. **Widoczność statusu systemu**: System powinien zawsze informować użytkownika o tym, co się dzieje, poprzez odpowiednie komunikaty lub wskaźniki.

2. **Zgodność z rzeczywistością i systemem**: Interfejs powinien używać języka i konwencji znanych użytkownikowi, takich jak słowa, frazy i koncepty zrozumiałe dla docelowej grupy użytkowników.

3. **Minimalizacja obciążenia użytkownika**: Każda niepotrzebna operacja powinna być zminimalizowana lub wyeliminowana, aby ułatwić użytkownikowi realizację zamierzonych celów.

4. **Spójność i standardy**: Terminy i działania powinny być spójne w różnych częściach interfejsu.

5. **Zapobieganie błędom**: Lepiej zapobiegać błędom, niż polegać na ich późniejszym wykrywaniu i naprawie.

6. **Rozpoznawanie zamiast przypominania**: Obiekty i opcje powinny być widoczne i łatwo dostępne, tak aby użytkownicy nie musieli pamiętać informacji z innych części interfejsu.

7. **Elastyczność i efektywność użycia**: Interfejs powinien być tak zaprojektowany, aby był użyteczny zarówno dla nowych, jak i doświadczonych użytkowników.

8. **Estetyczny i minimalistyczny wygląd**: Interfejs powinien być wolny od nieistotnych elementów, które mogą odciągać uwagę użytkownika od głównego zadania.

9. **Pomoc użytkownikom w rozpoznaniu, diagnozowaniu i naprawie błędów**: Komunikaty o błędach powinny być jasne, precyzyjne i zawierać sugestie dotyczące ich rozwiązania.

10. **Dokumentacja i pomoc**: Pomoc i dokumentacja, jeżeli są dostępne, powinny być skierowane do rozwiązania problemów użytkownika, być łatwo dostępne i łatwe w użyciu.
