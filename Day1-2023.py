from getdata import get_day_data

# splits the data we get back into an array where each string that was separated by a newline character
# is put into an index of the array.
splitresponse = get_day_data(1).split("\n")

# we use this array to check substrings within the given strings
stringdigitlist = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# in order to check from the end of the string, we have to check the words backwards because of
# how array is checked incrementally in reverse.
# do do this we have to reverse of all of the words in the array. one becomes eno, two becomes owt, etc.
flippedstringdigitlist = stringdigitlist.copy()
for i in range(len(flippedstringdigitlist)):
    flippedstringdigitlist[i] = flippedstringdigitlist[i][::-1]

# print(flippedstringdigitlist)

finalsum = 0

# for each string from the website
for i in range(len(splitresponse)):

    # print(splitresponse[i])
    firstdigit = 0
    lastdigit = 0

    # look through the string, j represents which character you're on/into the string (index)
    for j in range(len(splitresponse[i])):
        # if youve searched more than two levels into the string, start looking for words.
        if j > 2:
            # for each word in the word list
            for k in range(len(stringdigitlist)):
                # if you see that word in the stuff searched so far
                if stringdigitlist[k] in splitresponse[i][:j]:
                    # print("found " + stringdigitlist[k] + "!: reporting " + str(k+1))
                    firstdigit = str(k+1)
                    break
        
        # you found a word, so skip the rest.
        if firstdigit != 0:
            break
        
        # if you find a digit
        if splitresponse[i][j].isdigit():
            # print("found " + str(splitresponse[i][j]) + "!: reporting " + str(splitresponse[i][j]))
            firstdigit = str(splitresponse[i][j])
            break
        
    # we need to now look at the list backwards to find the first last digit
    flippedresponsestring = splitresponse[i][::-1]

    # look through the string backwards, j represents which character you're on/into the string (index)
    for j in range(len(flippedresponsestring)):
        # if youve searched more than two levels into the string, start looking for words.
        if j > 2:
            # for each word in the flipped list
            for k in range(len(flippedstringdigitlist)):
                # if that word is in what we've searched so far
                if flippedstringdigitlist[k] in flippedresponsestring[:j]:
                    # print("found " + flippedstringdigitlist[k] + "!: reporting " + str(k+1))
                    lastdigit = str(k+1)
                    break
        
        # you found a word, so skip the rest.
        if lastdigit != 0:
            break
        
        # if you find a digit
        if flippedresponsestring[j].isdigit():
            # print("found " + str(flippedresponsestring[j]) +"!: reporting " + str(flippedresponsestring[j]))
            lastdigit = str(flippedresponsestring[j])
            break

    # concatenate the digits you found, parse into an integer and add it to the sum.
    newdigit = firstdigit + lastdigit
    finalsum += int(newdigit)
    # print("")

# this will print out in your console, and is the number to be plugged in to the prompt in advent of code!
print("\nAnswer:\n" + str(finalsum))