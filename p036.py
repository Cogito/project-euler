def is_palindrome(text):
    return text == text[::-1]


def to_binary(n):
    return f'{n:b}'


def binary_palindromes(less_then):
    for n in range(1, less_then):
        if is_palindrome(str(n)) and is_palindrome(to_binary(n)):
            yield n


def test_p036():
    assert is_palindrome(str(585))
    assert to_binary(585) == '1001001001'
    assert is_palindrome(to_binary(585))


print(sum(binary_palindromes(1000000)))
