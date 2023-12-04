from getdata import get_day_data

# load the data into lines in an array
schematicarray = get_day_data(3).split("\n")

# # test stuff, comment out the line before this if you want to try this line out
# schematicarray = "467..114..\n...*......\n.35..633..\n......#...\n617*......\n.....+.58.\n..592.....\n.......755\n...$..*...\n.664...598".split("\n")

# # print out the map so you can look at it
# for line in schematicarray:
#     print (line)

partlist = []

partsum = 0

# for each line
for line in range(len(schematicarray)):

    # [ [number, starting index], [number, starting index], [number, starting index] ]
    linenumbers = []

    # parse through the line
    char = 0
    while char < len(schematicarray[line]):
        # if the thing you see is not a digit, continue to the next character
        if not schematicarray[line][char].isdigit():
            char+=1
            continue
        
        # we have a digit. . .
        parsestring = ""
        # perserve the start of the number
        startchar = char
        while char < len(schematicarray[line]) and schematicarray[line][char].isdigit():
            # add this character to the string we will parse into an integer, continue to the next digit in this internal loop.
            parsestring += schematicarray[line][char]
            char+=1
        # number done! put the number and it's starting index into linenumbers
        linenumbers.append([parsestring, startchar])

    # for each number we found on the line
    for number in linenumbers:
        # we start at the index we saved for this number
        index = number[1]

        # at every number, search the immediate surroundings for a symbol that is not "." or a digit.

        # . . . . . <- side length is going to be count/length of # + 2
        # . # # # . <- index starts at the first #, endindex is at the last #
        # . . . . .

        # if a symbol exists left of the number
        if (index - 1 >= 0) and not schematicarray[line][index - 1].isdigit() and not schematicarray[line][index - 1] == ".":
            # add this number to the total and continue
            partlist.append([number[0], schematicarray[line][index - 1]])
            partsum += int(number[0])
            continue
        
        # if a symbol exists right of the number
        endindex = index + len(number[0]) - 1
        if (endindex + 1 <= len(schematicarray[line]) - 1) and not schematicarray[line][endindex + 1].isdigit() and not schematicarray[line][endindex + 1] == ".":
            # add this number to the total and continue
            partlist.append([number[0], schematicarray[line][endindex + 1]])
            partsum += int(number[0])
            continue


        # calculate the side length
        sidelength = len(number) + 2

        # top
        # check bounds
        if line > 0:
            add = None
            # index from the start
            for i in range(sidelength + 1):
                # check internal bounds (characters)
                if (index - 1) + i >= 0 and (index - 1) + i <= len(schematicarray[line - 1]) - 1:
                    char = schematicarray[line - 1][(index - 1) + i]
                    # if there's a symbol
                    if not char.isdigit() and not char == ".":
                        # add this number to the total and continue
                        partlist.append([number[0], char])
                        add = int(number[0])
                        break
            
            if add != None:
                partsum += add
                continue
            
                

        # bottom
        # check external bounds (lines)
        if line < len(schematicarray) - 1:
            add = None
            # index from the start
            for i in range(sidelength + 1):
                # check internal bounds (characters)
                if (index - 1) + i >= 0 and (index - 1) + i <= len(schematicarray[line + 1]) - 1:
                    char = schematicarray[line + 1][(index - 1) + i]
                    # if there's a symbol
                    if not char.isdigit() and not char == ".":
                        # add this number to the total and continue
                        partlist.append([number[0], char])
                        add = int(number[0])
                        break
            
            if add != None:
                partsum += add
                continue








# part 2

gearsum = 0

numberofconnections = 0

# for each line, find the symbols that are gears "*" and save the positions
symbolpositions = []

# for each line
for line in range(len(schematicarray)):
    # for each character
    for index in range(len(schematicarray[line])):
        # if there's a gear at this position
        if schematicarray[line][index] == "*":
            # save the position as [line its on, index it's at, symbol it is (this is redundant)]
            symbolpositions.append([line, index, schematicarray[line][index]])


