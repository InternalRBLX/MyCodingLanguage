import basic

while True:
    text = input('basic > ')
    result, err = basic.run(text)

    if err: 
        print(err.as_string())
    else:
        print(result)