Queue = ["" for x in range(10)] #Will store strings. The length of this queue will be 10.

Head,Tail,NumOfItems = 0,0,0

def Enqueue(DataToAdd):
    global Queue,Head,Tail,NumOfItems
    if NumOfItems == 10:
        return False
    Queue[Tail] = DataToAdd
    if Tail >= 9:
        Tail = 0
    else:
        Tail += 1
    NumOfItems += 1
    return True

def Dequeue():
    global Head,NumOfItems
    if NumOfItems == 0:
        return "FALSE"
    Item = Queue[Head]
    Head += 1
    if Head >= 9:
        Head = 0
    NumOfItems -= 1
    return Item