def count_substring(string, sub_string):
    numcount = 0
    s=sub_string
    for i in range(0,len(string)-len(s)+1):
        if string[i:len(s)+i] == s :
            numcount = numcount + 1
        


    return numcount

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
