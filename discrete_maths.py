def splitInteger(num, parts):
    # your code here

    x, rem = divmod(num, parts)
    first_element = [x for i in range(parts - rem)]
    last_element = [x + 1 for j in range(rem)]
    return (first_element + last_element)


print(splitInteger(10, 5))