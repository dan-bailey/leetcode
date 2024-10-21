def strStr(haystack, needle):
        idx = []
        t = len(needle)
        h = len(haystack)
        found = False
        for x in range (0, (h - t + 1)):
            if (haystack[x:x+t] == needle):
                idx.append(x)
                found = True
        if found == False:
            return -1
        else:
            return idx[0]