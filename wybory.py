import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn=sqlite3.connect('wybory.db')
cursor = conn.cursor()

cursor.execute("""
SELECT 
  komisja,
  nawrocki_1, nawrocki_2,
  trzaskowski_1, trzaskowski_2,
  nawrocki_przeplywy_2_n,
  trzaskowski_przeplywy_2_n,
  CASE
    WHEN 
      ABS(nawrocki_przeplywy_2_n - trzaskowski_2) < ABS(nawrocki_przeplywy_2_n - nawrocki_2)
      AND
      ABS(trzaskowski_przeplywy_2_n - nawrocki_2) < ABS(trzaskowski_przeplywy_2_n - trzaskowski_2)
    THEN 'TAK'
    ELSE 'NIE'
  END AS podejrzenie_zamiany,
  CASE
    WHEN
      ABS(nawrocki_przeplywy_2_n - trzaskowski_2) < ABS(nawrocki_przeplywy_2_n - nawrocki_2)
      AND
      ABS(trzaskowski_przeplywy_2_n - nawrocki_2) < ABS(trzaskowski_przeplywy_2_n - trzaskowski_2)
    THEN
      CASE
        WHEN nawrocki_2 < trzaskowski_2 THEN 'Trzaskowski'
        ELSE 'Nawrocki'
      END
    ELSE NULL
  END AS zamiana_na_korzysc
FROM komisje_wyniki_sim
WHERE (
    ABS(nawrocki_przeplywy_2_n - nawrocki_2) > nawrocki_2 * 0.25
    AND
    ABS(trzaskowski_przeplywy_2_n - trzaskowski_2) > trzaskowski_2 * 0.25
  )
AND (nawrocki_2 > 30 AND trzaskowski_2 > 30)
AND (
  ABS(nawrocki_przeplywy_2_n - trzaskowski_2) < ABS(nawrocki_przeplywy_2_n - nawrocki_2)
  AND
  ABS(trzaskowski_przeplywy_2_n - nawrocki_2) < ABS(trzaskowski_przeplywy_2_n - trzaskowski_2)
)
ORDER BY zamiana_na_korzysc ASC;
""")

results = cursor.fetchall()

df = pd.DataFrame(results, columns=[
    "Komisja", "Nawrocki I", "Nawrocki II", 
    "Trzaskowski I", "Trzaskowski II", 
    "Przepływy Nawrocki", "Przepływy Trzaskowski",
    "Podejrzenie", "Na korzyść"
])

conn.close()

df.to_excel("wyniki_podejrzenia.xlsx", index=False)

print("Excel file saved as wyniki_podejrzenia.xlsx")