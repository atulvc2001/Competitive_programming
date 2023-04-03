if __name__ == "__main__":

    cases = int(input())
    for i in range(0, cases):
        num_a = input()
        set_a = list(map(int, input().split()))
        num_b = input()
        set_b = list(map(int, input().split()))

        if len(set_a) <= len(set_b):
            flag = 0
            try:
                for a in set_a:                                                    
                    if a not in set_b:
                        raise StopIteration
                    else:
                        flag = 1
            except StopIteration:
                flag = 0
                pass
        else:
            flag = 0

        if flag == 1:
            print("True")

        else:
            print("False")

        set_a = []
        set_b = []

        
        


