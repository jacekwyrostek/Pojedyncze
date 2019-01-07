import random
couponNum=int(input('Podaj iczbę kuponów: '))
i=1
while i < couponNum+1:
    myNumbers=[]
    while len(myNumbers)<7:
        newNumber=random.randint(1,49)
        if newNumber in myNumbers:
            #print('Eliminated',newNumber)
            continue
        myNumbers.append(newNumber)
    print(i,'Twoje Numery: ',myNumbers)
    input()
    i+=1
