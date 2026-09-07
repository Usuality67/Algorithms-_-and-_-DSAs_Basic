def gcd(n1,n2):

    remainder = n2 % n1 #CALCULATING REMAINDER


    number_store = n1 #MAKING A VARIABLE TO STORE THE SUBSEQUENT NUMBERS I.E NUMERATORS
    remainder_store = remainder #STORING THE SUBSEQUENT REMAINDERS, THIS WOULD LATER ACT AS A DENOMINATOR I.E DIVISOR
    if remainder_store == 0: #CHECKING IF REMAINDERS ARE ALREADY ZERO; IF YES THEN EXIT THE PROGRAM AND JUST RETURN THE NUMERATOR AS THATS THE GCD.

        return number_store


    while remainder_store > 0:  #LOOPING CONDITION TO MAKE SURE REMAINDERS I.E DENOMINATORS REMAIN > 0 , AND NOT TO BE 0 AS THAT COULD CAUSE ERRORS.

        remainder = number_store % remainder_store #SOUL OF THIS ALGORITHM , so just do long division with the number_store (previous remainder) as dividend and remainder store (previous remainder) as divisor. You would obtain the current remainder by doing so .



        number_store, remainder_store = remainder_store, remainder #JUST BASIC ASSIGNMENT , MAKE THE DIVISOR ( PREVIOUS REMAINDER ) YOUR DIVIDEND , AND THE REMAINDER YOU JUST FOUND ABOVE WOULD BE YOUR NEW DIVISOR.





    return  number_store #WHEN YOU HIT ZERO, JUST RETURN THE NUMBER STORED I.E DIVIDEND , because that is our GCD, since MOD by 0 is not possible ( remainder is 0 )


def BinarySearch(Arr,First,Last,ToFind):
    Mid = 0
    Flag = False
    while First != Last and not Flag:
        Mid = (First + Last) // 2
        if Arr[Mid] > ToFind:
            Last = Mid-1
        elif Arr[Mid] < ToFind:
            First = Mid + 1
        else:
            Flag = True
    if Flag:
        print(f"Item found at: {Mid}")


def Recursive(Arr,First,Last,ToFind):
    if First == Last:
        return -1
    else:
        Mid = (First+Last) // 2
        if Arr[Mid] > ToFind:
            return Recursive(Arr,First,Mid-1,ToFind)
        elif Arr[Mid] < ToFind:
            return Recursive(Arr,Mid+1,Last,ToFind)

        return Mid


def Insertion(Arr):
    for x in range(1,len(Arr)):
        hole = x
        value = Arr[x]
        while hole > 0 and value < Arr[hole-1]:
            Arr[hole] = Arr[hole-1]
            hole -= 1

        Arr[hole] = value
    return Arr


def Bubble(Arr):
    for x in range(len(Arr)):
        swap = False
        for y in range(len(Arr)-x-1):

            if Arr[y] > Arr[y+1]:
                Arr[y],Arr[y+1] = Arr[y+1],Arr[y]
                swap = True
        if not swap:
            break
    