# for each position, we need to search the eight spaces around for a number. 
for entry in symbolpositions:
    linkedcomponents = []
    # print(entry)

    # . . . <- upper checked positions before parse
    # . * . <- symbol position, left, right
    # . . . <- lower checked positions before parse
    
    # starts at an origin index, and reads things to the right, not including the origin character.
    def parserightof(originid, lineid):
        tempindex = originid
        parsestring = ""
        # parse right until end of number
        while tempindex + 1 <= len(schematicarray[lineid]) - 1 and schematicarray[lineid][tempindex + 1].isdigit():
            # if we find another digit, add it to the parse string.
            parsestring += str(schematicarray[lineid][tempindex + 1])
            tempindex += 1
        return parsestring

    # starts at an origin index, and reads things to the left, not including the origin character.
    def parseleftof(originid, lineid):
        tempindex = originid
        parsestring = ""
        # parse left until end of number
        while tempindex - 1 >= 0 and schematicarray[lineid][tempindex - 1].isdigit():
            # if we find another digit, add it to the parse string.
            parsestring += str(schematicarray[lineid][tempindex - 1])
            tempindex -= 1
        # because of how we're tracking left, we have to return the parse flipped.
        return parsestring[::-1]

    # check bounds, if there's a digit to the right
    if entry[1] + 1 < len(schematicarray[entry[0]]) - 1 and schematicarray[entry[0]][entry[1] + 1].isdigit():
        #parse right, add number.
        linkedcomponents.append(int(parserightof(entry[1], entry[0])))
        
    # check bounds, if there's a digit to the left
    if entry[1] - 1 >= 0 and schematicarray[entry[0]][entry[1] - 1].isdigit():
        #parse left, add number.
        linkedcomponents.append(int(parseleftof(entry[1], entry[0])))

    #top
    # if the thing right above is occupied by a number there can only be one number above, but if it unnocupied there could be two from each corner
    # check outer bounds (lines)
    if entry[0] > 0:
        # if the character above is a digit
        if schematicarray[entry[0] - 1][entry[1]].isdigit():
            #move to leftmost point, go 1 past and parserightof that point, add number
            tempindex = entry[1]
            while tempindex - 1 >= 0 and schematicarray[entry[0] - 1][tempindex - 1].isdigit():
                tempindex -= 1
            linkedcomponents.append(int(parserightof(tempindex - 1, entry[0] - 1)))

        # there is no number directly above, check upper corners
        else:
            # top left
            if entry[1] > 0 and schematicarray[entry[0] - 1][entry[1] - 1].isdigit():
                linkedcomponents.append(int(parseleftof(entry[1], entry[0] - 1)))

            # top right
            if entry[1] + 1 < len(schematicarray[entry[0] - 1]) - 1 and schematicarray[entry[0] - 1][entry[1] + 1].isdigit():
                linkedcomponents.append(int(parserightof(entry[1], entry[0] - 1)))
        
        
    #bottom
    # if the thing right below is occupied by a number there can only be one number below, but if it is unnocupied there could be two from each corner
    # check outer bounds (lines)
    if entry[0] < len(schematicarray) - 1:
        # if the character below is a digit
        if schematicarray[entry[0] + 1][entry[1]].isdigit():
            #move to leftmost point, go 1 past and parserightof that point, add number
            tempindex = entry[1]
            while tempindex - 1 >= 0 and schematicarray[entry[0] + 1][tempindex - 1].isdigit():
                tempindex -= 1
            linkedcomponents.append(int(parserightof(tempindex - 1, entry[0] + 1)))

        # there is no number directly below, check lower corners
        else:
            # bottom left
            if entry[1] > 0 and schematicarray[entry[0] + 1][entry[1] - 1].isdigit():
                linkedcomponents.append(int(parseleftof(entry[1], entry[0] + 1)))

            # bottom right
            if entry[1] + 1 < len(schematicarray[entry[0] + 1]) - 1 and schematicarray[entry[0] + 1][entry[1] + 1].isdigit():
                linkedcomponents.append(int(parserightof(entry[1], entry[0] + 1)))

    # scope definition
    compsmultiplied = 0

    # if a symbol/component/gear touches two things EXACTLY
    if len(linkedcomponents) == 2:

        numberofconnections += 1
        print(numberofconnections)

        print("line " + str(entry[0] - 1 + 1) + ": " + str(schematicarray[entry[0] - 1]))
        print("line " + str(entry[0] + 1) + ": " + str(schematicarray[entry[0]]))
        print("line " + str(entry[0] + 1 + 1) + ": " + str(schematicarray[entry[0] + 1]))

        for component in linkedcomponents:
            print(str(component))
        print()

        # the only line that really matters here
        compsmultiplied = linkedcomponents[0]*linkedcomponents[1]

    # add the gear ratio.
    gearsum += compsmultiplied



print("\nnumber of parts: " + str(len(partlist)))

print("part sum: " + str(partsum) + "\n")

print("number of gear connections: " + str(numberofconnections))

print("gear sum:" + str(gearsum) + "\n")
