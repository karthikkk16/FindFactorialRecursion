def FindFactorial(number):
    if number==0:
        return 1
    elif number==1:
        return 1
    else:
        return FindFactorial(number-1)*number
number=int(input())
print(FindFactorial(number))