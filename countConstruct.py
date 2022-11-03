# receive targetString and array of strings
# return amount of times targetString can be constructed from array
# same as canSum but with strings?
# no splitting, only check start and end

def countConstruct(targetString, strings, checked=None):
    if checked is None:
        checked = {}

    if targetString in checked:
        checked[targetString] = checked.get(targetString, 0) + 1
        return checked[targetString]

    if targetString == "":
        return 1

    for string in strings:
        # check if too long
        if len(string) > len(targetString):
            continue
        # check at start
        newString = None
        if targetString[0:len(string)] == string:
            newString = targetString[len(string):]

        # check at end
        if targetString[len(targetString)-len(string):] == string:
            newString = targetString[0:len(targetString)-len(string)]

        if newString is None:
            continue

        count = countConstruct(newString, strings, checked)
        if count != 0:
            checked[newString] = checked.get(newString, 0) + count
            return checked[newString]

    return checked.get(targetString, 0)


print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # 4
# print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeee"]))  # 0
