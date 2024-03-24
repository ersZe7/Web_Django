if __name__ == '__main__':
    n = int(input())  
    student_marks = {}  

    for _ in range(n):
        name, *marks = input().split()
        marks = list(map(float, marks))
        student_marks[name] = marks
    
    query_name = input()  
    avg_score = sum(student_marks[query_name]) / len(student_marks[query_name])
    
    print("{:.2f}".format(avg_score))
