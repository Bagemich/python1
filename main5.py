s = int(input("введите чётное поличесвто чисел , "))
i = 0
n = len(s)
def chet(s):
    return s % 2 == 0
print("количество чисел не чётное")
while i in range(n):
   s = (s[i-1]+s[(i+1) % n], end=' ')
print("сумма чисел")
