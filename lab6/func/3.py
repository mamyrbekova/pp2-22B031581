
def palindrome(string):
    string = ''.join(filter(str.isalnum, string.lower()))
    return string == string[::-1]


print(palindrome(input()))