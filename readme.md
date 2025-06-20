(English below)
# Analiza wyników wyborów prezydenckich 2025 w Polsce
## Czy doszło, na masową skalę, do pomyłek w postaci zamiany wyników kandydatów w drugiej turze?
- Do analizy wykorzystano wyniki 1. i 2. tury wyborów pobrane ze strony PKW.
- Dane zostały zaimportowane do bazy danych .sqlite, nazwy kolumn zmieniono dla lepszej czytelności.
- W pierwszym kroku wyliczono teoretyczne wyniki drugiej tury, bazujące na przepływach elektoratów z badania exit poll IPSOS z 1 czerwca 2025, z uwzględnieniem nowych wyborców.
- Następnie tak otrzymane wyniki porównano z wynikami 2. tury zarejestrowanymi w PKW; komisje, w których teoretyczne wyniki danego kandydata są blisze wynikom przeciwnika niz wynikom tego kandydata, a jednocześnie są rózne od siebie o więcej niz 25%, oznaczono jako mozliwą zamianę wyników.
- Odrzucono komisje, w których zaden z kandydatów w drugiej turze nie otrzymał więcej niz 30 głosów

## Wnioski
- w 22 komisjach odnotowano potencjalną zamianę głosów w drugiej turze
- 12 potencjalnych zamian przyniosło korzyść Karolowi Nawrockiemu, 10 Rafałowi Trzaskowskiemu
- Liczba komisji i fakt występowania róznic na korzyść obu kandydatów, wykluczają mozliwy wplyw owych nieprawidłowości na wyniki głosowania w skali kraju.
- Mimo to, fakt zaistnienia takich błędów wskazuje na zwrócenie uwagi na podobne incydenty, np. przy okazji wyborów samorządowych, gdzie mogą mieć one wpływ na wyniki głosowania.
- Wyniki zaprezentowano poniżej


English
# Analysis of the results of the 2025 presidential election in Poland
## Has there been, on a massive scale, confusion in the form of swapping the results of candidates in the second round?
- The results of the 1st and 2nd rounds of elections downloaded from the PKW website were used for the analysis.
- The data was imported into a .sqlite database, the column names were changed for better readability.
- In the first step, the theoretical results of the second round were calculated, based on electorate flows from the June 1, 2025 IPSOS exit poll, taking into account new voters.
- Then, the results so obtained were compared with the results of the 2nd round registered with the PKW; commissions in which the theoretical results of a given candidate are closer to those of the opponent than those of that candidate, while differing from each other by more than 25%, were marked as possible substitution of results.
- Committees in which no candidate in the second round received more than 30 votes were rejected

## Conclusions
- 22 commissions reported potential vote swapping in the second round
- 12 potential substitutions benefited Karol Nawrocki, 10 benefited Rafal Trzaskowski
- The number of commissions and the fact that there were differences in favor of both candidates, exclude the possible influence of these irregularities on the results of the vote nationwide.
- The results have been printed below

