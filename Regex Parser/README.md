## Regex Parser

#### main.py

Fisierul main.py se ocupa de citire, scrierea si parsarea datelor. 
Clasa class EvalVisitor(RegularExpressionVisitor) apeleaza functiile potrivite pentru a realiza transformarea RE -> NFA, in functie de input.

#### lfa_fa.py

Fisierul lfa_fa.py este o interfata comuna pentru ambele tipuri de automate. 

#### lfa_nfa.py 

In fisierul lfa_nfa.py se gasesc functiile pentru realizarea conversiei RE -> NFA.

#### lfa_dfa.py

In fisierul lfa_dfa.py se realizeaza conversia NFA -> DFA.

Se creeaza matriciile delta necesare pentru identificarea starilor, iar in cazul in care exista stari care nu au o tranzitie definita pentru fiecare simbol, se construieste o stare in plus.

Pentru cazurile in care se intalneste epsion, ma folosesc de o coada si marchez toate starile prin care se trece. 

#### RegularExpression.g4

Fisierul contine regulile gramaticii utilizate.


-----------
## Observatie
-----------

Pentru crearea fisierelor generate de ANTLR am folosit un script cu urmatoarele comenzi:

	alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
	antlr4 -Dlanguage=Python3 RegularExpression.g4 -visitor
	python3.8 main.py file.in file-nfa.out file-dfa.out
