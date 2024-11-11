# #Range function with for loop
# sum=0
# for number in range(1,101):
#     sum+=number
# print(sum)
for number in range(1,101):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    if number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")

    else:
        print(number)

