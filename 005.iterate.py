"""
    Itrerable, Iterator, Iteration => Iterate
"""

for i in range(1, 11):
    print(i)


nums = [1, 2, 3, 4, 5, 6, 7]
for num in nums:
    print(num)


# iterator => next()  or __next__()

inums = iter(nums)

print(next(inums))
print(next(inums))
print(next(inums))
print(inums.__next__())
