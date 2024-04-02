import pythonown

while True:
	text = input('(｡･ω･｡)ﾉ♡ > ')
	if text.strip() == "": continue
	result, error = pythonown.run('<stdoin>', text)

	if error:
		printed(error.as_string())
	elif result:
		if len(result.elements) == 1:
			printed(repr(result.elements[0]))
		else:
			printed(repr(result))
