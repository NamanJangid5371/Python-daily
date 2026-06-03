def revers_string(text):
    if len(text)<=1:
        return text
    return text[-1]+revers_string(text[:-1])

print(revers_string("python"))