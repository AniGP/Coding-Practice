if __name__ == '__main__':
    
    student = []
    grade = []
    names = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name, score])
        grade.append(score)

    unique_grades = set(grade)
    
    unique_grades_list = list(unique_grades)
    
    sorted_unique_grades_list = sorted(unique_grades_list)
    
    second_lowest = sorted_unique_grades_list[1]
    
    for s in student:
        if s[1] == second_lowest:
            names.append(s[0])
            names.sort()
    
    for n in names:
        print(n)
            
