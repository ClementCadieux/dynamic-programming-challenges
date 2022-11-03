# starting from top left of MxN grid,how many ways of traveling to bottom right only moving down/right
# recursion using dict

checked = {}

# order of args is irrelevant, make m smaller everytime


def gridTraveler(m, n):
    if m == 0 or n == 0:
        return 0

    if m == 1 or n == 1:
        return 1

    if n < m:
        temp = n
        n = m
        m = temp

    if (m, n) in checked:
        return checked[(m, n)]

    checked[(m, n)] = gridTraveler(m - 1, n) + gridTraveler(m, n - 1)
    return checked[(m, n)]


print(gridTraveler(0, 1))  # 0
print(gridTraveler(1, 1))  # 1
print(gridTraveler(2, 3))  # 3
print(gridTraveler(3, 2))  # 3
print(gridTraveler(3, 3))  # 6
print(gridTraveler(18, 18))  # 2333606220
