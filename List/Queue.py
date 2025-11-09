lst = []
while True:
    print("Choose Queue operations")
    opr = int(input('''
        1. Enqueue Element
        2. Dequeue Element
        3. Front Element
        4. Rear Element
        5. Display Queue
        6. Exit
    '''))
    if opr == 1:
        element = input("Enter the Element : ")
        lst.append(element)
        print(lst)

    elif opr == 2:
        if len(lst) == 0:
            print("Queue is Empty...")
            continue
        else:
            del lst[0]
            print(lst)
    
    elif opr == 3:
        if len(lst) == 0:
            print("Queue is Empty...")
            continue
        else:
            print("Front Element is : ",lst[0])

    elif opr == 4:
        if len(lst) == 0:
            print("Queue is Empty...")
            continue
        else:
            print("Rear Element is : ",lst[-1])

    elif opr == 5:
        print("Queue is : ",lst)

    elif opr == 6:
         break
    
    else:
        print("Invalid Operation...")
        break