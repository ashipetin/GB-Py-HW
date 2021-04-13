n = int(input("Введите число n"))
x = n
digit=0
while(n>0):
    digit=digit+1
    n=n//10
print(digit)
ans = x + x*(10**digit) + x + x*(10**(digit*2)) + x*(10**(digit)) + x
print(ans)

# Позволяет использовать числа с любым количеством символов
