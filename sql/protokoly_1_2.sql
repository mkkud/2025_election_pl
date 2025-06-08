create table protokoly_1_2 as 
select a.nr_komisji||'_'||a.gmina||'_'||a.siedziba as komisja,
			a.karty_wydane_lacznie as wyborcy_1,
			b.karty_wydane_lacznie as wyborcy_2,
			a.nawrocki_1,
			b.nawrocki_2,
			a.trzaskowski_1,
			b.trzaskowski_2,
			a.bartoszewicz,
			a.biejat,
			a.braun,
			a.holownia,
			a.jakubiak,
			a.maciak,
			a.mentzen, 
			a.senyszyn,
			a.stanowski,
			a.woch,
			a.zandberg
			
			
from protokoly_1 a inner join protokoly_2 b on a.nr_komisji=b.nr_komisji and a.siedziba=b.siedziba