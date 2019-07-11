#mary sells n number of items
#assigns each a popularity rating inclusive range 1 to n
def minimum_swaps(ratings):
    #rearrange the items popularity in desceding order
    n = len(ratings)
    # store the new array of items with enumerated value, position
    new_positions = list(enumerate(ratings))
    # sort the array with the new values
    new_positions.sort(reverse=True, key=lambda y: y[1])
    #if an item is not visited
    swapped_item = {v: False for v in range(n)}
   #initialiaze the number of swaps
    swaps = 0
   #check whether an item has been swapped
    for i in range(n):
        if swapped_item[i] or new_positions[i][0] == i:
            continue
        # find the number of items
        size = 0
        j = i
        #if not swapped?
        while not swapped_item [j]:
            swapped_item[j] = True
            j = new_positions[j][0]
            size += 1
        # adding no of items to swap
        if size > 0:
            swaps += (size - 1)
    return swaps