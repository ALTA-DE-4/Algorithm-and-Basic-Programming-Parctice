def palindrome(input_string):
    kata = str(input_string) [ ::-1]
    if str (input_string) == kata:
        return True
    return False

print(palindrome("civic"))
print(palindrome("katak"))
print(palindrome("kasur rusak"))
print(palindrome("kupu-kupu"))
print(palindrome("lion"))