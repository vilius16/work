#########################################################################################
#this is the student login part where the student can put in there details#
firstname = input("what is your first name? ")
surname = input("what is your surname? ")
age = input("How old are you? ")
yeargroup = input("what year are you in? ")
username = (firstname [0:3] + age)
password = input("please insert your password ")
print ("your username is - "+ username)
print ("your password is - "+ password)
##########################################################################################
#this puts there data in a external file#
fName="studentlogin.txt"
accessMode="w"
myF= open(fName, accessMode)
myF.write(username + password)
myF.close()
print("Login Successful")

###########################################################################################
#this asks what test and what difficalty they want there test to be#
subject=input("what suject do you want to do a test on? history? assasins creed? or COD zombies? ")
level=input("what level do you want it to be? easy? medium? or hard? " )
############################################################################################
# This is the easy history test#
#this gets the test from an external file#
if subject=="history" and level=="easy":
    file = open("./easy_history_questions.txt", "r")
#this gets the test from an external file#
    score = 0
    print (file.readline())
    q1E=input(" what is your answer? ")
    if q1E=="a":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q1E=="b":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q2E=input("what is your answer? ")
    if q2E=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q2E=="a":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q3E=input("what is your answer? ")
    if q3E=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q3E=="a":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q4E=input("what is your answer? ")
    if q4E=="a":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q4E=="b":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q5E=input("what is your answer? ")
    if q5E=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q5E=="a":
        print("incorrect")
    print("this is the end of the test, your final score is:", score)
################################################################################################
#this is the medium history test#
if subject=="history" and level=="medium":
    file = open("medium history questions", "r")
    print (file.readline())
    q1M=input("what is your answer? ")
    if q1M=="c":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q1M=="b":
        print("incorrect")
    if q1M=="a":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q2M=input("what is your answer? ")
    if q2M=="a":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q2M=="c":
        print("incorrect")
    if q2M=="b":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q3M=input("what is your answer? ")
    if q3M=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q3M=="c":
        print("incorrect")
    if q3M=="a":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q4M=input("what is your answer? ")
    if q4M=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q4M=="c":
        print("incorrect")
    if q4M=="a":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q5M=input("what is your answer? ")
    if q5M=="a":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q5M=="c":
        print("incorrect")
    if q5M=="b":
        print("incorrect")
####################################################################################################
#this loads the hard history test#
if subject=="history" and level=="hard":
    file = open("hard history questions", "r")
    print (file.readline())
    q1H=input("what is your answer? ")
    if q1H=="d":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q1H=="b":
        print("incorrect")
    if q1H=="a":
        print("incorrect")
    if q1H=="c":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q2H=input("what is your answer? ")
    if q2H=="a":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q2H=="c":
        print("incorrect")
    if q2H=="b":
        print("incorrect")
    if q2H=="d":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q3H=input("what is your answer? ")
    if q3H=="c":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q3H=="b":
        print("incorrect")
    if q3H=="a":
        print("incorrect")
    if q3H=="d":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q4H=input("what is your answer? ")
    if q4H=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q4H=="c":
        print("incorrect")
    if q4H=="a":
        print("incorrect")
    if q4H=="d":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q5H=input("what is your answer? ")
    if q5H=="a":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q5H=="c":
        print("incorrect")
    if q5H=="a":
        print("incorrect")
    if q5H=="d":
        print("incorrect")
#################################################################################################
#this is the easy assasins creed test#
if subject=="assasins creed" and level=="easy":
    file = open("easy assasins creed questions", "r")
    print (file.readline())
    q1E=input(" what is your answer? ")
    if q1E=="a":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q1E=="b":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q2E=input("what is your answer? ")
    if q2E=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q2E=="a":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q3E=input("what is your answer? ")
    if q3E=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q3E=="a":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q4E=input("what is your answer? ")
    if q4E=="a":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q4E=="b":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q5E=input("what is your answer? ")
    if q5E=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
    if q5E=="a":
        print("incorrect")
