
def getAnswer(level):
    if level == "hard":
        options = ['a', 'b', 'c', 'd']
        info = "A to D:"
    elif level == "medium":
        options = ['a', 'b', 'c']
        info = "A to C:"
    elif level == "easy":
        options = ['a', 'b']
        info = "A to B:"
    while True:
        data = input("Pick an answer from " + info)
        if data.lower() not in options:
            print("Not an appropriate choice.")
        else:
            return data
    return

def isAnswerCorrect(user_answer, correct_answer):
    if user_answer == correct_answer :
        print("✔✔✔✔")
        print("correct")
        print("✔✔✔✔")
        return True
    else :
        print ("❌❌❌❌")
        print ("Incorrect")
        print ("❌❌❌❌")
        return False
    pass

def askQuestion(question):
    print("-----------------------")
    print(question)

def getValidatedInput(statement, options):
    while True:
        data = input(statement)
        if data.lower() not in options:
            print("Not an appropriate choice.")
        else:
            return data

def getHistoryTest(level):
    score = 0
    if level == "easy":
        #THIS OPENS THE EXTERNAL FILE!!!
        file = open("./easy_history_questions.txt", "r")
        #THIS IS THE EASY QIUZ!!!
        # Question 1
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your score it", score)
        
        # Question 2
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your score it", score)
        
        # Question 3
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your score it", score)
        
        # Question 4
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your score it", score)
        
        # Question 5
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your final score it", score, "out of 5")
        fName="score.txt"
        accessMode="w"
        myF= open(fName, accessMode)
        myF.write (str(score))
        myF.close()


        
    if level == "medium":
        #THIS IS THE MEDIUM QIUZ!!!
        file = open("./medium_history_questions.txt", "r")
        # Question 1
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "c"):
            score += 1
        print("Your score it", score)
        
        # Question 2
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your score it", score)
        
        # Question 3
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your score it", score)
        
        # Question 4
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your score it", score)
        
        # Question 5
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your final score it", score, "out of 5")
        fName="score.txt"
        accessMode="w"
        myF= open(fName, accessMode)
        myF.write (str(score))
        myF.close()


    if level == "hard":
        #THIS IS THE HARD QUIZ!!!
        file = open("./hard_history_questions.txt", "r")
        # Question 1
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "d"):
            score += 1
        print("Your score it", score)
        
        # Question 2
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your score it", score)
        
        # Question 3
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "c"):
            score += 1
        print("Your score it", score)
        
        # Question 4
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your score it", score)
        
        # Question 5
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your final score it", score, "out of 5")
        fName="score.txt"
        accessMode="w"
        myF= open(fName, accessMode)
        myF.write (str(score))
        myF.close()


def getassasinscreedTest(level):
    score = 0
    if level == "easy":
        #THIS OPENS THE EXTERNAL FILE!!!
        file = open("./easy_assasins_creed_questions.txt", "r")
        #THIS IS THE EASY QIUZ!!!
        # Question 1
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your score it", score)
        
        # Question 2
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your score it", score)
        
        # Question 3
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your score it", score)
        
        # Question 4
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your score it", score)
        
        # Question 5
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your final score it", score, "out of 5")
        fName="score.txt"
        accessMode="w"
        myF= open(fName, accessMode)
        myF.write (str(score))
        myF.close()


    if level == "medium":
        #THIS IS THE MEDIUM QIUZ!!!
        file = open("./medium_assasins_creed_questions.txt", "r")
        # Question 1
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "c"):
            score += 1
        print("Your score it", score)
        
        # Question 2
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your score it", score)
        
        # Question 3
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your score it", score)
        
        # Question 4
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your score it", score)
        
        # Question 5
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your final score it", score, "out of 5")
        fName="score.txt"
        accessMode="w"
        myF= open(fName, accessMode)
        myF.write (str(score))
        myF.close()
        
    if level == "hard":
        #THIS IS THE HARD QUIZ!!!
        file = open("./hard_assasins_creed_questions.txt", "r")
        # Question 1
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "d"):
            score += 1
        print("Your score it", score)
        
        # Question 2
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your score it", score)
        
        # Question 3
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "c"):
            score += 1
        print("Your score it", score)
        
        # Question 4
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your score it", score)
        
        # Question 5
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your final score it", score, "out of 5")
        fName="score.txt"
        accessMode="w"
        myF= open(fName, accessMode)
        myF.write (str(score))
        myF.close()

        
def getcodTest(level):
    score = 0
    if level == "easy":
        #THIS OPENS THE EXTERNAL FILE!!!
        file = open("./easy_COD_questions.txt", "r")
        #THIS IS THE EASY QIUZ!!!
        # Question 1
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your score it", score)
        
        # Question 2
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your score it", score)
        
        # Question 3
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your score it", score)
        
        # Question 4
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your score it", score)
        
        # Question 5
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your final score it", score, "out of 5")
        fName="score.txt"
        accessMode="w"
        myF= open(fName, accessMode)
        myF.write (str(score))
        myF.close()
        

    if level == "medium":
        #THIS IS THE MEDIUM QIUZ!!!
        file = open("./medium_COD_questions.txt", "r")
        # Question 1
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "c"):
            score += 1
        print("Your score it", score)
        
        # Question 2
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your score it", score)
        
        # Question 3
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your score it", score)
        
        # Question 4
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your final score it", score, "out of 5")
        fName="score.txt"
        accessMode="w"
        myF= open(fName, accessMode)
        myF.write (str(score))
        myF.close()
        
        # Question 5
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your final score it", score, "out of 5")
        fName="score.txt"
        accessMode="w"
        myF= open(fName, accessMode)
        myF.write (str(score))
        myF.close()

        
        #THIS IS THE HARD QUIZ!!!
    if level == "hard":
        file = open("./hard_COD_questions.txt", "r")
        # Question 1
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "d"):
            score += 1
        print("Your score it", score)
        
        # Question 2
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your score it", score)
        
        # Question 3
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "c"):
            score += 1
        print("Your score it", score)
        
        # Question 4
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your score it", score)
        
        # Question 5
        askQuestion(file.readline())
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your final score it", score, "out of 5")
        fName="score.txt"
        accessMode="w"
        myF= open(fName, accessMode)
        myF.write (str(score))
        myF.close()


    return score

firstname = input("what is your first name? ")
surname = input("what is your surname? ")
age = input("How old are you? ")
yeargroup = input("what year are you in? ")
username = (firstname [0:3] + age)
password = input("please insert your password ")
print ("your username is - "+ username)
print ("your password is - "+ password)
fName="studentlogin.txt"
accessMode="w"
myF= open(fName, accessMode)
myF.write(username + password)
myF.close()
print("Login Successful")

subject = getValidatedInput("What test do you want to do? History, assasins creed or COD zombies(just write cod)?", ("history", "assasins creed", "cod"))

level = getValidatedInput("What difficulty do you want you test to be? easy, medium or hard?", ("easy", "medium", "hard"))

if subject == "history":
    getHistoryTest(level)
if subject == "assasins creed":
    getassasinscreedTest(level)
if subject == "cod":
    getcodTest(level)
else:
    print("No test found")
