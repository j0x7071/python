def factorial(n):
    return 1 if n==0 else n*factorial(n-1)

def factorial_iterativo(n):
    res=1
    if n >= 2:
        for i in range(n,0,-1): res*i
    return res

def fib(n):
    return 1 if n<= 1 else fib(n-1) + fib(n-2)
    
def fib_m(n):
    
    cache={0: 1,1: 1}
    if n not in cache:
        cache[n]= fib_m(n-1)+fib_m(n-2)
    return cache[n]
    
def main():
    cache={0: 1,1: 1}
    x=int(input("ingrese numero"))
    #print(factorial(x))
    print(fib_m(x))
    
    
main()