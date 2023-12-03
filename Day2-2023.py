from getdata import get_day_data

# read the data into an array where each line is an element
splitresponse = get_day_data(2).split("\n")


#part 1
idsum = 0

# on each line in lines 
for line in splitresponse:
    # there is an extra newline at the end, so this avoids an error.
    if line == "":
        break

    # splitting up the string to get us the ID
    # Lines look like this "Game Number: (all the other stuff)"
    gameid = int(line.split(":")[0].split(" ")[1])

    # print(gameid)

    # the maxes the page specifies for the colors:
    redmax = 12 
    greenmax = 13
    bluemax = 14

    # if we find a max has been exceeded, we refuse to add the gameID to the final sum.
    maxexceeded = False

    # splitting the line into the separate pulls. each pull ends with ;
    round = line.split(":")[1].split(";")

    for pull in round:
        # we make an array that looks like [" number color", " number color", " number color"] out of what we have
        colors = pull.split(",")

        # for each of those elements
        for col in colors:
            # get rid of the extra space element at the start while splitting each element
            # into an array like ["number", "color"]
            split = col.split(" ")[1:]
            # print(split)

            # check the color, then the appropriate value. if there's a problem we flag maxexceeded
            # and break the loop because we don't need to check the rest of an invalid game.
            if split[1] == "red":
                if int(split[0]) > redmax:
                    maxexceeded = True
                    break

            if split[1] == "blue":
                if int(split[0]) > bluemax:
                    maxexceeded = True
                    break

            if split[1] == "green":
                if int(split[0]) > greenmax: 
                    maxexceeded = True
                    break

        if maxexceeded:
            break
    
    # for any game/line that comes out of the loop without having exceeded the max 
    # we add to the sum.
    if not maxexceeded:
        idsum += gameid
    
# part 1 answer to put into the prompt on the website
print("\nAnswer 1:\n" + str(idsum))


#part 2
colorsum = 0

# for each line/game
for line in splitresponse:
    # fixes a newline bug at the end of file
    if line == "":
        break
    
    # this time we're checking the max value of all the sets in the game and reporting back
    # we're reporting the 'minimum' of the color item for the game to be valid
    # so we are selecting the biggest red, blue, and green values out of each pull
    redmin = 0
    bluemin = 0
    greenmin = 0

    # splitting the line into the separate pulls. each pull ends with ;
    round = line.split(":")[1].split(";")

    # print(round)


    for pull in round:
        #separate into numbers + colors [" number color", " number color" . . .]
        colors = pull.split(",")

        for col in colors:
            # separate each element into [ ["number", "color"], ["number", "color"] . . .]
            split = col.split(" ")[1:]
            # print(split)

            # check to see if the color we're looking at has a value higher than we've seen before,
            # if it does have a higher value, set it and then continue the loop (we don't need to check the other colors 
            # for this color, but we do need to look at the other colors in subsequent loops so we can't break it.)
            if split[1] == "red":
                if int(split[0]) > redmin:
                    redmin = int(split[0])
                    continue

            if split[1] == "blue":
                if int(split[0]) > bluemin:
                    bluemin = int(split[0])
                    continue

            if split[1] == "green":
                if int(split[0]) > greenmin: 
                    greenmin = int(split[0])
                    continue
    
    # we multiply all of the mins together (which can give us zero, but thankfully that is part of it)
    # and then add them to the grand sum.
    colorsum += (redmin*bluemin*greenmin)

# part 2 answer to put into the prompt on the website
print("\nAnswer 2:\n" + str(colorsum))