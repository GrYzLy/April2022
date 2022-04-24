def is_number(userInput):
    value = str(userInput)
    if value.strip().lstrip('-').replace('.', '', 1).isdigit():
        return True
    else:
        return False
    pass


def convert_number(str):
    floatNumber = float(str)
    return floatNumber
    pass


def is_valid_operator(operator):
    operators = ('+', '-', '*', '/')
    isInOperators = operator in operators
    return isInOperators 
    pass


def ask_for_a_number(force_valid_input):
    while True:
        a = input("Podaj liczbę:")
        a_number = is_number(a)

        if a_number is False:
            if not force_valid_input:
                return None
            print("Niepoprawna liczba!")
        else:
            return convert_number(a)

    pass


def ask_for_an_operator(force_valid_input):
    while True:
        operator = input("Podaj operator:")
        isValid = is_valid_operator(operator)

        if isValid is False:
            if not force_valid_input:
                return None
            print("Niepoprawny operator!")
        else:
            return operator

    pass


def calc(operator, a, b):
    if not is_valid_operator(operator) or not is_number(a) or not is_number(b):
        return None
    
    result = 0
    
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        if b != 0:
            result = a / b
        else:
            print("Nie mozna dzielic przez 0")

    return result

    pass


def simple_calculator():
    while True:   
        a = ask_for_a_number(False)
        if not a:
            break
        operator = ask_for_an_operator(True)
        b = ask_for_a_number(True)
        result = calc(operator, a, b)

        if result:
            print("Wynik %s" % result)

    pass


if __name__ == '__main__':
    simple_calculator()
