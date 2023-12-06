from getdata import get_day_data

cardlines = get_day_data(4).split("\n")

# part 1

pointsum = 0

# for every card
for line in cardlines:
    # fix error
    if line == "":
        break

    # split it into the card numbers and the have numbers
    broken = line.split("|")

    cardnumbers = broken[0].split(":")[1].split(" ")

    havenumbers = broken[1].split(" ")
    
    # count how many numbers show up from card numbers in have numbers
    count = 0
    for number in cardnumbers:
        for have in havenumbers:
            if number.isdigit() and number == have:
                count += 1

    # if you didn't count anything go to the next line
    if count-1 == -1:
        continue

    # 0 cards should be 0, 1 card is 1, 2 cards is 2, 3 cards is 4 . . . this follows the pattern 2^(x-1) (we have to make a special case for zero, thats what the above thing is)
    pointsum += pow(2, count-1)


print(pointsum)
print()

# part 2

# List in the format [ [index of the next card, the amount of times it has been copied], [index of the next card, the amount of times it has been copied] ]
# Like [ [0,1][1, 1] ] which eventually turns into something like [ [2, 24], [3, 47] . . . ]
indexlist = []

# we start with one copy of each card, so we must load the array with all of those copies.
for lineid in range(len(cardlines)):
    if cardlines[lineid] == "":
        continue
    indexlist.append([lineid, 1])

finalcount = 0

# while we still have something in the list
while len(indexlist):
    # error fixing
    if (indexlist[0][0] > len(cardlines)):
        continue
    
    # add the amount of copies this card is
    finalcount += indexlist[0][1]

    # split the card into it's components and count ONCE.
    broken = cardlines[indexlist[0][0]].split("|")
    cardnumbers = broken[0].split(":")[1].split(" ")
    havenumbers = broken[1].split(" ")

    # counting ONCE!!!!
    count = 0
    for number in cardnumbers:
        for have in havenumbers:
            if number.isdigit() and number == have:
                count += 1

    # for all the cards in count range above this card, add copies, which will be a single copy for every copy of this thing
    for i in range(count):
        # if the card isn't in there yet 
        if i+1 >= len(indexlist):
            indexlist.append([indexlist[0][0]+i+1, indexlist[0][1]])
        else:
            indexlist[i+1][1] += indexlist[0][1]
    
    # pop the copies we just went through and move to the next thing
    indexlist.pop(0)


print(finalcount)