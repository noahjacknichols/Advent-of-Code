
import copy
def opcode(operationPos, opcodeArray):
        # print(operationPos, opcodeArray)
    operation = opcodeArray[operationPos]
    if(operation == 1):
        # we add
        # print("add")
        pos1 = opcodeArray[operationPos+1]
        pos2 = opcodeArray[operationPos+2]
        outputPos = opcodeArray[operationPos+3]
        if(max(outputPos, pos1, pos2) > len(opcodeArray)-1):
            # opcodeArray[0] = 0
            print("invalid pos:",outputPos)
            return opcodeArray
        additiveVal = opcodeArray[pos1] + opcodeArray[pos2]
        opcodeArray[outputPos] = additiveVal
    elif(operation == 2):
        #we multiply
        # print("multiply")
        pos1 = opcodeArray[operationPos+1]
        pos2 = opcodeArray[operationPos+2]
        outputPos = opcodeArray[operationPos+3]
        if(max(outputPos, pos1, pos2) > len(opcodeArray)-1):
            # opcodeArray[0] = 0
            print("invalid pos:",outputPos)
            print("arr length:", len(opcodeArray))
            return opcodeArray
        additiveVal = opcodeArray[pos1] * opcodeArray[pos2]
        opcodeArray[outputPos] = additiveVal
    elif(operation == 99):
        #we halt
        print("program finished")
        return opcodeArray
    return opcodeArray

def main():
    with open('input2.txt', 'r') as file:
        fileInput = file.readlines()
        opcodeArray = [int(x) for x in fileInput[0].split(",")]
        original = []
        for val in opcodeArray:
            original.append(val)
        print("opcode:",opcodeArray)
        print("original:",original)
        print("array type:",type(opcodeArray))
        print("length:", len(opcodeArray)//4)
        outArr = []
        for j in range(0, 101):
            opcodeArray = copy.deepcopy(original)
            for k in range(0,101):
                print(j,k)
                opcodeArray = copy.deepcopy(original)
                opcodeArray[1] = j
                opcodeArray[2] = k
                # print("opcode:",opcodeArray)
                # print("original:",original)
                for i in range(0, len(opcodeArray),4):
                    # print(i)
                    x = opcode(i, opcodeArray)
                    if(x == ''):
                        print("opcode halted.")
                        break;
                    else:
                        opcodeArray = opcode(i, opcodeArray)

                print("opcodes pos 0 value is:", opcodeArray[0])
                outArr.append(opcodeArray[0])
                if(19690720 in outArr):
                    print("target found. noun,verb are:", (j,k))
                    return


        print("outarr:",outArr)
        if(19690720 in outArr):
            print("found")
        else:
            print("not found")


if __name__ == "__main__":
    main()