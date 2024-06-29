def caesar(offset, input_str):
    abjad = offset % 26
    alfabet_shifted = []
    
    for char in input_str:
        if char >= 'a' and char <= 'z':
            new_char = chr((ord(char) - ord('a') + abjad) % 26 + ord('a'))
            alfabet_shifted.append(new_char)
        elif char == ' ':
            alfabet_shifted.append(' ')  
    
    return ''.join(alfabet_shifted)

print(caesar(3, 'abc'))
print(caesar(2, 'alta'))
print(caesar(10, 'alterraacademy'))
print(caesar(1, 'abcdefghijklmnopqrstuvwxyz'))
print(caesar(1000, 'abcdefghijklmnopqrstuvwxyz'))

