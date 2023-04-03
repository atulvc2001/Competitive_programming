if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    output = student_marks[query_name]
    stu_avg = sum(output)/len(output)
    print("%.2f" %stu_avg)








	



