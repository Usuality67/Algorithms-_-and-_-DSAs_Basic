Queue = ["" for x in range(100)] #Will store strings and the length of this queue will be 100
QueueHead,QueueTail = -1,-1
NumberOfItems = 0 #Items in a queue-number

def Enqueue(DataItem):
    global Queue,QueueTail,QueueHead,NumberOfItems
    if NumberOfItems == len(Queue):
        return False
    else:
        QueueTail += 1
        if QueueHead == -1:
            QueueHead += 1
        Queue[QueueTail] = DataItem
        NumberOfItems += 1
        return True
def Dequeue():
    global Queue,QueueHead,NumberOfItems,QueueTail
    if NumberOfItems == 0:
        return "False"
    else:
        Item = Queue[QueueHead]
        QueueHead += 1
        NumberOfItems -= 1
        if NumberOfItems == 0:
            QueueHead,QueueTail = -1,-1
        return Item