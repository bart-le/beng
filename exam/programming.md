# METODY PROGRAMOWANIA, ZAGADNIENIA PODSTAWOWE

## Konstrukcja obiektów i zarządzanie pamięcią operacyjną w Javie i C++

### Java

W Javie pamięć operacyjna jest zarządzana automatycznie przez mechanizm zwany Garbage Collectorem (GC). Programiści nie muszą ręcznie alokować ani zwalniać pamięci, ponieważ GC śledzi obiekty, które nie są już używane, i usuwa je, zwalniając zasoby. Kiedy obiekt nie jest już używany (np. nie ma do niego referencji), Garbage Collector automatycznie go usuwa, zwalniając zasoby.

W Javie obiekty są tworzone za pomocą słowa kluczowego `new`.

```java
// Tworzenie nowego obiektu klasy MyClass
MyClass obj = new MyClass();
```

### C++

W C++ programista jest odpowiedzialny za zarządzanie pamięcią operacyjną. Alokacja i dealokacja pamięci odbywają się ręcznie za pomocą operatorów `new` i `delete` lub za pomocą biblioteki takiej jak `std::shared_ptr` lub `std::unique_ptr` w przypadku C++ 11 i nowszych standardów.

W C++ obiekty są tworzone za pomocą operatora `new` lub bezpośrednio na stosie.

```cpp
// Tworzenie obiektu za pomocą operatora new
MyClass* obj = new MyClass();

// Tworzenie obiektu na stosie
MyClass obj2;
```

Programista musi ręcznie zwolnić pamięć operacyjną zajmowaną przez obiekt, używając operatora `delete` w przypadku obiektów stworzonych za pomocą `new`.

```cpp
// Tworzenie obiektu za pomocą operatora new
MyClass* obj = new MyClass();

// Usuwanie obiektu i zwalnianie pamięci
delete obj;
```

W przypadku obiektów na stosie, pamięć zostanie automatycznie zwolniona po wyjściu z zakresu, w którym obiekt został zadeklarowany.

```cpp
#include <iostream>
using namespace std;

class MyClass
{
    public:
        MyClass(const string &msg): message(msg) {}

    void outputMessage()
    {
        cout << message << endl;
    }

    private:
        string message;
};

int main()
{
    MyClass obj("Hello, World!");

    obj.outputMessage();

    return 0;
}
```

## Rola klas, interfejsów i mixinów w programowaniu na przykładzie języka Java

### Klasy

Klasa jest podstawowym elementem obiektowym w wielu językach programowania, w tym w Javie. Definiuje ona "szablon", według którego tworzone są obiekty.

-   **Enkapsulacja**: Klasy skupiają dane i metody w jednej jednostce, chroniąc wewnętrzny stan obiektu przed nieautoryzowanym dostępem za pomocą modyfikatorów dostępu (`private`, `protected`, `public`).
-   **Dziedziczenie**: Klasa może dziedziczyć właściwości i metody z innej klasy, co pozwala na wielokrotne użycie kodu.
-   **Konstruktory**: Specjalne metody w klasie, które inicjalizują nowy obiekt.

```java
public class Student {
    private String name;
    private int yearOfStudy;

    public Student(String name, int yearOfStudy) {
        this.name = name;
        this.yearOfStudy = yearOfStudy;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getYearOfStudy() {
        return yearOfStudy;
    }

    public void setYearOfStudy(int yearOfStudy) {
        this.yearOfStudy = yearOfStudy;
    }

    @Override
    public String toString() {
        return String.format("Student{name='%s', yearOfStudy=%d}", name, yearOfStudy);
    }
}
```

### Interfejsy

W Javie, interfejsy definiują umowę lub kontrakt, który implementujące je klasy muszą przestrzegać.

-   **Deklaracja metod**: Interfejsy mogą deklarować metody, ale nie mogą zawierać ich implementacji (choć od Javy 8 mogą zawierać metody domyślne z implementacją).
-   **Wielodziedziczenie**: Java nie pozwala na wielodziedziczenie klas, ale klasa może implementować wiele interfejsów, co umożliwia formę wielodziedziczenia.
-   **Abstrakcja**: Umożliwiają tworzenie kodu, który działa na poziomie abstrakcji, a nie konkretnych implementacji.

