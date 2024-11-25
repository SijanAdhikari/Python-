import art
print(art.logo)

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operation_dic={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculator():
    should_accumulate=True
    first_num=float(input("What's the first number?:"))
    while should_accumulate:

        for symbol in operation_dic:
            print(symbol)
        operator=input("Pick an operation:")
        next_num=float(input("What's the next number?:"))
        result=operation_dic[operator](first_num,next_num)
        print(f"{first_num} {operator} {next_num} = {result}")
        go_on=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")

        if go_on=="y":
            first_num=result
        else:
            should_accumulate=False
            print("\n"*20)
            calculator()

calculator()