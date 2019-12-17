

def validPassword(pw):
    if(len(pw) == 6):
        pairFlag = False
        doubleFlag = False
        increasingFlag = True
        for i in range(1,len(pw)):
            if(int(pw[i]) < int(pw[i-1])):
                increasingFlag = False
        numbersSeen = []
        for i in range(1, len(pw)-1, 2):
            if(pw[i] == pw[i-1]):
                pairFlag = True
                if(pairFlag == True and pw[i] in numbersSeen and pw.count(pw[i]) > 2):
                    print(pw)
                    return False
                numbersSeen.append(pw[i])
                
        
        if(pairFlag == True and increasingFlag == True):
            return True
    return False


def countValidPasswords(passwords):
    validPasswords = 0

    for pw in passwords:
        if(validPassword(pw)):
            validPasswords+=1
        # else:
        #     print(pw)
    
    return validPasswords

def main():
    minRange = 124075
    maxRange = 580769

    passwords = []
    for i in range(minRange, maxRange+1, 1):
        passwords.append(str(i))


    
    # print("passwords are:", passwords)
    count = countValidPasswords(passwords)

    print("the count of valid passwords is:", count)





if __name__ == "__main__":
    main()