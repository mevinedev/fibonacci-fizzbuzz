n = int(input("integer: "))
if n>=1:
    def fibonacci(n):
        if n==1:
            return 0
        elif n==2: 
            return 1
        elif n > 2:
            return fibonacci(n-1) + fibonacci(n-2)
for n in range (1, n+1):
    print(n,fibonacci(n)) 

