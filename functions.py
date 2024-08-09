# A function is a block of code which only runs when it is called. In python , we do not use curly brackets, we use indentation with tabs or spaces.

# Create function
def sayHello():
    print("Hello world")

# Return values
def getSum(num1,nums2):
    return num1+nums2

# A lambda function is a small anonymous function 
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions.

getSum2 = lambda num1,num2 : num1+num2

print(getSum2(5,4))