# receive targetString and array of strings
# return boolean on whether targetString can be constructed from array
# same as canSum but with strings?
# no splitting, only check start and end

def canConstruct(targetString, strings, checked=None):
    if checked is None:
        checked = {}

    if targetString in checked:
        return checked[targetString]

    if targetString == "":
        return True

    for string in strings:
        # check if too long
        if len(string) > len(targetString):
            continue
        # check at start
        if targetString[0:len(string)] == string:
            newString = targetString[len(string):]
            if canConstruct(newString, strings, checked):
                checked[newString] = True
                return True

        # check at end
        if targetString[len(targetString)-len(string):] == string:
            newString = targetString[0:len(targetString)-len(string)]
            if canConstruct(newString, strings, checked):
                checked[newString] = True
                return True

    checked[targetString] = False
    return False


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # true
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # false
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # true
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeee", "f"]))  # true
