def find_max(nums):
    max_number= nums[0]
    for number in nums:
        if number > max_number:
            max_number = number
    return max_number


nums = [6, 7, 9, 5, 2]
print(find_max(nums))

#numbers = [4,6,9,7,5,2]
#max_number = numbers[0]
#for number in numbers:
    #if number > max_number:
        #max_number = number
#print (max_number)