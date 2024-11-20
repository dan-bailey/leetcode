def isValid(s):
    results = []
    for item in s:
        if item == "(":
            results.append(")")
        elif item == "{":
            results.append("}")
        elif item == "[":
            results.append("]")
        elif not results or results.pop() != item:
            return False
    
    return not results

print(isValid("(([{}]))")) # True
print(isValid("x")) # False
print(isValid("([)]")) # False
print(isValid("()[]((()))")) # True