# receive targetSum and array of numbers
# return combination of nums in number used to reach targetSum, or None
# any number can be used as many times as possible


def howSum(targetSum, numbers, checked=None):
    if checked is None:
        checked = {}

    if targetSum in checked:
        return checked[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    for n in numbers:
        remainder = targetSum - n
        result = howSum(remainder, numbers, checked)
        if result is not None:
            result.append(n)
            checked[remainder] = result
            return result

    checked[targetSum] = None
    return None


print(howSum(7, [2, 3]))  # [3, 2, 2]
print(howSum(7, [5, 3, 4, 7]))  # [4, 3]
print(howSum(7, [2, 4]))  # None
print(howSum(8, [2, 3, 5]))  # [2, 2, 2, 2]
print(howSum(300, [7, 14]))  # None (probably jams :) )
