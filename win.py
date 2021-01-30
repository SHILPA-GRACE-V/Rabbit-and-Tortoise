import random
while True:
    randomlist = []
    for i in range(0, 4):
        randomlist.append(str(random.randint(0, 9)))
    print(randomlist)
    number = int(input("Enter a number:"))
    if len(str(number)) == 4:
        l = list(str(number))
        if str(randomlist) == str(l):
            print("you won!!!!")
        else:
            for i in range(4):
                if l[i] == randomlist[i]:
                    print("Rabit")
                    break
                else:
                    for k in randomlist:
                        if l[i] == k:
                            print("tortoise")
                            break
