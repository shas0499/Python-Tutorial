lst = []
while True:
    print("Chosse Stack Operations")
    opr = int(input('''
        1. Push Element
        2. POP Element
        3. PEEK Element
        4. Display Stack
        5. Exit
    '''))
    if opr == 1:
        element = input("Enter the Element : ")
        lst.append(element)
        print(lst)

    elif opr == 2:
        if len(lst) == 0:
            print("Stack is Empty...")
            continue
        else:
            delete_element = lst.pop()
            print("Deleted Element is : ",delete_element)
            print(lst)

    elif opr == 3:
        print('Laste element in thee stack is : ',lst[-1])
    
    elif opr == 4:
        print("Stack is : ",lst)

    elif opr == 5:
        break

    else:
        print("Invalid Operation...")
        break
    print('Thank You...')