```java
public interface Study {
    void read();
    void takeExam();
}

public class Undergraduate implements Study {
    @Override
    public void read() {
        System.out.println("Being focused makes me look smarter.");
    }

    @Override
    public void takeExam() {
        System.out.println("Let's hope that I'll get the easy questions.");
    }
}
```

### Mixiny

Termin "mixin" nie jest bezpośrednio używany w kontekście języka Java, ale koncepcja jest związana z możliwością dodawania funkcjonalności do klas bez konieczności dziedziczenia. W Javie, mixinów można do pewnego stopnia symulować za pomocą interfejsów. Użycie mixinów w Javie za pomocą interfejsów z metodami domyślnymi pozwala na dodawanie dodatkowej funkcjonalności do klas bez konieczności dziedziczenia z innych klas.

-   **Interfejsy z metodami domyślnymi**: Od Javy 8, interfejsy mogą zawierać metody domyślne, które dostarczają domyślną implementację. Dzięki temu klasy mogą "mieszać" funkcjonalności z wielu interfejsów.
-   **Nie jest to czysty mixin**: W czystej formie, mixin pozwala na tworzenie klas, które mogą być używane do dodawania funkcjonalności do innych klas w sposób bardziej dynamiczny.

```java
public interface Work {
    default void writeCringeLinkedInPost() {
        System.out.println("Something about cold showers and waking up at 5AM.");
    }
}

public class GraduateStudent implements Study, Work {
    @Override
    public void read() {
        System.out.println("Enough already.");
    }

    @Override
    public void takeExam() {
        System.out.println("Not again.");
    }

    public void sendResume() {
        writeCringeLinkedInPost();
    }
}
```

## Pojęcie dziedziczenia na przykładzie języków Java i C++

Dziedziczenie to kluczowy koncept programowania obiektowego, który pozwala na tworzenie nowych klas na podstawie istniejących klas. Pozwala to na reużywanie kodu, rozszerzanie funkcjonalności istniejących klas oraz tworzenie hierarchii klas.

### Java

W Javie dziedziczenie jest realizowane za pomocą słowa kluczowego `extends`. W Javie każda klasa może dziedziczyć tylko po jednej klasie (nie ma wielodziedziczenia dla klas), ale może implementować wiele interfejsów. Wyjątkiem jest klasa o modyfikatorze `final`, która nie może być rodzicem jakiejkolwiek innej klasy.

Klasa `Student` dziedziczy po klasie `Person` i rozszerza jej funkcjonalność o możliwość studiowania.

```java
class Person {
    String name;

    Person(String name) {
        this.name = name;
    }

    void introduce() {
        System.out.println("My name is " + name + ".");
    }
}

class Student extends Person {
    int yearOfStudy;

    Student(String name, int yearOfStudy) {
        super(name);
        this.yearOfStudy = yearOfStudy;
    }

    void study() {
        System.out.println(name + " is studying.");
    }
}
```

### C++

W C++ dziedziczenie może być publiczne (`public`), chronione (`protected`) lub prywatne (`private`). W tym przypadku, podobnie jak w Javie, są klasy `Person` i `Student`, gdzie `Student` dziedziczy po klasie `Person`.

```cpp
#include <iostream>
#include <string>

class Person
{
    public:
        std::string name;

    Person(std::string n): name(n) {}

    void introduce()
    {
        std::cout << "My name is " << name << "." << std::endl;
    }
};

class Student: public Person
{
    public: int yearOfStudy;

    Student(std::string name, int year): Person(name), yearOfStudy(year) {}

    void study()
    {
        std::cout << name << " is studying." << std::endl;
    }
};
```

W C++ możliwe jest także wielodziedziczenie, czyli dziedziczenie po wielu klasach na raz.

```cpp
class Worker
{
    public:
        void work()
        {
            std::cout << "Working..." << std::endl;
        }
};

class WorkingStudent: public Person, public Worker
{
    public: WorkingStudent(std::string name): Person(name) {}
};
```

## Istota i zastosowania polimorfizmu na przykładzie języków Java i C++

W programowaniu polimorfizm odnosi się do zdolności obiektów różnych klas do bycia traktowanymi jak obiekty wspólnej klasy nadrzędnej.

### Typy polimorfizmu