|**Komisja**                                                                                                                            | **Nawrocki I tura** | **Nawrocki II tura** | **Trzaskowski I tura** | **Trzaskowski II tura** | **"Przepływy" Nawrocki IPSOS** | **"Przepływy" Trzaskowski IPSOS** | **Podejrzenie zamiany w II turze** | **Zamiana na korzyść** |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------- | --------------- | ----------------- | ------------------ | ---------------------- | ------------------------- | --------------- | -------------- |
| 4_gm. Brześć Kujawski_Szkoła Podstawowa, Wieniec ul. Szkolna 1, 87-880 Brześć Kujawski                                                 | 137            | 466             | 274               | 331                | 345,34                 | 457,66                    | TAK             | Nawrocki       |
| 25_m. Grudziądz_Zespół Placówek Młodzieżowych "Bursa", ul. gen. Józefa Hallera 37, 86-300 Grudziądz                                    | 173            | 504             | 343               | 324                | 343,01                 | 484,99                    | TAK             | Nawrocki       |
| 95_m. Kraków_Zespół Szkolno-Przedszkolny Nr 14, ul. Stawowa 179, 31-346 Kraków                                                         | 218            | 1132            | 550               | 540                | 605,32                 | 1070,68                   | TAK             | Nawrocki       |
| 13_m. Mińsk Mazowiecki_Przedszkole Miejskie Nr 6 w Mińsku Mazowieckim, ul. Warszawska 250/81, 05-300 Mińsk Mazowiecki                  | 153            | 611             | 345               | 363                | 391,85                 | 589,15                    | TAK             | Nawrocki       |
| 3_gm. Olesno_Publiczna Szkoła Podstawowa Nr 3, klasa nr 3, ul. Ignacego Krasickiego 25, 46-300 Olesno                                  | 173            | 637             | 403               | 378                | 413,5                  | 609,5                     | TAK             | Nawrocki       |
| 9_gm. Strzelce Opolskie_Przedszkole Publiczne nr 10, ul. Adama Asnyka 6, 47-100 Strzelce Opolskie                                      | 107            | 416             | 311               | 223                | 219,96                 | 418,04                    | TAK             | Nawrocki       |
| 17_m. Gdańsk_Szkoła Podstawowa Nr 62, Gdańsk ul. Kępna 38, 80-635 Gdańsk 8                                                             | 187            | 585             | 323               | 346                | 419,58                 | 521,42                    | TAK             | Nawrocki       |
| 17_gm. Gorzyce_Wojewódzki Ośrodek Lecznictwa Odwykowego i Zakład Opiekuńczo-Leczniczy, ul. Zamkowa 8, 44-350 Gorzyce                   | 24             | 69              | 30                | 35                 | 48,16                  | 55,84                     | TAK             | Nawrocki       |
| 160_m. Katowice_Szpital, ul. Raciborska 27, 40-074 Katowice                                                                            | 17             | 44              | 32                | 39                 | 32,64                  | 50,36                     | TAK             | Nawrocki       |
| 35_m. Tychy_Przedszkole Nr 17 w Tychach, ul. Lwa Tołstoja 5, 43-100 Tychy                                                              | 192            | 581             | 352               | 347                | 370,97                 | 563,03                    | TAK             | Nawrocki       |
| 11_m. Chodzież_Budynek Szpitala w Chodzieży, ul. Strzelecka 32, 64-800 Chodzież                                                        | 25             | 47              | 43                | 38                 | 31,54                  | 54,46                     | TAK             | Nawrocki       |
| 47_m. Konin_Wojewódzki Szpital Zespolony im. dr. Romana Ostrzyckiego w Koninie, ul. Szpitalna 45, 62-500 Konin                         | 27             | 80              | 28                | 38                 | 56,35                  | 60,65                     | TAK             | Nawrocki       |
| 11_gm. Inowrocław_Świetlica w Miechowicach, Miechowice 34, 88-101 Miechowice                                                           | 62             | 71              | 39                | 124                | 121,29                 | 73,71                     | TAK             | Trzaskowski    |
| 4_gm. Bychawa_Urząd Miejski (sala konferencyjna), ul. Marszałka Józefa Piłsudskiego 22, 23-100 Bychawa                                 | 174            | 163             | 89                | 260                | 269,49                 | 163,51                    | TAK             | Trzaskowski    |
| 3_m. Grybów_Przedszkole Samorządowe "Pod Topolą", ul. Leszczynowa 1, 33-330 Grybów                                                     | 268            | 305             | 163               | 338                | 397,26                 | 248,74                    | TAK             | Trzaskowski    |
| 1_gm. Magnuszew_Szkoła Podstawowa w Magnuszewie, ul. Bohaterów Września 10, 26-910 Magnuszew                                           | 285            | 193             | 105               | 467                | 449,05                 | 212,95                    | TAK             | Trzaskowski    |
| 7_m. Ostrów Mazowiecka_Szkoła Podstawowa Nr 2 im. Papieża Jana Pawła II, ul. gen. Stefana Grota-Roweckiego 6, 07-300 Ostrów Mazowiecka | 166            | 205             | 149               | 338                | 297,57                 | 248,43                    | TAK             | Trzaskowski    |
| 498_zagranica_Cassino, Via Marconi, Aula Pacis, 03043 Cassino, Cassino, Republika Włoska                                               | 79             | 45              | 91                | 110                | 96,59                  | 57,41                     | TAK             | Trzaskowski    |
| 19_gm. Olesno_OSP w Kolonii Łomnickiej, Kolonia Łomnicka 20A, 46-300 Olesno                                                            | 18             | 40              | 13                | 46                 | 53,32                  | 32,68                     | TAK             | Trzaskowski    |
| 36_m. Ostrowiec Świętokrzyski_Dom Pomocy Społecznej, ul. Grabowiecka 7, 27-400 Ostrowiec Świętokrzyski                                 | 47             | 42              | 37                | 78                 | 63,93                  | 57,07                     | TAK             | Trzaskowski    |
| 4_gm. Staszów_Publiczna Szkoła Podstawowa nr 2 im. Ignacego Jana Paderewskiego w Staszowie, ul. Niepodległości 4, 28-200 Staszów       | 224            | 209             | 143               | 360                | 344,56                 | 226,44                    | TAK             | Trzaskowski    |
| 4_gm. Sępopol_Szkoła Podstawowa w Dzietrzychowie, Dzietrzychowo 10, 11-210 Sępopol                                                     | 71             | 91              | 63                | 155                | 141,93                 | 103,07                    | TAK             | Trzaskowski    |