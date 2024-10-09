def dividePlayers(skill):
        # speed things up if it's an odd number of players, we can fail this right away
        if (int(len(skill)) % 2 > 0):
            return -1

        # determine number of two-person teams and init teamSkill val
        numGroups = int(len(skill)/2)
        teamSkill = 0
        
        # how many total points do we have?
        for score in skill:
            teamSkill += score

        # divide total score by number of teams to get required points per team
        teamPoints = int(teamSkill/numGroups)
        
        # sort the array from largest to smallest
        skill.sort()

        # let's build a team
        teamList = []
        # create two pointers that start at the ends and work to the middle
        firstPointer = 0
        lastPointer = int(len(skill) - 1)
        while (firstPointer <= numGroups - 1) and (lastPointer >= numGroups):
            # start a new array teamList with the values from each pointer
            teamList.append([skill[firstPointer], skill[lastPointer]])
            # move the pointers inward
            firstPointer += 1
            lastPointer -= 1
        
        # check team sizes, return -1 if they're not equal to required team points
        count = 0
        for team in teamList:
            if (teamList[count][0] + teamList[count][1]) != teamPoints:
                    return -1
            count += 1
        
        # iterate through the teams to create the values intended to be returned
        retVal = 0
        for team in teamList:
            retVal += (team[0] * team[1])
        return retVal