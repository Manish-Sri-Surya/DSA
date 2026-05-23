students=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name= input()
        score= float(input())
        students.append([name,score])
    scores=[]
    for student in students:
        scores.append(student[1])
    unique_scores=list(set(scores))
    unique_scores.sort()
    second_lowest=unique_scores[1]
    names=[]
    for student in students:
        if student[1]==second_lowest:
            names.append(student[0])
    names.sort()
    
    for name in names:
        print(name)
            
