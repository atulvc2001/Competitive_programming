if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    

    a=list(set(arr))
    l=list(sorted(a))

    print(l[-2])

