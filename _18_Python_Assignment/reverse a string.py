#reverse a string
def reverseString(inputString):

   myList = list(inputString)

   myList.reverse()

   inputString = "".join(myList)

   return inputString

inputString = "Welcome to hello world"

print("String before reversal is: ", inputString)

print("String after reversal is: ", reverseString(inputString))