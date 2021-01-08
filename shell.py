import logic

while True:
		text = input('logic > ')
		result, error = logic.run('<stdin>', text)

		if error: print(error.as_string())
		else: print(result)