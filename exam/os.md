# SYSTEMY OPERACYJNE

## Klasyfikacja systemów operacyjnych

Systemy operacyjne mogą być klasyfikowane według różnych kryteriów, w tym czasu działania, architektury i interakcji z użytkownikiem.

### Według czasu działania

-   **Systemy czasu rzeczywistego**: Operują w ściśle określonych ramach czasowych, używane na przykład w samochodach czy systemach kontroli lotów.
-   **Systemy wsadowe**: Wykonują zadania w kolejności zdefiniowanej przez priorytety, zazwyczaj bez interakcji z użytkownikiem.
-   **Systemy interakcyjne**: Umożliwiają bezpośredni dialog z użytkownikiem i współbieżne wykonywanie różnych procesów.

### Według architektury

-   **Monolityczne**: Najprostsza forma, gdzie wszystkie zadania są wykonywane przez jądro.
-   **Warstwowe**: Posiadają hierarchiczną strukturę poleceń systemowych i mogą wykonywać wiele poleceń równocześnie.
-   **Klient-serwer**: Złożona architektura, w której serwer nadzoruje działanie podrzędnych systemów w sieci.
-   **Systemy równoległe**: Składają się z wielu procesorów, co umożliwia równoległe przetwarzanie danych.
-   **Systemy rozproszone**: Składają się z wielu komputerów połączonych w sieć, działających jako jedna jednostka.

### Według typu jądra

-   **Jądro monolityczne**: Wszystkie funkcje systemu operacyjnego są zawarte w jednym jądrze. Przykładem są różne wersje Unix.
-   **Mikrojądro**: Zawiera tylko podstawowe funkcje jak zarządzanie wątkami czy komunikacja międzyprocesowa. Przykłady to QNX, BeOS.
-   **Jądro hybrydowe**: Stanowi kompromis między jądrem monolitycznym a mikrojądrem, zawierając elementy obu.

### Inne kryteria

-   **Ze względu na interfejs**: Systemy tekstowe jak DOS, czy graficzne jak Windows.
-   **Ze względu na liczbę zadań**: Systemy jednozadaniowe jak DOS i wielozadaniowe jak Linux.
-   **Ze względu na przeznaczenie**: Mogą być przeznaczone dla użytku domowego, jako stacje robocze w sieci, lub jako serwery.

## Problem szeregowania procesów/wątków w systemach operacyjnych

Proces w kontekście systemów operacyjnych to instancja programu w trakcie wykonania, posiadająca własny licznik instrukcji oraz obszar w pamięci operacyjnej. Proces może być w jednym z kilku stanów: Nowy, Aktywny, Czekający, Gotowy, lub Zakończony. Struktura procesu jest złożona i kosztowna; zawiera segment kodu, stos, stertę i segment danych.

Wątek, czyli proces lekki, jest subkomponentem procesu. Wątki w ramach jednego procesu są wykonywane współbieżnie i mają wspólne zasoby, z wyjątkiem rejestru i stosu wywołań.

Planista jest systemowym procesem decydującym, który proces zostanie wykonany. Istnieją dwa typy planowania: niewywłaszczeniowe i wywłaszczeniowe. Ekspedytor jest odpowiedzialny za implementację decyzji planisty.

Kryteria jakości planowania procesów to wykorzystanie procesora, przepustowość, czas oczekiwania, czas obrotu i czas reakcji. Te kryteria są różnie ważne w różnych kontekstach zastosowań.

### Problemy szeregowania

Problem szeregowania procesów i wątków w systemach operacyjnych dotyczy efektywnego i sprawiedliwego przydzielania zasobów obliczeniowych do różnych procesów.

-   **Zagłodzenie (starvation)**: W systemach z planowaniem priorytetowym, procesy o niższym priorytecie mogą być nieustannie opóźniane, co prowadzi do ich zagłodzenia.

-   **Efekt "wąskiego gardła" (bottleneck)**: Niewłaściwe szeregowanie może spowodować, że pewne zasoby (np. procesor, dysk) są nadmiernie wykorzystywane, podczas gdy inne są marnowane.

