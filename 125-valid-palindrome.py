def validPalindrome(s):
    # strip it down and clean it up
    validChars = "abcdefghijklmnopqrstuvwxyz0123456789"
    s = s.lower()
    out = ""
    for x in range (0, len(s)):
        if s[x] in validChars:
            out = out + s[x]
    if out == out[::-1]:
        return True
    else:
        return False