
Stack = [-1 for x in range(30)] #Initialize with a null value "-1"
TopOfStack = -1

def Push(Data):
    global Stack,TopOfStack
    if TopOfStack >= len(Stack)-1:
        return False
    else:
        TopOfStack += 1
        Stack[TopOfStack] = Data
        return True

def Pop():
    global TopOfStack,Stack
    if TopOfStack == -1:
        return -999
    else:
        Item = Stack[TopOfStack]
        TopOfStack -= 1
        return Item

#To find the greatest and the lowest value in a stack

def FindValues():
    Item1 = Pop()
    ItemArray = []
    while Item1 != -999:
        ItemArray.append(Item1)
        Item1 = Pop()
    Greatest = -1000
    Lowest = 1001
    for x in ItemArray:
        if x > Greatest:
            Greatest = x
        elif x < Lowest:
            Lowest = x
    print(f"Greatest: {Greatest}")
    print(f"Lowest: {Lowest}")