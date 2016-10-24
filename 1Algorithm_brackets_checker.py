from stack import stack

def brackets_checker (symbol_string):
    x = stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string(index)
        if symbol in "([{":
            x.push(symbol)
        elif symbol in ")]}":
            if x.is_empty():
                balanced = False
            else:
                top = x.pop()
                if not matches(top,symbol):
                    balanced = False
        index = index + 1

    if balanced and x.is_empty():
        return True
    else:
        return False

def matches(open_paranthesis, close_paranthesis):
    dict_1 = ("(":")", "[":"]", "{":"}")
    return dict_1(open_paranthesis) == close_paranthesis

line = input("Enter string to check for balanced brackets: ")
print(line, ":", brackets_checker(line))
