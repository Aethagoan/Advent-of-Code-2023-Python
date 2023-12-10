from getdata import get_day_data

reports = get_day_data(9).split("\n")

reports.pop(-1) # get rid of that pesky newline at the end

def getchangenumber(numbers):
    # take all of the differences between adjacent nums and put them into a list
    changelist = []
    for i in range(1, len(numbers)):
        changelist.append(int(numbers[i]) - int(numbers[i-1]))

    # is the list beneath at the bottom level (is everything zero?)
    atbottomlevel = True
    for num in changelist:
        if num != 0:
            atbottomlevel = False

    # if we're just above the bottom level, pass the last number of this line (not the zero line below)
    if atbottomlevel:
        # print(changelist)
        return (numbers[len(numbers)-1])

    # add the last number underneath to the last number of this and pass it up the chain.
    return int(numbers[len(numbers)-1]) + getchangenumber(changelist)

# feed the function the input for each line, get a final number from that line and add it to the sum.
finalsum = 0
for report in reports:
    reportnums = report.split(" ")
    finalnumber = getchangenumber(reportnums)
    # print(finalnumber)
    finalsum += finalnumber

print("\nAnswer 1:")
print(finalsum)

# just put the input into the same function in reverse and it will do the same thing! magic!
finalsum = 0
for report in reports:
    reportnums = report.split(" ")
    finalnumber = getchangenumber(reportnums[::-1])
    # print(finalnumber)
    finalsum += finalnumber

print("\nAnswer 2:")
print(finalsum)