1. **Statyczny polimorfizm (czas kompilacji)**: Jest zaimplementowany przy użyciu przeciążenia funkcji i operatorów. Odnosi się do sytuacji, gdy funkcja jest ewaluowana na podstawie typów argumentów w czasie kompilacji.
2. **Dynamiczny polimorfizm (czasu wykonania)**: Jest zaimplementowany przy użyciu dziedziczenia i wskaźników. Odnosi się do sytuacji, gdy dokładna funkcja, która ma być wywołana, jest decydowana w czasie wykonywania programu.

### Zastosowania polimorfizmu

-   Wspiera modularność oraz rozdzielenie odpowiedzialności w programach.
-   Umożliwia rozszerzanie istniejących bibliotek kodu bez modyfikowania istniejącego kodu.
-   Umożliwia implementowanie metod zewnętrznych bez konieczności modyfikowania oryginalnej klasy.

### Java

```java
abstract class UniversityMember {
    public abstract void showRole();
}

class Student extends UniversityMember {
    @Override
    public void showRole() {
        System.out.println("I am a student.");
    }
}

class Professor extends UniversityMember {
    @Override
    public void showRole() {
        System.out.println("I am a professor.");
    }
}

public class UniversityDemo {
    public static void main(String[] args) {
        UniversityMember member1 = new Student();
        UniversityMember member2 = new Professor();

        member1.showRole();
        member2.showRole();
    }
}
```

### C++

```cpp
#include <iostream>

class UniversityMember
{
    public:
        virtual void showRole()
        {
            std::cout << "I am a university member." << std::endl;
        }
};

class Student: public UniversityMember
{
    public: void showRole()
    {
        std::cout << "I am a student." << std::endl;
    }
};

class Professor: public UniversityMember
{
    public: void showRole()
    {
        std::cout << "I am a professor." << std::endl;
    }
};

int main()
{
    UniversityMember *member1 = new Student();
    UniversityMember *member2 = new Professor();

    member1->showRole();
    member2->showRole();

    delete member1;
    delete member2;

    return 0;
}
```

W obu przykładach jest klasa bazowa `UniversityMember` oraz dwie klasy dziedziczące: `Student` i `Professor`. Dzięki polimorfizmowi istnieje możliwość używania wskaźnika (lub referencji) typu `UniversityMember` do wywołania odpowiedniej metody `showRole` dla obiektu typu `Student` lub `Professor`.

## Użycie tablic oraz innych struktur danych w Javie i C++, Java Collections Framework

Zarówno Java Collections Framework, jak i C++ Standard Template Library oferują różnorodne struktury danych zoptymalizowane do różnych zastosowań. Kluczem jest wybór odpowiedniej struktury danych dla konkretnego problemu.

### Java

#### Tablice

To są podstawowe struktury danych, które przechowują elementy tego samego typu.

```java
// Inicjalizacja 3-elementowej tablicy liczb całkowitych
int[] numbers = new int[3];

 // Przypisanie wartości do pierwszego elementu
numbers[0] = 1;
```

#### Java Collections Framework

Jest to zbiór klas i interfejsów, które implementują powszechnie używane struktury danych.

##### Listy (interfejs `List`)

Struktura danych typu kolekcja, w której elementy są uporządkowane.

```java
List<String> list = new ArrayList<>();

list.add("student");
```

##### Zbiory (interfejs `Set`)

Kolekcja, która nie dopuszcza duplikatów.

```java
Set<String> set = new HashSet<>();

set.add("student");
```

##### Mapy (interfejs `Map`)

Kolekcja, która przechowuje pary klucz-wartość.

```java
Map<String, Integer> map = new HashMap<>();

map.put("John", 1337);
```

##### Kolejki (interfejs `Queue`)

Kolekcja służąca do przechowywania elementów w kolejności FIFO (First-In-First-Out).

```java
Queue<String> queue = new LinkedList<>();

queue.offer("student");
```

#### Stosy (klasa `Stack`)

Kolekcja typu LIFO (Last-In-First-Out).

```java
Stack<String> stack = new Stack<>();

stack.push("student");
```

### C++

Tak samo jak w Javie, tablice w C++ przechowują elementy tego samego typu.

#### Tablice

```cpp
// Inicjalizacja 3-elementowej tablicy liczb całkowitych
int numbers[3];

// Przypisanie wartości do pierwszego elementu
numbers[0] = 1;
```

#### Standard Template Library

