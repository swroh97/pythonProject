number = int(input("정수 입력 > "))
if number %2 == 0:
    print("\n".join(["입력한 문자열은 {}입니다.","{}은 짝수입니다."]).format(number, number))

else:
    print("""\ 입력한 문자열은 {}입니다. 
        {}은 홀수입니다.""".format(number, number))

def repeat_call(value, n):
    for i in range(n):
        print(value)


repeat_call(input("Input은 : ", ), 5)

