x = {"a":4, "b":8, "c":1, "d":10 }

new_list = sorted(x.items(), key=(lambda k:k[1]))

print (new_list)


#OR
import operator

sorted(x.items(), key=operator.itemgetter(1))