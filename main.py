import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os
import seaborn as sns
import matplotlib.pyplot as plt


# reading csvs
df1 = pd.read_csv("input/protokoly_po_obwodach_utf8.csv", sep=";")
df2 = pd.read_csv("input/protokoly_po_obwodach_w_drugiej_turze_utf8.csv", sep=";")

# renaming columns for practical reasons
df1 = df1.rename(columns={
    "Nr komisji": "nr_komisji",
    "Gmina": "gmina",
    "Teryt Gminy": "teryt_gminy",
    "Powiat": "powiat",
    "Teryt Powiatu": "teryt_powiatu",
    "Województwo": "wojewodztwo",
    "Siedziba": "siedziba",
    "Typ obwodu": "typ_obwodu",
    "Typ obszaru": "typ_obszaru",
    "Liczba kart do głosowania otrzymanych przez obwodową komisję wyborczą, ustalona po ich przeliczeniu przed rozpoczęciem głosowania z uwzględnieniem ewentualnych kart otrzymanych z rezerwy": "karty_otrzymane",
    "Liczba wyborców uprawnionych do głosowania (umieszczonych w spisie, z uwzględnieniem dodatkowych formularzy) w chwili zakończenia głosowania": "wyborcy_uprawnieni",
    "Liczba niewykorzystanych kart do głosowania": "karty_niewykorzystane",
    "Liczba wyborców, którym wydano karty do głosowania w lokalu wyborczym (liczba podpisów w spisie oraz adnotacje o wydaniu karty bez potwierdzenia podpisem w spisie)": "karty_wydane_lokal",
    "Liczba wyborców, którym wysłano pakiety wyborcze": "pakiety_wyslane",
    "Liczba wyborców, którym wydano karty do głosowania w lokalu wyborczym oraz w głosowaniu korespondencyjnym (łącznie)": "karty_wydane_lacznie",
    "Liczba wyborców głosujących przez pełnomocnika (liczba kart do głosowania wydanych na podstawie aktów pełnomocnictwa otrzymanych przez obwodową komisję wyborczą)": "glosy_pelnomocnik",
    "Liczba wyborców głosujących na podstawie zaświadczenia o prawie do głosowania": "glosy_zaswiadczenie",
    "Liczba otrzymanych kopert zwrotnych w głosowaniu korespondencyjnym": "koperty_zwrotne",
    "Liczba kopert zwrotnych w głosowaniu korespondencyjnym, w których nie było oświadczenia o osobistym i tajnym oddaniu głosu": "koperty_brak_oswiadczenia",
    "Liczba kopert zwrotnych w głosowaniu korespondencyjnym, w których oświadczenie nie było podpisane przez wyborcę": "koperty_brak_podpisu",
    "Liczba kopert zwrotnych w głosowaniu korespondencyjnym, w których nie było koperty na kartę do głosowania": "koperty_brak_karty",
    "Liczba kopert zwrotnych w głosowaniu korespondencyjnym, w których znajdowała się niezaklejona koperta na kartę do głosowania": "koperty_niezaklejone",
    "Liczba kopert na kartę do głosowania w głosowaniu korespondencyjnym wrzuconych do urny": "koperty_wyjete",
    "Liczba kart wyjętych z urny": "karty_wyjete",
    "w tym liczba kart wyjętych z kopert na kartę do głosowania w głosowaniu korespondencyjnym": "karty_koperty_korespondencyjne",
    "Liczba kart nieważnych (bez pieczęci obwodowej komisji wyborczej lub inne niż urzędowo ustalone)": "karty_niewazne",
    "Liczba kart ważnych": "karty_wazne",
    "Liczba głosów nieważnych (z kart ważnych)": "glosy_niewazne",
    "w tym z powodu postawienia znaku „X” obok nazwiska dwóch lub większej liczby kandydatów": "glosy_x_wielu",
    "w tym z powodu niepostawienia znaku „X” obok nazwiska żadnego kandydata": "glosy_x_brak",
    "w tym z powodu postawienia znaku „X” wyłącznie obok nazwiska skreślonego kandydata": "glosy_x_skreslony",
    "Liczba głosów ważnych oddanych łącznie na wszystkich kandydatów (z kart ważnych)": "glosy_wazne",
    "BARTOSZEWICZ Artur": "bartoszewicz",
    "BIEJAT Magdalena Agnieszka": "biejat",
    "BRAUN Grzegorz Michał": "braun",
    "HOŁOWNIA Szymon Franciszek": "holownia",
    "JAKUBIAK Marek": "jakubiak",
    "MACIAK Maciej": "maciak",
    "MENTZEN Sławomir Jerzy": "mentzen",
    "NAWROCKI Karol Tadeusz": "nawrocki_1",
    "SENYSZYN Joanna": "senyszyn",
    "STANOWSKI Krzysztof Jakub": "stanowski",
    "TRZASKOWSKI Rafał Kazimierz": "trzaskowski_1",
    "WOCH Marek Marian": "woch",
    "ZANDBERG Adrian Tadeusz": "zandberg"
})

