def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # normalize inputs, just to be sure
        ransomNote = ransomNote.lower()
        magazine = magazine.lower()
        # let's chew on it
        magazineCount = Counter(magazine) # build the counts of the letters
        for char in ransomNote:
            magazineCount[char] -= 1
            if magazineCount[char] < 0:
                return False
        return True