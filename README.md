# Założenia aplikacji

Aplikacja do zarządzania zamówieniami i ich wykonaniem w firmie typu tartak, wykonana przy użyciu Django.</br>
W bazie danych będą się znajdowały modele:</br>
-Klient - dane klienta tj. Imie, Nazwisko, Adres i tp</br>
-Zamówienie - dane dotyczace całego zamówienia np. Data złożenia, data wykonania, elementy</br>
-Element - klucz obcy Zamówienia, kazde zamówienie może mieć bliżej nieokreśloną liczbę elementów. Zawiera wszystkie dane dotyczace danego elementu tj. długość, wysokość, szerokość, ilość/objętość/ilość metrów bierzących</br>
Do poprawnego działania systemu, będą potrzebne 3 rodzaje użytkowników: Zwykły, zarządzający oraz administrator.</br>
Zwykły użytkownik będzie miał dostęp jedynie do odczytu informacji i w założeniu ma za zadanie wykonanie zamówienia.</br>
Zarządzający będzie mógł dodawac nowe zamówienia, klientów oraz przekazywać odpowiednie dane do innych użytkowników.</br>
Administrator posiada domyślne uprawnienia administracyjne Django, i jest odpowiedzialny za zarządzanie użytkownikami (dodawanie, usuwanie, nadawanie uprawnień)