To kolekcja klas C++, które dostarczają kilka zintegrowanych struktur danych.

##### Vector (`<vector>`)

```cpp
#include <vector>

std::vector<int> vec;

vec.push_back(1);
```

##### Set (`<set>`)

```cpp
#include <set>

std::set<int> s;

s.insert(1);
```

##### Map (`<map>`)

```cpp
#include <map>

std::map<std::string, int> m;

m["John"] = 1337;
```

##### Queue (`<queue>`)

```cpp
#include <queue>

std::queue<int> q;

q.push(1);
```

##### Stack (`<stack>`)

```cpp
#include <stack>

std::stack<int> st;

st.push(1);
```

## Programowanie współbieżne, mechanizmy i narzędzia na przykładzie języka Java

Programowanie współbieżne w Javie oferuje wiele mechanizmów i narzędzi do tworzenia aplikacji współbieżnych, ale również przynosi wiele wyzwań związanych z zagadnieniami takimi jak wyścigi (race conditions), zakleszczenia (deadlocks) czy warunki wyścigowe (race hazards). Dlatego ważne jest dokładne zrozumienie mechanizmów współbieżności oraz odpowiednie testowanie kodu, aby poprawić wydajność i lepiej wykorzystać wielordzeniowe procesory.

-   **Wątek (Thread):** Najmniejsza jednostka wykonawcza w programie. W Java każdy wątek jest reprezentowany przez obiekt klasy `Thread`.
-   **Proces:** Niezależna jednostka wykonawcza posiadająca własną przestrzeń adresową. Wątki w obrębie tego samego procesu dzielą tę samą przestrzeń pamięci.

### Klasa `Thread`

Można tworzyć nowy wątek przez dziedziczenie z klasy `Thread` i przesłonięcie metody `run()`.

```java
class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Thread is running");
    }
}

MyThread t = new MyThread();
t.start();
```

### Interfejs `Runnable`

Alternatywny sposób tworzenia wątków bez konieczności dziedziczenia z klasy `Thread`.

```java
class MyRunnable implements Runnable {
    @Override
    public void run() {
        System.out.println("Runnable is running");
    }
}

Thread t = new Thread(new MyRunnable());
t.start();
```

### Synchronizacja

Istnieją różne mechanizmy synchronizacji w Javie, takie jak `synchronized` metod, bloków synchronizowanych i klas `ReentrantLock` oraz `ReentrantReadWriteLock`.

```java
public class Counter {
    private int value = 0;

    public synchronized void increment() {
        value++;
    }

    public synchronized int getValue() {
        return value;
    }
}
```

### Interfejsy `Future` i `Callable`

`Future` reprezentuje wynik obliczeń asynchronicznych. Jest to sposób na uzyskanie wyniku działania wątku w przyszłości. `Callable` to funkcjonalny interfejs, który jest podobny do `Runnable`, ale może zwrócić wartość lub zgłosić wyjątek. Umożliwiają tworzenie zadań, które można wykonywać asynchronicznie i które mogą zwracać wynik.

```java
import java.util.concurrent.*;

public class FutureCallableExample {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newFixedThreadPool(1);

        Callable<String> callableTask = () -> {
            TimeUnit.SECONDS.sleep(1);
            return "Callable result";
        };

        Future<String> future = executor.submit(callableTask);

        while (!future.isDone()) {
            System.out.println("Waiting...");
            TimeUnit.MILLISECONDS.sleep(100);
        }

        String result = future.get();
        System.out.println(result);

        executor.shutdown();
    }
}
```

### Executor Framework

Zamiast ręcznego tworzenia wątków, Java oferuje ramy wykonawcze, które zarządzają pulą wątków. Najpopularniejsze klasy to `ThreadPoolExecutor` i `Executors`.

```java
ExecutorService executorService = Executors.newFixedThreadPool(3);

executorService.execute(() -> System.out.println("Executing task in thread pool."));
executorService.shutdown();
```

### Klasy współbieżności z pakietu `java.util.concurrent`

Java oferuje wiele zaawansowanych narzędzi do programowania współbieżnego, takich jak semafory, bariery cykliczne, zamek CountDownLatch i wiele innych.

### Kolekcje współbieżne

Java posiada kolekcje zoptymalizowane pod kątem współbieżności, takie jak `ConcurrentHashMap`, `CopyOnWriteArrayList` i `ConcurrentLinkedQueue`.

