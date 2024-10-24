input_word = input("Enter some characters:")

def remove_vowels(word):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    result = ''.join(char for char in word if char not in vowels)
    return result


result = remove_vowels(input_word)
print("Word without vowels:", result)