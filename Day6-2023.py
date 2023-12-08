from getdata import get_day_data

races = get_day_data(6).split("\n")

# part 1

racetimes = []
highscores = []

# this loads all the race times into racetimes
char = 0
while char < len(races[0]):
    # if the thing you see is not a digit, continue to the next character
    if not races[0][char].isdigit():
        char+=1
        continue
    
    # we have a digit. . .
    parsestring = ""

    while char < len(races[0]) and races[0][char].isdigit():
        # add this character to the string we will parse into an integer, continue to the next digit in this internal loop.
        parsestring += races[0][char]
        char+=1
    # number done! put the number into racetimes
    racetimes.append(int(parsestring))

# this loads all the high scores into highscores
char = 0
while char < len(races[1]):
    # if the thing you see is not a digit, continue to the next character
    if not races[1][char].isdigit():
        char+=1
        continue
    
    # we have a digit. . .
    parsestring = ""
    # perserve the start of the number
    while char < len(races[1]) and races[1][char].isdigit():
        # add this character to the string we will parse into an integer, continue to the next digit in this internal loop.
        parsestring += races[1][char]
        char+=1
    # number done! put the number into highscores
    highscores.append(int(parsestring))

# print(racetimes)
# print(highscores)

totalslist = []
# the important part is the if statement, everything else just moves over the data.
for raceid in range(len(racetimes)):
    accum = 0
    for i in range(racetimes[raceid]):
        if i*(racetimes[raceid] - i) > highscores[raceid]:
            accum += 1
    totalslist.append(accum)

finalnum = 1
for num in totalslist:
    # print(num)
    finalnum *= num

print("Answer 1:")
print(finalnum)
print()


# part 2

singleracetime = 0
singlehighscore = 0

# this loads singleracetime
char = 0
while char < len(races[0]):
    # this finds the first digit
    if not races[0][char].isdigit():
        char+=1
        continue
    
    # we have a digit. . .
    parsestring = ""
    
    while char < len(races[0]):
        # add this character to the string we will parse into an integer, continue to the next digit in this internal loop.
        # this will skip anything that is not a digit since we want all the digits parsed into a single number this time around
        if races[0][char].isdigit():
            parsestring += races[0][char]
        char+=1
    # number done! put the number into singleractime
    singleracetime = (int(parsestring))

char = 0
while char < len(races[1]):
    # if the thing you see is not a digit, continue to the next character
    if not races[1][char].isdigit():
        char+=1
        continue
    
    # we have a digit. . .
    parsestring = ""
    
    while char < len(races[1]):
        # add this character to the string we will parse into an integer, continue to the next digit in this internal loop.
        # this will skip anything that is not a digit since we want all the digits parsed into a single number this time around
        if races[1][char].isdigit():
            parsestring += races[1][char]
        char+=1
    # number done! put the number into singlehighscore
    singlehighscore = (int(parsestring))


# print(singleracetime)
# print(singlehighscore)
# print()

# whenever we find a case that beats the highscore, add it to the number of solutions
# this takes around 5-10 seconds
singleaccum = 0
for i in range(singleracetime):
    if i*(singleracetime - i) > singlehighscore:
        singleaccum += 1

print("Answer 2:")
print(singleaccum)
print()