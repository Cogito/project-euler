import string
import operator
import itertools


def p059():
    with open('p059_cipher.txt') as cipher_text:
        alphabet = string.ascii_letters
        cipher_text = "".join(chr(int(c)) for c in cipher_text.read().split(","))
        for key in ((key1, key2, key3) for key1 in alphabet for key2 in alphabet for key3 in alphabet):
            plain_text = xor(cipher_text, key)
            if ' the ' in plain_text:
                print(sum_ascii_values(plain_text))


def xor(text, key):
    key = itertools.cycle(key)
    out = ""
    for character in text:
        out += chr(operator.xor(ord(character), ord(next(key))))
    return out


def sum_ascii_values(text):
    return sum(ord(c) for c in text)


def test_p059():
    assert xor(xor('this is a secret', 'key'), 'key') == 'this is a secret'


if __name__ == '__main__':
    p059()
