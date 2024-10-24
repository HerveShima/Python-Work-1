name = input("Enter a name: ")
a = []

def convert(name):
    for char in name:
        if char.isupper():
            a.append('_') 
            a.append(char.lower()) 
        else:
            a.append(char) 
    b = ''.join(a) 
    return b

result = convert(name)
print(result)
