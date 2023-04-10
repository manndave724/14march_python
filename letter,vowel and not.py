def is_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter.lower() in vowels:
        return True
    else:
        return False

# example usage
print(is_vowel('a')) # True
print(is_vowel('b')) # False

