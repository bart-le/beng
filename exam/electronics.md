# PODSTAWY ELEKTRONIKI I TECHNIKI CYFROWEJ

## Implementacje podstawowych elementów pasywnych (rezystorów, kondensatorów i cewek)

### Rezystory

Rezystory są zwykle wykonane z materiałów o wysokim oporze, takich jak węgiel lub metal. W zależności od ich budowy mogą przyjmować różne kształty i rozmiary, ale często wyglądają jak małe cylindryczne elementy z drucikami na obu końcach. Ogranicza lub kontroluje przepływ prądu w obwodzie. Rezystory są używane do dzielenia napięcia w obwodach. Mają stałą wartość oporu, która jest mierzona w omach ($\Omega$).

#### Typy rezystorów

1. **Rezystory węglikowe**: Składają się z mieszanki węgla i żywicy i są jednymi z najczęściej używanych typów rezystorów. Są stosunkowo tanie, ale nie zawsze dokładne.
2. **Rezystory metalizowane**: Wykonane z cienkiej warstwy metalu nałożonej na podłoże ceramiczne. Są bardziej dokładne i stabilne termicznie od rezystorów węglikowych.
3. **Rezystory SMD (Surface Mount Device)**: Są mniejsze i przeznaczone do montażu powierzchniowego, często używane w miniaturyzowanych urządzeniach.

### Kondensatory

Kondensator składa się z dwóch przewodzących płyt rozdzielonych izolatorem nazywanym dielektrykiem. Dielektryk może być wykonany z różnych materiałów, takich jak papier, ceramika czy nawet powietrze. Kondensatory magazynują i uwalniają energię w postaci ładunku elektrycznego. Kondensatory są często używane w elektronice do stabilizacji napięcia, filtrowania czy w aplikacjach związanych z częstotliwością. Mają stałą pojemność, która jest mierzona w faradach (F).

#### Typy kondensatorów

1. **Kondensatory elektrolityczne**: Stosowane, gdy potrzebne są duże pojemności. Składają się z dwóch elektrod i elektrolitu.
2. **Kondensatory ceramiczne**: Małe, tanie i niepolarne, ale zazwyczaj o niskiej pojemności. Są szeroko stosowane w aplikacjach RF (Radio Frequency) i jako kondensatory dekuplujące.
3. **Kondensatory foliowe**: Składają się z cienkich warstw folii metalowej i dielektryka. Są stosowane w zastosowaniach, gdzie wymagana jest duża dokładność i stabilność.

### Cewki indukcyjne

Cewka to zazwyczaj drut miedziany nawinięty wokół rdzenia. Cewki magazynują energię w postaci pola magnetycznego. Gdy przez cewkę przepływa prąd, tworzy się wokół niej pole magnetyczne. Rdzeń może być wykonany z różnych materiałów, takich jak powietrze, żelazo czy ferryt. Mogą być używane do filtrowania sygnałów, w transformatorach do przenoszenia energii lub w obwodach radiowych do tworzenia rezonansów. Ich indukcyjność jest mierzona w henrach (H).

#### Typy cewek

1. **Cewki powietrzne**: Składają się z drutu nawiniętego wokół rdzenia powietrznego. Są stosunkowo proste, ale mogą być duże i nieefektywne w niektórych aplikacjach.
2. **Cewki ferrytowe**: Drut jest nawinięty na rdzeń z materiału ferrytowego, co zwiększa efektywność cewki.
3. **Cewki toroidalne**: Drut jest nawinięty wokół rdzenia w kształcie torusa (pączka). Są to cewki o wysokiej efektywności i niewielkich rozmiarach w porównaniu z innymi typami.

Wszystkie te elementy pasywne są niezbędne w projektowaniu i budowie układów elektronicznych. W zależności od aplikacji inżynierowie elektronicy wybierają odpowiednie typy i wartości tych komponentów, aby osiągnąć pożądane właściwości obwodu.

## Filtr dolnoprzepustowy RC, co to jest częstotliwość graniczna i pasmo przenoszenia filtru

Filtr dolnoprzepustowy RC (rezystor-kondensator) jest prostym rodzajem filtra elektronicznego, który przepuszcza sygnały o niskiej częstotliwości i tłumi sygnały o wysokiej częstotliwości. Jest zbudowany z rezystora (R) i kondensatora (C), połączonych w określonym układzie.

### Częstotliwość graniczna

Częstotliwość graniczna, nazywana również częstotliwością odcięcia, to punkt, w którym filtr zaczyna znacząco tłumić sygnały. Dla filtru dolnoprzepustowego RC, to jest częstotliwość, przy której amplituda sygnału wyjściowego spada do około 70,7% ($\frac{1}{\sqrt{2}}$) amplitudy sygnału wejściowego.

### Pasmo przenoszenia

Pasmo przenoszenia to zakres częstotliwości, w którym filtr efektywnie przepuszcza sygnał. Dla filtru dolnoprzepustowego, pasmo przenoszenia będzie zawierać częstotliwości od zera do częstotliwości granicznej. Sygnały o częstotliwościach wyższych niż częstotliwość graniczna będą tłumione.

W praktyce, opisując pasmo przenoszenia, często używa się też terminów jak "zakres stopnia tłumienia", który mówi o tym, jak skutecznie filtr tłumi sygnały o różnych częstotliwościach.

## Architektura harwardzka a architektura von Neumana

### Architektura von Neumana

-   **Jedna pamięć**: Stosuje jedną wspólną pamięć dla przechowywania danych i instrukcji.
-   **Sekwencyjne działanie**: Odczytywanie instrukcji i przetwarzanie danych odbywa się sekwencyjnie, co może spowalniać system.
-   **Uniwersalność**: Jest bardziej uniwersalna i stosowana w większości komputerów osobistych.

