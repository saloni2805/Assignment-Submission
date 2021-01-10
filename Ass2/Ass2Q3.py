def count_elements_lists(nums):
    nums = [item for sublist in nums for item in sublist]
    dic_data = {}
    for num in nums:
        if num in dic_data.keys():
            dic_data[num] += 1
        else:
            key = num
            value = 1
            dic_data[key] = value
    return dic_data
nums = [
        [5,7,4,3],
        [9,5,4,2],
        [7,9,2,5],
       ]    
print("Original list of lists:")
print(nums)
print("\nFrequency of the elements in the said list of lists:")
print(count_elements_lists(nums))