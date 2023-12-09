from getdata import get_day_data

hands = get_day_data(7).split("\n")

fivekind = [] # you cheaters
fourkind = [] # four of a kind
fullhouse = [] # full house
threekind = [] # three of a kind
twopair = [] # two pair
onepair = [] # single pair
highcard = [] # high card

# for each set of cards in the hands (each line)
for cards in hands:
    # split the cards JJJJJ and the score 111 in format 'JJJJJ 111'
    justcards = cards.split(" ")

    # pesky newline at the end
    if justcards == ['']:
        continue

    # A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
    # thirteen value array
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # for each card in the cards, for whatever value it is, we keep track of how many of those we see by using an array of accumulators
    for value in justcards[0]:
        if value == '2':
            counts[0] += 1
            continue
        if value == '3':
            counts[1] += 1
            continue
        if value == '4':
            counts[2] += 1
            continue
        if value == '5':
            counts[3] += 1
            continue
        if value == '6':
            counts[4] += 1
            continue
        if value == '7':
            counts[5] += 1
            continue
        if value == '8':
            counts[6] += 1
            continue
        if value == '9':
            counts[7] += 1
            continue
        if value == 'T':
            counts[8] += 1
            continue
        if value == 'J':
            counts[9] += 1
            continue
        if value == 'Q':
            counts[10] += 1
            continue
        if value == 'K':
            counts[11] += 1
            continue
        if value == 'A':
            counts[12] += 1
            continue
    
    # now we find out which card we saw the most in the hand
    largestcount = 0
    for num in counts:
        if num > largestcount:
            largestcount = num

    # and then we process that.
    # if we see five cards, this hand goes in fivekind
    if largestcount == 5:
        fivekind.append(cards)
    # if we see four cards, this hand goes in fourkind.
    if largestcount == 4:
        fourkind.append(cards)
    # if we see three cards, if we see two other matching cards in the same hand it goes to fullhouse, if not, threekind.
    if largestcount == 3:
        if 2 in counts:
            fullhouse.append(cards)
        else:
            threekind.append(cards)
    # if we see two card max, we check to see if it's two pair or just one pair and do accordingly
    if largestcount == 2:
        twos = 0
        for num in counts:
            if num == 2:
                twos += 1
        if twos == 2:
            twopair.append(cards)
        if twos == 1:
            onepair.append(cards)
    # and now we're left with high card.
    if largestcount == 1:
        highcard.append(cards)

# this is a bucket sort, how it works is we look at a card in the hand, and based on that card, push it into an array.
# this formula recurses until there is only one hand left in any given array, and then starts to reconstruct all of the buckets
# taking the highest buckets first and adding the lower buckets to the end of that bucket in order.
# cool stuff!
def thirteenbucketsort(hands):

    def recursingsort(hands, sortbyindex):
        # past the index
        if sortbyindex > 4:
            return hands
        
        # one thing (or less) in the list just return it
        if len(hands) < 2:
            return hands

        bucket2 = []
        bucket3 = []
        bucket4 = []
        bucket5 = []
        bucket6 = []
        bucket7 = []
        bucket8 = []
        bucket9 = []
        bucketT = []
        bucketJ = []
        bucketQ = []
        bucketK = []
        bucketA = []

        # look at the value of the card, bucket appropriately.
        for single in hands:
            if single[sortbyindex] == "2":
                bucket2.append(single)
                continue
            if single[sortbyindex] == "3":
                bucket3.append(single)
                continue
            if single[sortbyindex] == "4":
                bucket4.append(single)
                continue
            if single[sortbyindex] == "5":
                bucket5.append(single)
                continue
            if single[sortbyindex] == "6":
                bucket6.append(single)
                continue
            if single[sortbyindex] == "7":
                bucket7.append(single)
                continue
            if single[sortbyindex] == "8":
                bucket8.append(single)
                continue
            if single[sortbyindex] == "9":
                bucket9.append(single)
                continue
            if single[sortbyindex] == "T":
                bucketT.append(single)
                continue
            if single[sortbyindex] == "J":
                bucketJ.append(single)
                continue
            if single[sortbyindex] == "Q":
                bucketQ.append(single)
                continue
            if single[sortbyindex] == "K":
                bucketK.append(single)
                continue
            if single[sortbyindex] == "A":
                bucketA.append(single)
                continue
        
        # put the buckets in a list for "easier" iteration
        buckets = []
        buckets.append(bucketA)
        buckets.append(bucketK)
        buckets.append(bucketQ)
        buckets.append(bucketJ)
        buckets.append(bucketT)
        buckets.append(bucket9)
        buckets.append(bucket8)
        buckets.append(bucket7)
        buckets.append(bucket6)
        buckets.append(bucket5)
        buckets.append(bucket4)
        buckets.append(bucket3)
        buckets.append(bucket2)

        # now put the buckets together from A down to 2 and voila!
        # this is also where the recursion happens
        sortedhands = []
        for bucket in buckets:
            sortedhands += recursingsort(bucket, sortbyindex+1)

        # pass it up the chain
        return sortedhands
    # this actually starts the process.
    return recursingsort(hands, 0)