```java
ConcurrentMap<String, String> map = new ConcurrentHashMap<>();

map.put("key", "value");
```

### Atomic Variables

W Javie istnieją klasy, takie jak `AtomicInteger` czy `AtomicReference`, które zapewniają atomowe operacje na pojedynczych zmiennych, co jest przydatne w programowaniu współbieżnym. Są one alternatywą dla volatile i synchronized w niektórych przypadkach.

```java
AtomicInteger atomicInt = new AtomicInteger(0);

int incrementedValue = atomicInt.incrementAndGet();
```

### Volatile

Słowo kluczowe `volatile` zapewnia, że zmienne są czytane bezpośrednio z pamięci głównej, a nie z pamięci podręcznej wątku. Gwarantuje ono widoczność zmian zmiennej przez wszystkie wątki.

```java
public class SharedResource {
    private volatile boolean flag = true;

    public boolean isFlag() {
        return flag;
    }

    public void setFlag(boolean flag) {
        this.flag = flag;
    }
}
```

## Typy i metody sparametryzowane (generics) w Javie, szablony (templates) w C++

Generics w Javie i szablony w C++ mają podobne cele, ale są realizowane w różny sposób w obu językach. Głównym celem obu mechanizmów jest zapewnienie mechanizmów reużywalności kodu w bezpieczny sposób, ale zachowując przy tym typowanie statyczne.

### Porównanie

-   **Bezpieczeństwo typów**: Zarówno generics w Javie, jak i szablony w C++ zapewniają bezpieczeństwo typów w czasie kompilacji, co pomaga unikać błędów w czasie wykonania.

-   **Implementacja**: Generics w Javie są realizowane za pomocą typu erasure, co oznacza, że informacje o typach sparametryzowanych są usuwane w czasie kompilacji. W C++, każda instancja szablonu jest kompilowana do osobnego kodu binarnego dla każdego używanego typu.

-   **Ograniczenia**: W Javie możemy definiować ograniczenia dla typów sparametryzowanych (np. `T extends Number`), co nie jest możliwe w C++ w taki sam sposób.

### Java

Typy sparametryzowane (czyli generics) w Javie umożliwiają tworzenie klas, interfejsów i metod z typem, który jest określany w momencie tworzenia instancji klasy lub wywołania metody.

#### Klasa generyczna

```java
public class Box<T> {
    private T item;

    public void set(T item) {
        this.item = item;
    }

    public T get() {
        return item;
    }
}

Box<String> stringBox = new Box<>();

stringBox.set("Hello, World!");
String value = stringBox.get();
```

#### Metoda generyczna

```java
public class Utility {
    public static <T> void print(T item) {
        System.out.println(item);
    }
}

Utility.print("Hello, World!");
Utility.print(1337);
```

### C++

Szablony w C++ pozwalają na definiowanie funkcji i klas, które pracują na ogólnych typach, co umożliwia reużywalność kodu.

#### Szablon funkcji

```cpp
template <typename T>
    T getMax(T a, T b)
    {
        return (a > b) ? a : b;
    }

int main()
{
    cout <<getMax<int> (13, 37);
    cout <<getMax<double> (1.3, 3.7);
}
```

#### Szablon klasy

```cpp
template <typename T>
    class Box
    {
        public:
            Box(T val): value(val) {}

        T getValue()
        {
            return value;
        }

        void setValue(T val)
        {
            value = val;
        }

        private:
            T value;
    };

int main()
{
    Box<string> stringBox("Hello, World!");
    Box<int> intBox(1337);

    cout << stringBox.getValue();
    cout << intBox.getValue();
}
```

## Lambda-wyrażenia i interfejsy funkcyjne w języku Java

Lambda-wyrażenia i interfejsy funkcyjne to ważne funkcje wprowadzone w Javie 8, które zrewolucjonizowały sposób pisania kodu, czyniąc go bardziej zwięzłym, czytelnym i funkcyjnym.

### Lambda-wyrażenia

Lambda-wyrażenie to krótka blokowa forma reprezentowania obiektu jednej metody. To wyrażenie można przekazać do metody jako argument, co jest szczególnie przydatne w operacjach na strumieniach oraz przy programowaniu reaktywnym.

#### Składnia

