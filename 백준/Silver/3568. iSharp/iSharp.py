statement = input().split()

prefix = statement[0]

for value in statement[1:]:
    name_chars = []
    type_chars = []

    for c in value[:-1]:
        if c.isalpha():
            name_chars.append(c)
        elif c == '[':
            type_chars.append(']')
        elif c == ']':
            type_chars.append('[')
        else:
            type_chars.append(c)
    
    name = "".join(name_chars)
    additionalType = "".join(reversed(type_chars))

    print(f"{prefix}{additionalType} {name};")