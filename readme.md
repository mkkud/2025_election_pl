## Analiza wyników wyborów prezydenckich 2025 w Polsce
# Czy doszło, na masową skalę, do pomyłek w postaci zamiany wyników kandydatów w drugiej turze?
- Do analizy wykorzystano wyniki 1. i 2. tury wyborów pobrane ze strony PKW.
- Dane zostały zaimportowane do bazy danych .sqlite, nazwy kolumn zmieniono dla lepszej czytelności.
- W pierwszym kroku wyliczono teoretyczne wyniki drugiej tury, bazujące na przepływach elektoratów z badania exit poll IPSOS z 1 czerwca 2025, z uwzględnieniem nowych wyborców.
- Następnie tak otrzymane wyniki porównano z wynikami 2. tury zarejestrowanymi w PKW; komisje, w których teoretyczne wyniki danego kandydata są blisze wynikom przeciwnika niz wynikom tego kandydata, a jednocześnie są rózne od siebie o więcej niz 25%, oznaczono jako mozliwą zamianę wyników.
- Odrzucono komisje, w których zaden z kandydatów w drugiej turze nie otrzymał więcej ni 30 głosów

