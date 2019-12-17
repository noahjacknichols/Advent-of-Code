import copy
import sys
def findCrosses(botPath1, botPath2):
    # crossPos = []
    # for path1 in botPath1:
    #     # print(path1)
    #     for path2 in botPath2:
    #         # print(path2)
    #         if(path1 == path2):
    #             "found cross.."
    #             crossPos.append(path1)
    

    return [x for x in botPath1 if x in botPath2]


def calcPath(bot, botPath):
    botDict = {}
    totalSteps = 0
    for steps in bot:
        direction = steps[0]
        numSteps = int(steps[1:])

        print(direction, numSteps)
        for step in range(numSteps):
            if(direction == 'U'):
                newPos = copy.deepcopy(botPath[len(botPath)-1])
                newPos[1] = newPos[1] + 1
                botPath.append(newPos)
                totalSteps+=1
                pos = '' + str(newPos[0])+","+str(newPos[1])
                botDict[pos] = totalSteps
            elif(direction == 'D'):
                newPos = copy.deepcopy(botPath[len(botPath)-1])
                newPos[1] = newPos[1] - 1
                botPath.append(newPos)
                totalSteps+=1
                pos = '' + str(newPos[0])+","+str(newPos[1])
                botDict[pos] = totalSteps
            elif(direction == 'R'):
                newPos = copy.deepcopy(botPath[len(botPath)-1])
                newPos[0] = newPos[0] + 1
                botPath.append(newPos)
                totalSteps+=1
                pos = '' + str(newPos[0])+","+str(newPos[1])
                botDict[pos] = totalSteps
            
            elif(direction == 'L'):
                newPos = copy.deepcopy(botPath[len(botPath)-1])
                newPos[0] = newPos[0] - 1
                botPath.append(newPos)
                totalSteps+=1
                pos = '' + str(newPos[0])+","+str(newPos[1])
                botDict[pos] = totalSteps
    return botPath, botDict








def main():


    with open("input3.txt", 'r') as file:
        bot1 = [x.rstrip() for x in file.readline().split(",")]
        bot2 = [x.rstrip() for x in file.readline().split(",")]
        print(bot1)
        print(bot2)

        botPath1 = [[0,0]]
        botPath2 = [[0,0]]
        botPath1, dict1 = calcPath(bot1, botPath1)
        botPath2, dict2 = calcPath(bot2, botPath2)
        print("finished paths..")
        # print(dict1)
        # print(dict2)
        print(len(botPath1))

        print(len(botPath2))
        crossPos = findCrosses(botPath1, botPath2)
        print("found crosses at:", crossPos)
        sums = {}
        for pos in crossPos[1:]:
            posKey = ""+str(pos[0]) + "," + str(pos[1])
            print(pos, abs(dict1[posKey]), abs(dict2[posKey]))
            sums[posKey] = abs(dict1[posKey]) + abs(dict2[posKey])
        
        print(sums)



    return


if __name__ == "__main__":
    main()