```java
(args) -> { body }
```

##### Bez argumentów

```java
() -> System.out.println("Hello, World!");
```

##### Z jednym argumentem

Nawiasy są opcjonalne.

```java
x -> x * x
```

##### Z wieloma argumentami

```java
(x, y) -> x + y
```

### Interfejsy funkcyjne

Interfejs funkcyjny to interfejs, który posiada tylko jedną abstrakcyjną metodę (może posiadać też inne metody domyślne lub statyczne). Dzięki temu, że ma tylko jedną metodę, można go reprezentować za pomocą lambda-wyrażenia.

Java 8 wprowadziła wiele wbudowanych interfejsów funkcyjnych w pakiecie `java.util.function`. Najczęściej używane z nich to:

-   `Predicate<T>`: reprezentuje predykat (warunek) jednego argumentu typu `T`.
-   `Function<T, R>`: reprezentuje funkcję przyjmującą argument typu `T` i zwracającą `R`.
-   `Consumer<T>`: reprezentuje operację na jednym argumencie typu `T` bez wyniku.
-   `Supplier<T>`: reprezentuje dostawcę wyników typu `T`.

```java
import java.util.*;
import java.util.function.Predicate;
import java.util.stream.Collectors;

class Student {
    private String name;
    private double grade;

    public Student(String name, double grade) {
        this.name = name;
        this.grade = grade;
    }

    public String getName() {
        return name;
    }

    public double getGrade() {
        return grade;
    }

    public boolean hasPassed(double passingGrade) {
        return grade >= passingGrade;
    }

    @Override
    public String toString() {
        return String.format("Student{name='%s', grade=%.2f}", name, grade);
    }

    public static void main(String[] args) {
        List <Student> students = Arrays.asList(
            new Student("Leonardo", 5.0),
            new Student("Raphael", 4.2),
            new Student("Donatello", 5.9),
            new Student("Michelangelo", 3.1)
        );

        Predicate<Student> passedPredicate = student -> student.hasPassed(5.0);
        List<Student> nerds = students.stream()
            .filter(passedPredicate)
            .collect(Collectors.toList());

        nerds.forEach(System.out::println);
    }
}
```

Uruchomienie kodu, wyświetla listę studentów, którzy zdali (czyli osiągnęli ocenę 5.0 lub wyższą). Lambda-wyrażenia i interfejsy funkcyjne, jak w tym przypadku Predicate<Student>, uczyniły filtrację listy studentów bardziej zwięzłą i czytelną.

## Przetwarzanie strumieniowe (środki pakietu java.util.stream)

Przetwarzanie strumieniowe to jeden z najważniejszych dodatków do języka Java wprowadzonych w Java 8. Umożliwia ono deklaratywne przetwarzanie kolekcji danych w sposób bardziej czytelny i zoptymalizowany. Strumienie w Javie są mocno inspirowane funkcjonalnym podejściem do przetwarzania danych.

Podstawowe koncepcje przetwarzania strumieniowego w Javie:

1. **Strumień**: W środku pakietu `java.util.stream` strumień reprezentowany jest przez interfejs `Stream<T>`. Strumień to sekwencja elementów, które można przetwarzać sekwencyjnie lub równolegle.

2. **Operacje pośrednie i końcowe**: Strumienie mają dwie główne grupy operacji: pośrednie (transformujące strumień, zwracają nowy strumień) i końcowe (produkujące wynik lub efekt uboczny).

    - Przykłady operacji pośrednich: `filter`, `map`, `sorted`.
    - Przykłady operacji końcowych: `collect`, `forEach`, `reduce`.

3. **Short-circuit**: Niektóre operacje na strumieniach, takie jak `limit` czy `findFirst`, mogą zakończyć przetwarzanie wcześnie, gdy znajdą odpowiedni wynik.

```java
List<Student> students = Arrays.asList(
    new Student("Leonardo", 5.0),
    new Student("Raphael", 4.2),
    new Student("Donatello", 5.9),
    new Student("Michelangelo", 3.1)
);
```

#### Operacje pośrednie

##### `filter`

Wybiera elementy spełniające dany warunek.

```java
Stream<Student> passedStudents = students.stream()
    .filter(student -> student.getGrade() >= 5.0);
```

##### `map`

Transformuje każdy element strumienia.

