length = 10
index = 0
while index < length:
    if index + 1 < length:
        print str(index) + "," + str(index + 1)
        index += 2
    else:
        index += 1
