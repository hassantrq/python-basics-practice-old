def is_palindrome(s):
    s = ''.join(x for x in s if x.isalnum())
    s = s.lower()
    is_palin = True
    for i in range(len(s)):
        if (s[i] != s[-(i+1)]):
            is_palin=False
            #break
    return is_palin



s="12321" #sting to check if palindrome
print(is_palindrome(s))