# we do this sorting for every type of hand
sortedfivekind = thirteenbucketsort(fivekind)
sortedfourkind = thirteenbucketsort(fourkind)
sortedfullhouse = thirteenbucketsort(fullhouse)
sortedthreekind = thirteenbucketsort(threekind)
sortedtwopair = thirteenbucketsort(twopair)
sortedonepair = thirteenbucketsort(onepair)
sortedhighcard = thirteenbucketsort(highcard)

# and then we put them all in order in a single array.
fullysorted = sortedfivekind + sortedfourkind + sortedfullhouse + sortedthreekind + sortedtwopair + sortedonepair + sortedhighcard

# flip that array
reversefullsort = fullysorted[::-1]

finalvalue = 0

# and do the rankings, and add to the sum.
for i in range(0, len(reversefullsort)):
    finalvalue += (int(reversefullsort[i].split(" ")[1]) * (i+1))

print("\nAnswer 1:")
print(finalvalue)

# part 2
# this one is more complicated because J is now wild, and also the lowest value by sorting,
# the notable changes are that J is now at the end of the bucket iteration, and the
# way in which we put stuff into the lists originally is a bit different, accounting for J.

def thirteenbucketsortJ(hands):

    def recursingsort(hands, sortbyindex):
        # past the index
        if sortbyindex > 4:
            return hands
        
        # print(hands)
        # one thing (or less) in the list just return it
        if len(hands) < 2:
            return hands

        bucket2 = []
        bucket3 = []
        bucket4 = []
        bucket5 = []
        bucket6 = []
        bucket7 = []
        bucket8 = []
        bucket9 = []
        bucketT = []
        bucketJ = []
        bucketQ = []
        bucketK = []
        bucketA = []

        for single in hands:
            if single[sortbyindex] == "2":
                bucket2.append(single)
                continue
            if single[sortbyindex] == "3":
                bucket3.append(single)
                continue
            if single[sortbyindex] == "4":
                bucket4.append(single)
                continue
            if single[sortbyindex] == "5":
                bucket5.append(single)
                continue
            if single[sortbyindex] == "6":
                bucket6.append(single)
                continue
            if single[sortbyindex] == "7":
                bucket7.append(single)
                continue
            if single[sortbyindex] == "8":
                bucket8.append(single)
                continue
            if single[sortbyindex] == "9":
                bucket9.append(single)
                continue
            if single[sortbyindex] == "T":
                bucketT.append(single)
                continue
            if single[sortbyindex] == "J":
                bucketJ.append(single)
                continue
            if single[sortbyindex] == "Q":
                bucketQ.append(single)
                continue
            if single[sortbyindex] == "K":
                bucketK.append(single)
                continue
            if single[sortbyindex] == "A":
                bucketA.append(single)
                continue

        buckets = []
        buckets.append(bucketA)
        buckets.append(bucketK)
        buckets.append(bucketQ)
        buckets.append(bucketT)
        buckets.append(bucket9)
        buckets.append(bucket8)
        buckets.append(bucket7)
        buckets.append(bucket6)
        buckets.append(bucket5)
        buckets.append(bucket4)
        buckets.append(bucket3)
        buckets.append(bucket2)
        buckets.append(bucketJ) # <- Look at me!

        sortedhands = []
        for bucket in buckets:
            sortedhands += recursingsort(bucket, sortbyindex+1)

        return sortedhands
    return recursingsort(hands, 0)

