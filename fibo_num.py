import sys

def fibo(n):
        if n == 1:
                return [1]
        if n == 2:
                return [1,1]
        #n>2
        a = 1
        b = 1
        series = [a,b]
        for i in range(n-2):
                c=a+b
                series.append(c)
                a=b
                b=c
        return series
def num(n):
        if n == 0:
                return 0
        elif n == 1:
                return 1
        else:
                return num(n-1) + num(n-2)
try:
        n=int(input('number?:'))
        print(fibo(n))
        print(num(n))
except ValueError:
        print('wrong input')