df2 = df2.rename(columns={
    "Nr komisji": "nr_komisji",
    "Gmina": "gmina",
    "Teryt Gminy": "teryt_gminy",
    "Powiat": "powiat",
    "Teryt Powiatu": "teryt_powiatu",
    "Województwo": "wojewodztwo",
    "Siedziba": "siedziba",
    "Typ obwodu": "typ_obwodu",
    "Typ obszaru": "typ_obszaru",
    "Liczba kart do głosowania otrzymanych przez obwodową komisję wyborczą, ustalona po ich przeliczeniu przed rozpoczęciem głosowania z uwzględnieniem ewentualnych kart otrzymanych z rezerwy": "karty_otrzymane",
    "Liczba wyborców uprawnionych do głosowania (umieszczonych w spisie, z uwzględnieniem dodatkowych formularzy) w chwili zakończenia głosowania": "wyborcy_uprawnieni",
    "Liczba niewykorzystanych kart do głosowania": "karty_niewykorzystane",
    "Liczba wyborców, którym wydano karty do głosowania w lokalu wyborczym (liczba podpisów w spisie oraz adnotacje o wydaniu karty bez potwierdzenia podpisem w spisie)": "karty_wydane_lokal",
    "Liczba wyborców, którym wysłano pakiety wyborcze": "pakiety_wyslane",
    "Liczba wyborców, którym wydano karty do głosowania w lokalu wyborczym oraz w głosowaniu korespondencyjnym (łącznie)": "karty_wydane_lacznie",
    "Liczba wyborców głosujących przez pełnomocnika (liczba kart do głosowania wydanych na podstawie aktów pełnomocnictwa otrzymanych przez obwodową komisję wyborczą)": "glosy_pelnomocnik",
    "Liczba wyborców głosujących na podstawie zaświadczenia o prawie do głosowania": "glosy_zaswiadczenie",
    "Liczba otrzymanych kopert zwrotnych w głosowaniu korespondencyjnym": "koperty_zwrotne",
    "Liczba kopert zwrotnych w głosowaniu korespondencyjnym, w których nie było oświadczenia o osobistym i tajnym oddaniu głosu": "koperty_brak_oswiadczenia",
    "Liczba kopert zwrotnych w głosowaniu korespondencyjnym, w których oświadczenie nie było podpisane przez wyborcę": "koperty_brak_podpisu",
    "Liczba kopert zwrotnych w głosowaniu korespondencyjnym, w których nie było koperty na kartę do głosowania": "koperty_brak_karty",
    "Liczba kopert zwrotnych w głosowaniu korespondencyjnym, w których znajdowała się niezaklejona koperta na kartę do głosowania": "koperty_niezaklejone",
    "Liczba kopert na kartę do głosowania w głosowaniu korespondencyjnym wrzuconych do urny": "koperty_wyjete",
    "Liczba kart wyjętych z urny": "karty_wyjete",
    "w tym liczba kart wyjętych z kopert na kartę do głosowania w głosowaniu korespondencyjnym": "karty_koperty_korespondencyjne",
    "Liczba kart nieważnych (bez pieczęci obwodowej komisji wyborczej lub inne niż urzędowo ustalone)": "karty_niewazne",
    "Liczba kart ważnych": "karty_wazne",
    "Liczba głosów nieważnych (z kart ważnych)": "glosy_niewazne",
    "w tym z powodu postawienia znaku „X” obok nazwisk obu kandydatów": "glosy_x_wielu",
    "w tym z powodu niepostawienia znaku „X” obok nazwiska żadnego kandydata": "glosy_x_brak",
    "w tym z powodu postawienia znaku „X” wyłącznie obok nazwiska skreślonego kandydata": "glosy_x_skreslony",
    "Liczba głosów ważnych oddanych łącznie na obu kandydatów (z kart ważnych)": "glosy_wazne",
    "NAWROCKI Karol Tadeusz": "nawrocki_2",
    "TRZASKOWSKI Rafał Kazimierz": "trzaskowski_2"
})

# creating sqlite3 database in memory
conn = sqlite3.connect(":memory:")
df1.to_sql("protokoly_1", conn, index=False, if_exists="replace")
df2.to_sql("protokoly_2", conn, index=False, if_exists="replace")

# executing sql queries
with open("sql\protokoly_1_2.sql", "r", encoding="utf-8") as f:
    protokoly_1_2 = f.read()
conn.executescript(protokoly_1_2)
conn.commit()

with open(("sql\komisje_wyniki.sql"), "r", encoding="utf-8") as f:
    komisje_wyniki_sql = f.read()
conn.executescript(komisje_wyniki_sql)
conn.commit()

with open(("sql\zamiana.sql"), "r", encoding="utf-8") as f:
    zamiana = f.read()
df_result = pd.read_sql_query(zamiana, conn)

with open(("sql\zamiana_filtered.sql"), "r", encoding="utf-8") as f:
    zamiana = f.read()
df_result_excel = pd.read_sql_query(zamiana, conn)

# renaming columns in results tables for display purposes
df_result = df_result.rename(columns={
    "komisja":"Komisja", 
    "nawrocki_1":"Nawrocki I", 
    "nawrocki_2":"Nawrocki II", 
    "trzaskowski_1":"Trzaskowski I", 
    "trzaskowski_2":"Trzaskowski II", 
    "nawrocki_przeplywy_2_n":"Przepływy Nawrocki", 
    "trzaskowski_przeplywy_2_n":"Przepływy Trzaskowski",
    "podejrzenie_zamiany":"Podejrzenie", 
    "zamiana_na_korzysc":"Na korzyść"
    }
    )
df_result_excel = df_result_excel.rename(columns={
    "komisja":"Komisja", 
    "nawrocki_1":"Nawrocki I", 
    "nawrocki_2":"Nawrocki II", 
    "trzaskowski_1":"Trzaskowski I", 
    "trzaskowski_2":"Trzaskowski II", 
    "nawrocki_przeplywy_2_n":"Przepływy Nawrocki", 
    "trzaskowski_przeplywy_2_n":"Przepływy Trzaskowski",
    "podejrzenie_zamiany":"Podejrzenie", 
    "zamiana_na_korzysc":"Na korzyść"
    }
    )

conn.close()

#saving filtered results to excel
df_result_excel.to_excel(os.path.join("result","results.xlsx"), index=False)
print("Excel file saved as results.xlsx")