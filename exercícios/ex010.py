def eh_forma_XY(s):
    meio = len(s) // 2
    X = s[:meio]
    Y = s[meio:]
    return X == Y[::-1]

print(eh_forma_XY("ABCDPOOO"))
print(eh_forma_XY("123321"))
print(eh_forma_XY("123123"))