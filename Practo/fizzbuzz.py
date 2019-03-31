for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print str(i) + " --> " + "fizzbuzz"
    elif i % 3 == 0:
        print str(i) + " --> " +  "fizz"
    elif i % 5 == 0:
        print str(i) + " --> " + "Buzz"
    else:
        print i