fivekind = []
fourkind = []
fullhouse = []
threekind = []
twopair = []
onepair = []
highcard = []

for cards in hands:
    justcards = cards.split(" ")
    if justcards == ['']:
        continue

    # A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
    # thirteen value array
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for value in justcards[0]:
        if value == '2':
            counts[0] += 1
            continue
        if value == '3':
            counts[1] += 1
            continue
        if value == '4':
            counts[2] += 1
            continue
        if value == '5':
            counts[3] += 1
            continue
        if value == '6':
            counts[4] += 1
            continue
        if value == '7':
            counts[5] += 1
            continue
        if value == '8':
            counts[6] += 1
            continue
        if value == '9':
            counts[7] += 1
            continue
        if value == 'T':
            counts[8] += 1
            continue
        if value == 'J':
            counts[9] += 1
            continue
        if value == 'Q':
            counts[10] += 1
            continue
        if value == 'K':
            counts[11] += 1
            continue
        if value == 'A':
            counts[12] += 1
            continue
    
    # ignore J, we deal with it when we're shifting things into lists J is in counts[9]
    largestcount = 0
    for num in range(len(counts)):
        if num == 9:
            continue
        if counts[num] > largestcount:
            largestcount = counts[num]

    # it looks complicated, it's just the max value + how many js and then sorted accordingly
    if largestcount == 5:
        fivekind.append(cards)
    elif largestcount == 4:
        if counts[9] == 1:
            fivekind.append(cards)
        else:
            fourkind.append(cards)
    elif largestcount == 3:
        if counts[9] == 2:
            fivekind.append(cards)
        elif counts[9] == 1:
            fourkind.append(cards)
        elif 2 in counts:
            fullhouse.append(cards)
        else:
            threekind.append(cards)
    elif largestcount == 2:
        twos = 0
        if counts[9] == 3:
            fivekind.append(cards)
        elif counts[9] == 2:
            fourkind.append(cards)
        elif counts[9] == 1:
            for num in counts:
                if num == 2:
                    twos += 1
            if twos == 2:
                fullhouse.append(cards)
            if twos == 1:
                threekind.append(cards)
        else:
            for num in counts:
                if num == 2:
                    twos += 1
            if twos == 2:
                twopair.append(cards)
            if twos == 1:
                onepair.append(cards)
    elif largestcount == 1:
        if counts[9] == 4:
            fivekind.append(cards)
        elif counts[9] == 3:
            fourkind.append(cards)
        elif counts[9] == 2:
            threekind.append(cards)
        elif counts[9] == 1:
            onepair.append(cards)
        else:
            highcard.append(cards)
    elif largestcount == 0:
        if counts[9] == 5:
            fivekind.append(cards)

# ok now we sort with the modified alg.
sortedfivekind = thirteenbucketsortJ(fivekind)
sortedfourkind = thirteenbucketsortJ(fourkind)
sortedfullhouse = thirteenbucketsortJ(fullhouse)
sortedthreekind = thirteenbucketsortJ(threekind)
sortedtwopair = thirteenbucketsortJ(twopair)
sortedonepair = thirteenbucketsortJ(onepair)
sortedhighcard = thirteenbucketsortJ(highcard)

# # this is fun to look at sometimes
# print(sortedfivekind)
# print()
# print(sortedfourkind)
# print()
# print(sortedfullhouse)
# print()
# print(sortedthreekind)
# print()
# print(sortedtwopair)
# print()
# print(sortedonepair)
# print()
# print(sortedhighcard)
# print()

# same as before, just into the same list, then flipped, then ranked and added to the sum.
fullysorted = sortedfivekind + sortedfourkind + sortedfullhouse + sortedthreekind + sortedtwopair + sortedonepair + sortedhighcard

reversefullsort = fullysorted[::-1]

finalvalue = 0

for i in range(0, len(reversefullsort)):
    finalvalue += (int(reversefullsort[i].split(" ")[1]) * (i+1))


print("\nAnswer 2:")
print(finalvalue)
