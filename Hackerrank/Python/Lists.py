if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(0,N):
        command = str(input()).split()  # [insert, 0, 5]
            # command is an array
        
        if command[0] == "insert":
            i = int(command[1])
            e = int(command[2])
            arr.insert(i,e)

        elif command[0] == "print":
            print(arr)

        elif command[0] == "remove":
            i = int(command[1])
            arr.remove(i)

        elif command[0] == "append":
            i = int(command[1])
            arr.append(i)

        elif command[0] == "sort":
            arr.sort()

        elif command[0] == "pop":
            arr.pop()

        elif command[0] == "reverse":
            arr.reverse()