```java
Stream<String> studentNames = students.stream()
    .map(Student::getName);
```

##### `sorted`

Sortuje strumień.

```java
Stream<Student> sortedByGrade = students.stream()
    .sorted(Comparator.comparingDouble(Student::getGrade));
```

#### Operacje końcowe

##### `forEach`

Wykonuje akcję dla każdego elementu strumienia.

```java
students.stream()
    .forEach(System.out::println);
```

##### `collect`

Zmienia strumień w kolekcję.

```java
List<String> names = students.stream()
    .map(Student::getName)
    .collect(Collectors.toList());
```

##### `reduce`

Składa elementy strumienia w jedną wartość.

```java
double averageGrade = students.stream()
    .mapToDouble(Student::getGrade)
    .average()
    .orElse(0.0);
```

#### Przetwarzanie równoległe

Można łatwo przekształcić strumień sekwencyjny w strumień równoległy za pomocą metody `parallelStream()` lub `parallel()`. Pozwala to na równoległe przetwarzanie danych, co jest szczególnie przydatne w przypadku dużych zbiorów danych.

```java
double averageGradeParallel = students.parallelStream()
    .mapToDouble(Student::getGrade)
    .average()
    .orElse(0.0);
```

Przetwarzanie strumieniowe w Javie umożliwia składanie wielu operacji w jednym łańcuchu, co sprawia, że kod jest bardziej czytelny i wyraźny. Warto zaznaczyć, że operacje na strumieniach nie modyfikują źródła danych; zamiast tego tworzą nowy strumień pośredni lub końcowy wynik.

## Narzędzia programowania operacji wejście-wyjście w języku Java

W Javie operacje wejścia-wyjścia (I/O) odnoszą się do czytania i zapisywania danych. Java dostarcza bogate API do operacji I/O, które można znaleźć głównie w pakietach `java.io` i `java.nio`. Współczesne wersje Javy zachęcają do korzystania z pakietu `java.nio.file` ze względu na jego wydajność i nowoczesne API. Jednakże tradycyjne klasy z pakietu `java.io` są nadal szeroko stosowane, zwłaszcza w starszym kodzie.

### Pakiet `java.io`

Ten pakiet zawiera większość klas używanych do operacji blokujących wejścia-wyjścia.

-   **Strumienie bajtowe**: Do operacji I/O na plikach binarnych.

    -   `FileInputStream`
    -   `FileOutputStream`

-   **Strumienie znakowe**: Do operacji I/O na plikach tekstowych.

    -   `FileReader`
    -   `FileWriter`

-   **Buforowane strumienie**: Dla wydajniejszego I/O.

    -   `BufferedReader`
    -   `BufferedWriter`
    -   `BufferedInputStream`
    -   `BufferedOutputStream`

-   **Inne klasyczne klasy i interfejsy**:
    -   `File`: Reprezentuje ścieżkę do pliku lub katalogu.
    -   `Serializable`: Interfejs umożliwiający serializację obiektu.

```java
try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
}
```

### Pakiet `java.nio`

Pakiet `java.nio` (New I/O) został wprowadzony w Javie 1.4 i dostarcza alternatywne i bardziej wydajne metody I/O. Jest on szeroko stosowany, szczególnie w operacjach nieblokujących I/O i buforowanym dostępie do plików.

-   **Bufory**: `ByteBuffer`, `CharBuffer`, `IntBuffer` itp.

-   **Kanały**:

    -   `FileChannel`: Dostęp do plików w stylu NIO.
    -   `SocketChannel` i `ServerSocketChannel`: Dla gniazd sieciowych.

-   **Selektory**: Umożliwiają niestandardowe i nieblokujące operacje I/O na wielu kanałach jednocześnie.

-   **Mapowanie plików w pamięci**: Za pomocą klasy `MappedByteBuffer`.

-   **Ścieżki i system plików**: Pakiet `java.nio.file` wprowadza nowoczesne podejście do pracy z systemem plików:
    -   `Paths` i `Path`
    -   `Files`: Klasa pomocnicza z przydatnymi metodami dla operacji na plikach.
    -   `WatchService`: Monitorowanie zmian w systemie plików.

```java
Path path = Paths.get("file.txt");
List<String> lines = Files.readAllLines(path, StandardCharsets.UTF_8);

for (String line : lines)
    System.out.println(line);
```
