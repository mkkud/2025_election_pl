SELECT komisja
	,nawrocki_1
	,nawrocki_2
	,trzaskowski_1
	,trzaskowski_2
	,nawrocki_przeplywy_2_n
	,trzaskowski_przeplywy_2_n
	,CASE 
		WHEN abs(nawrocki_przeplywy_2_n - trzaskowski_2) < abs(nawrocki_przeplywy_2_n - nawrocki_2)
			AND abs(trzaskowski_przeplywy_2_n - nawrocki_2) < abs(trzaskowski_przeplywy_2_n - trzaskowski_2)
			THEN 'TAK'
		ELSE 'NIE'
		END AS podejrzenie_zamiany
	,CASE 
		WHEN abs(nawrocki_przeplywy_2_n - trzaskowski_2) < abs(nawrocki_przeplywy_2_n - nawrocki_2)
			AND abs(trzaskowski_przeplywy_2_n - nawrocki_2) < abs(trzaskowski_przeplywy_2_n - trzaskowski_2)
			THEN CASE 
					WHEN nawrocki_2 < trzaskowski_2
						THEN 'Trzaskowski'
					ELSE 'Nawrocki'
					END
		ELSE NULL
		END AS zamiana_na_korzysc
FROM komisje_wyniki_sim
WHERE (
		abs(nawrocki_przeplywy_2_n - nawrocki_2) > nawrocki_2 * 0.25
		AND abs(trzaskowski_przeplywy_2_n - trzaskowski_2) > trzaskowski_2 * 0.25
		)
	AND (
		nawrocki_2 > 30
		AND trzaskowski_2 > 30
		)
	AND

podejrzenie_zamiany = 'TAK'
ORDER BY zamiana_na_korzysc ASC

