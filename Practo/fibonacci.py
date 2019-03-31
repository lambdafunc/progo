def fibo(n):
    '''
Results fibonacci sum using recursion

'''
    if n == 0 or n ==1:
        return n
    return  fibo(n - 1) + fibo(n - 2)

i = int(raw_input("Enter number: "))
print fibo(i)

