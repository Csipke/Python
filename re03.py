import re
words = open('regex_sum_42.txt')
totalSum = 0
for numbers in words:
    numbers = numbers.rstrip() #kivágjuk őket, mégpedig azokat, akik:
    nums = re.findall(('[0-9]+'), numbers)
    if len(nums) > 0:
        nums = map(int, nums)
        total = sum(nums)
        totalSum += total
print(totalSum)

# Ez jó

    