################################################################################################
#this is the medium assasins creed test#
if subject=="assasins creed" and level=="medium":
    file = open("medium assasins creed questions", "r")
    print (file.readline())
    q1M=input("what is your answer? ")
    if q1M=="c":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q1M=="b":
        print("incorrect")
    if q1M=="a":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q2M=input("what is your answer? ")
    if q2M=="a":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q2M=="c":
        print("incorrect")
    if q2M=="b":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q3E=input("what is your answer? ")
    if q3E=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q3E=="c":
        print("incorrect")
    if q3E=="a":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q4E=input("what is your answer? ")
    if q4E=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q4E=="c":
        print("incorrect")
    if q4E=="a":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q5E=input("what is your answer? ")
    if q5E=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q5E=="c":
        print("incorrect")
    if q5E=="a":
        print("incorrect")    
####################################################################################################
#this loads the hard assasins creed test#
if subject=="assasins creed" and level=="hard":
    file = open("hard assasins creed questions", "r")
    print (file.readline())
    q1H=input("what is your answer? ")
    if q1H=="d":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
    if q1H=="b":
        print("incorrect")
    if q1H=="a":
        print("incorrect")
    if q1H=="c":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q2H=input("what is your answer? ")
    if q2H=="a":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
    if q2H=="c":
        print("incorrect")
    if q2H=="b":
        print("incorrect")
    if q2H=="d":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q3H=input("what is your answer? ")
    if q3H=="c":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
    if q3H=="b":
        print("incorrect")
    if q3H=="a":
        print("incorrect")
    if q3H=="d":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q4H=input("what is your answer? ")
    if q4H=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
    if q4H=="c":
        print("incorrect")
    if q4H=="a":
        print("incorrect")
    if q4H=="d":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q5H=input("what is your answer? ")
    if q5H=="a":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
    if q5H=="c":
        print("incorrect")
    if q5H=="b":
        print("incorrect")
    if q5H=="d":
        print("incorrect")
###################################################################################################
if subject=="COD" and level=="easy":
    file = open("easy COD questions", "r")
    print (file.readline())
    q1E=input(" what is your answer? ")
    if q1E=="a":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q1E=="b":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q2E=input("what is your answer? ")
    if q2E=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q2E=="a":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q3E=input("what is your answer? ")
    if q3E=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q3E=="a":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q4E=input("what is your answer? ")
    if q4E=="a":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q4E=="b":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q5E=input("what is your answer? ")
    if q5E=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
    if q5E=="a":
        print("incorrect")
################################################################################################
#this is the medium COD test#
if subject=="COD" and level=="medium":
    file = open("medium COD questions", "r")
    print (file.readline())
    q1M=input("what is your answer? ")
    if q1M=="c":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q1M=="b":
        print("incorrect")
    if q1M=="a":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q2M=input("what is your answer? ")
    if q2M=="a":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q2M=="c":
        print("incorrect")
    if q2M=="b":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q3E=input("what is your answer? ")
    if q3E=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q3E=="c":
        print("incorrect")
    if q3E=="a":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q4E=input("what is your answer? ")
    if q4E=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q4E=="c":
        print("incorrect")
    if q4E=="a":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q5E=input("what is your answer? ")
    if q5E=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        score +=1
        print("Your score it", score)
    if q5E=="c":
        print("incorrect")
    if q5E=="a":
        print("incorrect")    
####################################################################################################
#this loads the hard history test#
if subject=="COD" and level=="hard":
    file = open("hard COD questions", "r")
    print (file.readline())
    q1H=input("what is your answer? ")
    if q1H=="d":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
    if q1H=="b":
        print("incorrect")
    if q1H=="a":
        print("incorrect")
    if q1H=="c":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q2H=input("what is your answer? ")
    if q2H=="a":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
    if q2H=="c":
        print("incorrect")
    if q2H=="b":
        print("incorrect")
    if q2H=="d":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q3H=input("what is your answer? ")
    if q3H=="c":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
    if q3H=="b":
        print("incorrect")
    if q3H=="a":
        print("incorrect")
    if q3H=="d":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q4H=input("what is your answer? ")
    if q4H=="b":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
    if q4H=="c":
        print("incorrect")
    if q4H=="a":
        print("incorrect")
    if q4H=="d":
        print("incorrect")
    print (file.readline())
    print (file.readline())
    q5H=input("what is your answer? ")
    if q5H=="a":
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
    if q5H=="c":
        print("incorrect")
    if q5H=="b":
        print("incorrect")
    if q5H=="d":
        print("incorrect")
##############################################################################################

        
    
