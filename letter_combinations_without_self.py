import itertools

def letter_combinations(digits):
    digits = list(digits)
    print(digits)
    comb_list = []
    comb=[]
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
    elif len(digits) == 2:
        comb = itertools.product(list(alpha[int(digits[0])]), list(alpha[int(digits[1])]))
        for v1, v2 in comb:
            comb_list.append(v1+v2)
    elif len(digits) == 3:
        comb = itertools.product(list(alpha[int(digits[0])]), list(alpha[int(digits[1])]), list(alpha[int(digits[2])]))
        for v1, v2, v3 in comb:
            comb_list.append(v1+v2+v3)
    elif len(digits) == 4:
        comb = itertools.product(list(alpha[int(digits[0])]), list(alpha[int(digits[1])]), list(alpha[int(digits[2])]), list(alpha[int(digits[3])]))
        for v1, v2, v3, v4 in comb:
            comb_list.append(v1+v2+v3+v4)
    return comb_list


comb = letter_combinations("234")
print(comb)


