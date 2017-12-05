
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
        print("Correct")
        return True
    else :
        print ("Incorrect")
        return False
    pass

def askQuestion(question, *answers):
    print("-----------------------")
    print(question)
    for answer in answers:
        print(answer)

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
        askQuestion("When did WW1 start and end?", " A - 28 July 1914 to 11 November 1918", "B - 31 June 1912 to 22 september 1930?")
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your score it", score)

        askQuestion("when did WW2 srart and end?" " a - 1 September 1939 to 2 September 1945", "b - 31 April 1956 to 19 december 1969? ")
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your score it", score)

        askQuestion("when was the treaty of Versilles signed?", " a - March 20 1920", "b - June 28, 1919? ")
        if isAnswerCorrect(getAnswer(level), "b"):
            score +=1
        print("Your score it", score)

        askQuestion("Which countries took part in WW1?", " a - Britain, France, Russia, taly, Germany, Austria-Hungary, Ottoman Empire and Bulgaria", "b - China, Britain, France, Brazil, lithuania, Germany Sweden and Finland? ")
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your score it", score)
    if level == "medium":
        askQuestion("Adolf Hitler was born in which country?", " a-france", "b-Germany", "c-Austria")
        if isAnswerCorrect(getAnswer(level), "c"):
            score += 1
        print("Your score it", score)
        askQuestion("The disease that ravaged and killed a third of Europe's population in the 14th century is known as?", " a-the White death", " b-The bubonic plague", " c-smallpox")
        if isAnswerCorrect(getAnswer(level), "b"):
            score += 1
        print("Your score it", score)
        askQuestion("Who is known as the Artist of the world famous painting Mona Lisa?", " -Leonardo da Vinci", " b-Michelangelo", " c-Vincent van Gogh ")
        if isAnswerCorrect(getAnswer(level), "a"):
            score += 1
        print("Your score it", score)
    else:
        print("No test found")

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
myF.write(username    +   password)
myF.close()
print("Login Successful")

subject = getValidatedInput("What test do you want to do? History, music or computer science?", ("history", "music", "computer science"))

level = getValidatedInput("What difficulty do you want you test to be? easy, medium or hard?", ("easy", "medium", "hard"))

if subject == "history":
    getHistoryTest(level)
else:
    print("No test found")
