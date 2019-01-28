def main():
    problem1()
    problem2()

def problem1():
    # KEY: The requirement was to continue prompting user until they enter q to quit
    total = 0
    userInput = int(input("Enter a number or press 'q' to quit:"))
    if userInput.lower() != 'q':
        return int(input("Enter a number or press 'q' to quit:"))
    elif userInput == 'q':
        print(sum(userInput))
    else:
        print ("INVALID")

def problem2():
    # KEY: The requirements were to get the 2 numbers and pass them to your 'do_the_math' function
    num1= int(input("Enter the First Number in the calculation:"))
    num2= int(input("Enter the Second Number in the calculation:"))


# This function is never called
def do_the_math(num1,num2):
    add = (num1+num2,"add")
    sub = (num1-num2, "sub")
    div = (num1//num2, "div")
    mult = (num1*num2,"mult")




if __name__ == '__main__':
        main()