W tym modelu jest jedna pamięć, która przechowuje zarówno dane, jak i instrukcje. Procesor odczytuje instrukcje i dane z tej samej pamięci. To jest bardzo prosty i intuicyjny sposób organizacji, ale ma swoje ograniczenia.

Architektura von Neumana jest bardziej tradycyjna i jest używana w większości komputerów osobistych. W tym modelu, pamięć komputera jest używana zarówno do przechowywania danych, jak i instrukcji programu. Zatem, odczytanie i zapisywanie danych odbywa się w tej samej przestrzeni pamięci, co może prowadzić do pewnych ograniczeń, takich jak wąskie gardło przepustowości. Głównym ograniczeniem jest to, że odczytanie instrukcji i danych musi odbywać się sekwencyjnie, co może spowalniać komputer.

### Architektura Harwardzka

-   **Dwie pamięci**: Ma dwie oddzielne przestrzenie pamięci, jedną dla instrukcji, a drugą dla danych.
-   **Równoczesne działanie**: Możliwość jednoczesnego odczytywania instrukcji i operowania na danych, co zwykle zwiększa wydajność.
-   **Specjalizacja**: Często stosowana w systemach wbudowanych i innych specjalistycznych zastosowaniach, gdzie wydajność jest kluczowa.

Każda z tych architektur ma swoje miejsce i zastosowanie, ale wybór między nimi zależy od wymagań konkretnego projektu. Architektura von Neumana jest łatwiejsza do zrozumienia i implementacji, ale Harwardzka oferuje lepszą wydajność w specjalistycznych zastosowaniach.

## Sposoby obsługi zdarzeń w mikrokontrolerze

### Sondowanie (polling)

-   **Prosta metoda**: Mikrokontroler ciągle sprawdza stan wejść czy zmiennych, aby zobaczyć, czy zdarzenie miało miejsce.
-   **Brak efektywności**: Zajmuje dużo zasobów, ponieważ mikrokontroler jest zajęty ciągłym sprawdzaniem, zamiast wykonywania innych zadań.

### Przerwania (interrupts)

-   **Automatyczna reakcja**: Mikrokontroler jest informowany automatycznie, gdy zachodzi określone zdarzenie, dzięki czemu może natychmiastowo je obsłużyć.
-   **Wysoka efektywność**: Pozwala na oszczędność zasobów i czasu, gdyż mikrokontroler może wykonywać inne zadania pomiędzy przerwaniami.

### Programowanie zdarzeniowe (event-driven Programming)

-   **Kolejka zdarzeń**: Zdarzenia są dodawane do kolejki i obsługiwane w określonym czasie.
-   **Modularność**: Pozwala na bardziej modularny i łatwy do zarządzania kod.

### Timery

-   **Czasowe zdarzenia**: Mikrokontroler może wykonywać zadania w określonych odstępach czasu.
-   **Wielozadaniowość**: Możliwość jednoczesnego wykonywania różnych operacji w różnych odstępach czasu.

### Kontrolery DMA (Direct Memory Access)

-   **Bezpośredni dostęp do pamięci**: Automatyzuje transfer danych między pamięcią a urządzeniami peryferyjnymi.
-   **Oszczędność czasu CPU**: Pozwala na wykonywanie innych zadań przez CPU podczas transferu danych.

## Popularne interfejsy komunikacyjne w mikrokontrolerze

Interfejsy komunikacyjne w mikrokontrolerach odgrywają kluczową rolę w przesyłaniu danych między różnymi modułami czy urządzeniami. Każdy z tych interfejsów ma swoje unikalne cechy i zastosowania. Wybór odpowiedniego interfejsu zależy od wymagań konkretnego projektu, takich jak prędkość, odporność na zakłócenia czy łatwość implementacji.

### UART (Universal Asynchronous Receiver/Transmitter)

-   **Asynchroniczny**: Dane są przesyłane bez synchronizacji zegara.
-   **Łatwy w użyciu**: Najprostszy interfejs do implementacji, często używany w komunikacji z komputerem lub innymi prostymi urządzeniami.

### SPI (Serial Peripheral Interface)

-   **Synchroniczny**: Wymaga linii zegarowej do synchronizacji danych.
-   **Wysoka prędkość**: Może działać na znacznie wyższych prędkościach niż UART.
-   **Master-Slave**: Jeden urządzenie sterujące (master) i jedno lub więcej urządzeń podrzędnych (slave).

### I2C (Inter-Integrated Circuit)

-   **Synchroniczny**: Tak jak SPI, używa zegara do synchronizacji.
-   **Wielu uczestników**: Pozwala na komunikację między wieloma urządzeniami na tej samej magistrali.
-   **Adresowalność**: Każde urządzenie ma unikalny adres.

### CAN (Controller Area Network)

-   **Odporność na zakłócenia**: Stworzony do pracy w trudnych warunkach, często w pojazdach.
-   **Wiadomości**: Dane są przesyłane w formie wiadomości, a nie strumienia bajtów.

### USB (Universal Serial Bus)

-   **Wszechstronny**: Może służyć do przesyłania danych, ładowania baterii i innych funkcji.
-   **Wysoka prędkość**: Wersje jak USB 3.0 i wyżej oferują bardzo wysoką prędkość przesyłania danych.

### Ethernet

-   **Sieciowy interfejs**: Umożliwia komunikację w sieci LAN.
-   **Wysoka prędkość**: Może osiągnąć prędkości do 1 Gb/s lub więcej w nowszych wersjach.
