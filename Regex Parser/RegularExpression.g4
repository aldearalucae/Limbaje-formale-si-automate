grammar RegularExpression;

expr:
	symb = SYMBOL STAR				# symStarExpr
	| LPAREN expr RPAREN			# parenExpr
	| symb = SYMBOL					# symbolExpr
	| left = expr right = expr		# concatExpr
	| left = expr OR right = expr	# orExpr
	| expr STAR						# starExpr;

SYMBOL: [a-z];

LPAREN: '(';

RPAREN: ')';

STAR: '*';

OR: '|';
