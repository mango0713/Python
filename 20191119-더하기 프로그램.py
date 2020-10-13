
def sum_func(n):
    s = 0
    for x in range(1, n+1):
        s = s + x
    return s
def sum_gauss(n):
    q = n * ( n + 1) / 2
    return q

z = int (input("값을 입력하세요"))
print (sum_func(z))
print (sum_gauss(z))         

