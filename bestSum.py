# receive targetSum and array of numbers
# return shortest combination of nums in number used to reach targetSum, or None
# any number can be used as many times as possible


def bestSum(targetSum, numbers, checked=None):
    if checked is None:
        checked = {}

    if targetSum in checked:
        return checked[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    result = None

    for n in numbers:
        remainder = targetSum - n
        res = bestSum(remainder, numbers, checked)
        if res is not None:
            res.append(n)
            if result is None or len(result) > len(res):
                result = res[:]
            res.remove(n)

    checked[targetSum] = result
    return result


print(bestSum(7, [2, 3]))  # [3, 2, 2]
print(bestSum(7, [5, 3, 4, 7]))  # [7]
print(bestSum(7, [2, 4]))  # None
print(bestSum(8, [2, 3, 5]))  # [3, 5]
print(bestSum(126, [1, 2, 2, 25]))  # [25, 25, 25, 25, 25, 1]
