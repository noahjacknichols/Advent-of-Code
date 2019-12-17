
def additionalFuel(module):
    module = calc(module)

    fuelSum = module
    # print("fuelSum starts at ", fuelSum)
    while(module > 0):
        module = calc(module)
        if(module > 0):
            fuelSum+= module
        # print("+s", module)

    return fuelSum



def calc(mass): 
    requiredFuel = (mass//3) -2

    return requiredFuel



def main():
    with open('input.txt', 'r') as file:
        sum = 0
        inputLines = file.readlines()
        for line in inputLines:
            sum+= additionalFuel(int(line.strip()))
        
        print("the calculated sum was:")
        print(sum)



if __name__ == "__main__":
    main()