-   **Nieefektywne wykorzystanie procesora**: Nieoptymalne strategie mogą prowadzić do niewykorzystania pełnej mocy obliczeniowej procesora.

-   **Ograniczona przepustowość**: Niewłaściwe szeregowanie może spowolnić tempo wykonania procesów, wpływając negatywnie na przepustowość systemu.

-   **Duże opóźnienia**: Niektóre strategie, takie jak Round-Robin, mogą wprowadzać duże opóźnienia w systemie z powodu częstego przełączania kontekstu.

-   **Efekt konwoju (convoy effect)**: W strategiach typu FCFS, krótkie zadania mogą czekać za dłuższymi, co opóźnia ich wykonanie.

-   **Złożoność implementacji**: Optymalne strategie, takie jak SRTF, są trudne do zaimplementowania i wymagają zaawansowanych algorytmów i metryk.

-   **Zmienność zasobów**: W systemach rozproszonych i chmurowych, zasoby mogą być dynamicznie przydzielane i zwalniane, co dodatkowo komplikuje problem szeregowania.

### Strategie szeregowania

-   **First-Come, First-Served (FCFS)**: Jest to jedna z najprostszych strategii. Procesy są obsługiwane w kolejności ich przybycia. Choć jest to łatwe do zaimplementowania, strategia ta jest podatna na "efekt konwoju", gdzie krótkie zadania czekają w kolejce za dłuższymi.

-   **Shortest Job First (SJF)**: W tej strategii, proces o najkrótszym czasie wykonania jest wybierany najpierw. Pomaga to w minimalizacji średniego czasu oczekiwania, ale jest trudne do zaimplementowania w praktyce, gdyż trudno jest z góry określić czas wykonania procesu.

-   **Shortest-Remaining-Time-First (SRTF)**: Jest to wersja SJF z wywłaszczaniem. Jeżeli w kolejce pojawia się proces o krótszym czasie wykonania niż obecnie wykonywany, obecny proces jest wstrzymywany. Chociaż jest to optymalne pod względem średniego czasu obrotu i oczekiwania, jest trudne do zaimplementowania i może prowadzić do zagłodzenia.

-   **Round-Robin (RR)**: Każdy proces w kolejce otrzymuje równy kwant czasu (tzw. "time slice") na wykonanie. Po upływie tego czasu, proces wraca na koniec kolejki. Jest to dobre dla systemów wieloużytkownikowych, ale może być nieefektywne, jeśli kwant czasu jest źle dobrany.

-   **Planowanie priorytetowe**: Procesy są wybierane na podstawie ich priorytetów. Wysoki priorytet oznacza szybsze przydzielenie zasobów. Problemem może być zagłodzenie procesów o niskim priorytecie, co można rozwiązać przez "starzenie" – zwiększanie priorytetu procesów, które czekają zbyt długo.

## Problem synchronizacji procesów/wątków w programach komputerowych oraz przedstaw jakie wsparcie w tym zakresie oferują systemy komputerowe i operacyjne

### Problemy synchronizacji

Problemy synchronizacji procesów i wątków obejmują kilka kluczowych wyzwań i ryzyk, które wymagają starannej analizy i zarządzania.

-   **Wyścig procesów (race condition)**: Występuje, gdy dwie lub więcej operacji są zależne od czasu i sekwencji wykonywania. Rezultat operacji jest nieprzewidywalny i może prowadzić do błędów.

-   **Zakleszczenie (deadlock)**: Stan, w którym dwa lub więcej procesów lub wątków czekają na zasoby, które są zablokowane przez siebie nawzajem. W tym przypadku żaden z nich nie może kontynuować działania.

-   **Wyglodzenie (starvation)**: Sytuacja, w której jeden lub więcej procesów są nieustannie pozbawiane dostępu do zasobów przez inne, bardziej priorytetowe procesy.

