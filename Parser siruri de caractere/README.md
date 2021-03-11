## Parser siruri de caractere

### main.py

Fisierul main.py se ocupa de citirea, prelucrarea si scrierea datelor. 

din fisierele de intrare se citesc cele doua string-uri:
>string1 = f.readline().strip().upper()
>string2 = f.readline().strip().upper()

Se prelucreaza folosing metoda get_offsets(string1, string2) si se scriu datele de iesire.

### boyer_moore.py

In fisierul boyer_moore am definit cele 3 metode care se ocupa de impementarea algorimtului si metoda 'def check_limits(string1, string2)' care verifica conditia impusa in enunt.
>STRING_1_LIMIT = 40
>STRING_2_LIMIT = 15.000.000

Metoda def get_delta(string1) calculeaza matricea delta. Se verifica pentru fiecare substring, starea in care trebuie sa ajunga. 

	0 		[0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
	1 L 	[0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
	2 LF 	[3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
	3 LFA	[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]

Pentru cazul in care nu se gaseste o potrivire a substring-ului in string, tai prima litera din substring si ultitma litera din string. 

Exemplu:

		substring-ul pe care il caut: OOABCOOABC
		stringul in care caut: 		  OOABCOOABD

		-nu se potrivesc, fac o taiere => sirurile devin:

									  0ABCOOABC
									  00ABCOOAB
		-nu se potrivesc =>
									  ABCOOABC
									  OOABCOOA
		-nu se potrivesc =>
									  BCOOABC
									  OOABCOO
		-nu se potrivesc =>
									  COOABC
									  OOABCO
		-nu se potrivesc =>
									  OOABC
									  OOABC

		S-a gasit o potrivire, deci ma opresc.

		Dupa acest pas, vectorii devin:

	0 		[0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
	1 L 	[0 0 0 0 0 2 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
	2 LF 	[3 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
	3 LFA	[0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0]


Metoda def compute_offsets(string1, string2) apeleaza metoda get_delta pentru a obtine matricea de stari si calculeaza current_state efectuand scaderea dintre codul ASCII al literei curente si codul ASCII al literei A. 


		def get_offsets(string1, string2) apeleaza metoda care ii trimite 
	offset-urile finale.