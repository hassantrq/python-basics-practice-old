import itertools

def letter_combinations(digits):
    digits = list(digits)
    alpha={
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    }
    if len(digits) == 0:
        return ""
    elif len(digits) == 1:
        return list(alpha[int(digits[0])])
    else:
        alphab=""
        for num in digits:
            alphab += alpha[int(num)]
        comb = itertools.combinations(alphab, len(digits))
        comb_list = [''.join(i) for i in comb]


        return comb_list


print(letter_combinations("234"))



