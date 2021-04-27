def int_func(z):
    s = z.split(" ")
    phrase = ""
    for i in range(0,len(s)):
        a = s[i]
        b = chr(ord(a[0])-32)
        if i < len(s)-1:
                phrase = phrase + b + a[1:] + " "
        else:
            phrase = phrase + b + a[1:]
    return phrase
y = int_func(input("Type lowercase english string divided by spaces: "))
print(y)