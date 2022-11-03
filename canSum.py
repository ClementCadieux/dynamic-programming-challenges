# receive targetSum and array of numbers
# return boolean on if the sum can be achieved using the numbers in the array
# any number can be used as many times as possible


def canSum(targetSum, numbers, checked=None):
    if checked is None:
        checked = {}
    if targetSum in checked:
        return checked[targetSum]

    if targetSum < 0:
        return False

    if targetSum == 0:
        return True

    for n in numbers:
        remainder = targetSum - n
        if canSum(remainder, numbers, checked):
            checked[remainder] = True
            return checked[remainder]

    checked[targetSum] = False
    return checked[targetSum]


print(canSum(7, [3, 5, 4, 7]))  # true
print(canSum(7, [2, 4]))  # false
print(canSum(7, [4, 5, 3]))  # true
print(canSum(300, [7, 14]))  # false
