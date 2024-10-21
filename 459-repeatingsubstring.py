def repeatedSubstringPattern(s):
        # concat the string twice, and chop the two ends off
        # if the string still appears in concat then it's built from that substring
        return s in (s + s)[1:-1]