-   **Inwersja priorytetu (priority inversion)**: Występuje, gdy proces o niższym priorytecie zajmuje zasób, którego potrzebuje proces o wyższym priorytecie, co prowadzi do opóźnień.

-   **Nieatomowość operacji**: Problemy związane z operacjami, które są podzielone na kilka etapów i mogą być przerwane, co prowadzi do niekonsekwentnych stanów systemu.

-   **Spójność danych**: Obejmuje trudności z utrzymaniem aktualności i spójności danych, gdy są one modyfikowane przez wiele procesów lub wątków.

-   **Niedeterminizm**: Problemy wynikające z trudności w przewidywaniu sekwencji wykonywania wątków i procesów, co utrudnia debugowanie i testowanie.

-   **Złożoność zarządzania**: Im więcej mechanizmów synchronizacji jest używanych, tym trudniejsze staje się zarządzanie systemem i zapewnienie jego niezawodności.

-   **Narzuty systemowe**: Mechanizmy synchronizacji wprowadzają dodatkowe obciążenie dla systemu, co może wpłynąć na wydajność.

### Mechanizmy synchronizacji w systemach komputerowych i operacyjnych

-   **Semafory**: Są to zmienne lub abstrakcyjne typy danych, które są używane do sterowania dostępem do zasobu. Dwa podstawowe rodzaje to semafory binarne i zliczające.

-   **Mutexy (Mutual Exclusion Locks)**: To bardziej specjalizowany typ binarnego semafora, który zapewnia wzajemne wykluczenie. Stosowany, gdy tylko jeden wątek na raz może mieć dostęp do zasobu.

-   **Zmienne warunkowe**: Umożliwiają wątkom czekanie na spełnienie pewnego warunku przed kontynuacją wykonywania.

-   **Monitory**: To abstrakcyjne typy danych lub klasy obiektów, które kapsułkują metody i zmienne warunkowe w jednym obiekcie, zapewniając tym samym bezpieczny dostęp do zasobów.

-   **Komunikacja międzyprocesowa (IPC)**: Takie mechanizmy jak kolejki komunikatów, gniazda oraz potoki są używane do synchronizacji i komunikacji między różnymi procesami.

-   **Transakcje**: Oferują atomowość i izolację w działaniach, szczególnie w systemach baz danych, ale również w innych rodzajach aplikacji.

-   **API specyficzne dla języka**: Współczesne języki programowania, takie jak Java czy C#, oferują wbudowane klasy i metody dla zarządzania synchronizacją.

-   **Sprzętowe wsparcie**: Niekiedy synchronizacja jest wspierana na poziomie sprzętu, jak np. w architekturach wieloprocesorowych przez użycie instrukcji atomowych.

-   **Planowanie i szeregowanie**: Systemy operacyjne mogą oferować różne polityki szeregowania, które mogą być wykorzystane do zarządzania dostępem do zasobów w sposób bardziej zaawansowany.

-   **Rozszerzenia i biblioteki**: Istnieją różne biblioteki i narzędzia, które oferują dodatkowe mechanizmy synchronizacji, takie jak tzw. read-write locks, czy semafory nazwane.

## Mechanizmy obsługi pamięci operacyjnej wykorzystywane w systemach operacyjnych

-   **Podział pamięci (memory partitioning)**: Pamięć jest podzielona na segmenty, do których przydzielane są różne procesy. Podział może być stały lub dynamiczny.

-   **Paginacja (paging)**: Pamięć fizyczna jest podzielona na jednostki o stałym rozmiarze, nazywane stronami. Procesy są dzielone na strony i ładowane do dostępnych stron w pamięci fizycznej.

-   **Segmentacja (segmentation)**: Pamięć jest podzielona na segmenty różnych rozmiarów, które są dynamicznie przydzielane procesom. Każdy segment ma różne atrybuty takie jak prawa dostępu.

-   **Pamięć wirtualna (virtual memory)**: Mechanizm, który umożliwia procesom korzystanie z więcej pamięci, niż jest fizycznie dostępna, przez przechowywanie części danych na dysku twardym.

