def fibo(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)


#This is a Test
for i in range(10):
    print(fibo(i+1))