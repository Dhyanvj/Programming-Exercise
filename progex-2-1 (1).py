# Do not change any part of this script between the beginning
# of the file and point A (below)
# ----------------------------------------------------------------------------------------------------------------------------


def Main () :
    # 'Top-level' function (main program)
    theList = []   # Start with an empty list of theList
                   # because the user hasn't entered a list yet
    # Main loop - repeatedly displays the menu,
    #             gets the user to choose an operation
    #             and carries out that operation
    while True :
        ShowMenu ()
        chosen = GetMenuChoice ()
        if chosen == "0" :        # option 0 is 'quit the program'
            break
        else :
            theList = ExecuteChoice (chosen, theList)
    print ("Thanks for using the program: goodbye")



def ShowMenu () :
    print ("Menu options")
    print ("0 Quit the program")
    print ("1 Enter a new list of numbers")
    print ("2 Display the current list of numbers")
    print ("3 Find the count of all the positive numbers in the list")
    print ("4 Create a list containing double the value of each of the numbers in the list")
    print ("5 Create a list of the indexes of the negative numbers in the list")
    print ("6 Find the odd number in the list that has the largest magnitude")
    print ("7 Remove all even numbers from the list")
    print ("8 Show the first even and first odd number in the list")
    


def GetMenuChoice () :
    choice = input ("Please enter a number between 0 and 8: ")
    print()
    return choice



def ExecuteChoice (c,theList) :
    # performs the operation specified by c on the list theList
    if c == "1" :
        theList = GetTheNumbers ()
    if c == "2" :
        showNums (theList)
    if c == "3" :
        posCount = CountOfPositives (theList)
        print ("The count of positive numbers in the list is",posCount)
    if c == "4" :
        doubleList = ListOfDoubles (theList)
        print ("The doubles of all numbers in the list are")
        print (doubleList)
    if c == "5" :
        indexes = IndexesOfNegatives (theList)
        print ("The indexes of all negative numbers in the list are")
        print(indexes)
    if c == "6" :
        largest = LargestMagnitudeOdd (theList)
        if largest == 100 :
            print ("Thre are no odd numbers in the list")
        else :
            print ("The odd number with the largest magnitude is",largest)
    if c == "7" :
        theList = RemoveEvens (theList)
        print ("All even numbers have been removed from the list, leaving")
        print (theList)
    if c == "8" :
        firstNums = FirstEvenOdd (theList)
        if firstNums[0] == 999 :
            print ("There are no even numbers in the list")
        else :
            print ("The first even number in the list is",firstNums[0])
        if firstNums[1] == 100 :
            print ("There are no odd numbers in the list")
        else :
            print ("The first odd number in the list is",firstNums[1])     
        
    return theList



def GetTheNumbers () :
    # obtains a new list of numbers from the user
    numberList = []
    while True :
        numstr = input("Please type in a whole number, or q to quit: ")
        if numstr == 'q' :
            break
        number = int(numstr)
        numberList.append(number)
    return numberList
  
 
 
def showNums (numberList) :
    # shows the contents of numberList on screen
    print ("The current list of numbers is")
    print (numberList)
    print ()


# Do not change any part of this script between the beginning
# of the file and point A (below)
# ----------------------------------------------------------------------------------------------------------------------------
# POINT A
# ----------------------------------------------------------------------------------------------------------------------------

# Insert your Student Registration Number (SRN) between the
# quotation marks in the assignment statement below:

SRN = "21008521"

# For example, if your SRN is 01234567 the assignment statement
# should read  SRN = "01234567"

# ----------------------------------------------------------------------------------------------------------------------------
# Provide correct implementations of the functions below,
# each of which currently contains a code stub
#
# Do not change the name, the number of parameters, or
# the number of return values of any of these functions
#
# You are not allowed to use any external modules
# in the solution of these problems (no imports)
# ----------------------------------------------------------------------------------------------------------------------------
    


def CountOfPositives (numberList) :
    count = 0
    for i in numberList :
        if i > 0 :
            count = count + 1
    return count
    # Returns the count of positive numbers in numberList
    # (the quantity of numbers in numberList that are positive)

    return 0



def ListOfDoubles (numberList) :
    newList = []
    for i in numberList :
        i = i * 2
        newList = newList + [i]
    return newList
    # Returns a list of numbers, each member of which is a number which is
    # double the corresponding number in numberList.

    return []



def IndexesOfNegatives (numberList) :
    newList = []
    for i in numberList :
        if i < 0 :
            i = numberList.index(i)
            newList = newList + [i]
    return newList
    # Returns a list containing the indexes of all the negative
    # numbers in numberList.

    return []



def LargestMagnitudeOdd (numberList) :
    numList = []
    for i in numberList :
        if i % 2 != 0 :
            numList.append(i)
    if len(numList) == 0 :
        return 100
    else :
        return max(numList, key=abs)
    
    # Returns the odd number in numberList that has the largest magnitude
    # (the one that is furthest from zero, whether in a positive or a negative
    # direction).
    # If numberList contains no odd numbers the function should return
    # the value 100.
    
    return 100


def RemoveEvens (numberList) :
    numList = []
    for i in numberList :
        if i % 2 != 0 :
            numList = numList + [i]
    return numList
    # Returns a list of numbers noEvens that is the same as numberList
    # but with all of the even numbers removed

    return numberList



def FirstEvenOdd (numberList) :
    even = 999
    odd = 100
    for i in numberList :
        if i % 2 == 0 :
            even = i
            break
    for i in numberList :
        if i % 2 != 0 :
            odd = i
            break
    return [even,odd]
    # Returns a two element list, firstNums, containing the first even number
    # in numberList followed by the first odd number in numberList.
    # If numberList contains no even numbers the first element of firstNums
    # should be 999.
    # If numberList contains no odd numbers the second element of firstNums
    # should be 100.
    
    return [999,100]




Main()
