def string_ascii_sum(s):
    arr=[]
    sum=0
    for c in s:
        arr.append(ord(c))

    for i in range(len(arr)-1):
        sum += (abs(arr[i] - arr[i+1]))

    print(sum)
