select komisja, 
			nawrocki_1, nawrocki_2, 
			0.5*bartoszewicz+0.1*biejat+0.92*braun+0.14*holownia+0.8*jakubiak+0.5*maciak+0.88*mentzen+0.19*senyszyn+0.51*stanowski+0.8*woch+0.16*zandberg +nawrocki_1 as nawrocki_przeplywy_2,
			trzaskowski_1, trzaskowski_2, 
			0.5*bartoszewicz+0.9*biejat+0.08*braun+0.86*holownia+0.2*jakubiak+0.5*maciak+0.12*mentzen+0.81*senyszyn+0.49*stanowski+0.2*woch+0.84*zandberg +trzaskowski_1 as trzaskowski_przeplywy_2,
			wyborcy_2-wyborcy_1 as nowi_wyborcy,
			0.5*bartoszewicz+0.1*biejat+0.92*braun+0.14*holownia+0.8*jakubiak+0.5*maciak+0.88*mentzen+0.19*senyszyn+0.51*stanowski+0.8*woch+0.16*zandberg +nawrocki_1+0.45*(wyborcy_2-wyborcy_1) as nawrocki_przeplywy_2_n,
			0.5*bartoszewicz+0.9*biejat+0.08*braun+0.86*holownia+0.2*jakubiak+0.5*maciak+0.12*mentzen+0.81*senyszyn+0.49*stanowski+0.2*woch+0.84*zandberg +trzaskowski_1+0.55*(wyborcy_2-wyborcy_1) as trzaskowski_przeplywy_2_n
			
from protokoly_1_2