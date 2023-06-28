# 함수를 선언합니다.
def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# 함수를 호출합니다.
print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))

def fibonacci(n):

    counter = 0

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#print("fibonacci(1):", fibonacci(1))
#print("fibonacci(2):", fibonacci(2))
#print("fibonacci(3):", fibonacci(3))
#print("fibonacci(4):", fibonacci(4))
print("fibonacci(5):", fibonacci(35))