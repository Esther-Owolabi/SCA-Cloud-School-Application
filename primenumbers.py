userInput1 = int(input('Enter a number:  '))
userInput2 = int(input('Enter another number: '))
count = 0
PrimeNumbers = []
for num in range(userInput1, userInput2 + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            count += 1
            PrimeNumbers.append(num)

print(count)
print(PrimeNumbers)