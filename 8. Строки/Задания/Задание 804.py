def CaesarCipherChar(c, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if c in alphabet:
        pos = alphabet.index(c)
        new_pos = (pos + k) % 26
        return alphabet[new_pos]
    elif c in ALPHABET:
        pos = ALPHABET.index(c)
        new_pos = (pos + k) % 26
        return ALPHABET[new_pos]
    else:
        return c


def CaesarCipher(S, k):
    result = ""
    for c in S:
        result += CaesarCipherChar(c, k)
    return result
