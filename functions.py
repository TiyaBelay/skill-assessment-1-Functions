# SOLUTIONS!

################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".
def raw_input():

    print "Hello World"

raw_input() #Function needs to be called in order for this to get executed

# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.

def raw_input(name):

    print "Hi, " + name

raw_input("Tiya")

# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.

def mult(a, b):

    print a * b

mult(2, 4)

# 4. Write a function that takes a string and an integer and
#    prints the string that many times

def mult(string, n):

    print "Hello " * n

mult("Hello", 3)

# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".

def eval(n):
    if n > 0:
        print "Higher than 0"
    else:
        print "Lower than 0"

eval(-1)

# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def div(n):
    if n % 3 == 0:
        print "Yes"
        return True
    else:
        print "No"
        return False
div(5)

# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.

def spaces(sentence):
    
    count = sentence.count(" ")
    print count
    return

spaces("How are you, Din?")

# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

default = 0.15

def total(meal_price, tip_percentage):
    if tip_percentage == 0:
        total = meal_price + (meal_price * default)
        print total
    else:
        total = meal_price + (meal_price * tip_percentage)
        print total

total(14, 0)

# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.
#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.



################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.



# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.

#default = 'Engineer'
#
#def job(name, job_title):
#    if job_title == None:
#        print default + name
#        return
#    else:
#        print job_title + name
#        return
#job('Tiya')

# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.






# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.

numbers = []

def append(n):
    numbers.append(n)
    print numbers

append(4)