-   **Buforowanie i cache**: System operacyjny utrzymuje bufor lub pamięć podręczną dla często używanych danych, co zmniejsza czas dostępu do tych danych.

-   **Zarządzanie pamięcią w procesorach wielordzeniowych (multi-core memory management)**: Mechanizmy takie jak coherency i lokalność są używane do optymalizacji zarządzania pamięcią w systemach wielordzeniowych.

-   **Strategie wymiany (swapping strategies)**: Algorytmy takie jak LRU (Least Recently Used), FIFO (First-In, First-Out) i inne są używane do zarządzania przestrzenią w pamięci.

-   **Alokatory pamięci**: Zarządzają dynamicznym przydzielaniem i zwalnianiem pamięci w czasie wykonywania programu.

-   **Ochrona pamięci (memory protection)**: Mechanizmy takie jak bit ochrony, strony tylko do odczytu i przestrzenie adresowe są używane do zapobiegania nieautoryzowanemu dostępowi do pamięci.

-   **Równoczesny dostęp (concurrency control)**: Mechanizmy takie jak blokady i semafory są używane do synchronizacji dostępu do pamięci współdzielonej przez różne procesy.

-   **Odzyskiwanie pamięci (garbage collection)**: W niektórych systemach operacyjnych i językach programowania, automatyczne mechanizmy są używane do odzyskiwania nieużywanej pamięci.

## Istota mechanizmu pamięci wirtualnej, wady i zalety tego rozwiązania

Pamięć wirtualna to mechanizm zarządzania pamięcią, który decouples fizyczne i logiczne widoki pamięci. W praktyce oznacza to, że programy mogą korzystać z większej ilości pamięci niż fizycznie dostępna w systemie. Działa to na zasadzie przechowywania części danych na dysku twardym w specjalnym obszarze zwanym "plikiem stronicowania". Kiedy proces potrzebuje dostępu do danych, które nie są obecnie w pamięci RAM, system operacyjny przenosi odpowiednie dane z dysku do RAM, zastępując mniej ważne lub rzadko używane dane.

### Zalety pamięci wirtualnej

-   **Elastyczność**: Umożliwia uruchamianie większej liczby lub bardziej złożonych aplikacji jednocześnie, nawet jeżeli fizyczna pamięć RAM jest ograniczona.

-   **Izolacja procesów**: Każdy proces ma własną przestrzeń adresową, co ułatwia izolację i zabezpieczenie procesów przed wzajemnym wpływem.

-   **Uproszczenie programowania**: Programiści mogą skupić się na logice aplikacji, nie martwiąc się o ograniczenia fizycznej pamięci.

-   **Wydajność**: Możliwość wykorzystania różnych algorytmów do zarządzania stronicą, takich jak LRU, co może zwiększyć ogólną wydajność systemu.

-   **Zgodność wsteczna**: Starsze aplikacje, które nie są świadome dużych pojemności pamięci, mogą działać efektywniej w systemach z pamięcią wirtualną.

### Wady pamięci wirtualnej

-   **Opóźnienia (latency)**: Przenoszenie danych między dyskiem a pamięcią RAM może być czasochłonne, co wpływa na wydajność.

-   **Złożoność**: Algorytmy zarządzania stronicą i wybór strategii wymiany mogą być złożone i trudne do optymalizacji.

-   **Narzut systemowy**: Zarządzanie pamięcią wirtualną wymaga dodatkowych zasobów systemowych, takich jak CPU i pamięć, co może wpływać na ogólną wydajność systemu.

-   **Ryzyko fragmentacji**: Użycie pliku stronicowania może prowadzić do fragmentacji dysku, co dodatkowo obniża wydajność.

-   **Trudności w diagnostyce**: Problemy z wydajnością mogą być trudniejsze do zdiagnozowania i rozwiązania, gdyż warstwa abstrakcji pamięci wirtualnej komplikuje analizę.
