database = [] #empty database


def addStudent(score_maths, score_english, score_computer):
#get the details for the three students, details exclude id
    if len(database) >= 3: #the database already contains 3 elements
        print("Error saving student: you cant save more than 3 students.")
        return
    
    id = len(database) + 10001
    score_maths = float(score_maths )
    score_english = float( score_english)
    score_computer = float( score_computer)
    
    new_student = { 
                        'id':id,
                        'courses':('Maths','English','Computer Science'),
                        'scores':(score_maths, score_english, score_computer)
                    }
    database.append( new_student)
    print("Student saved successfully!\n\n")
    
    


def printStudents():
    print()
    print("STUDENT IN DATABSE".center(80, "-"), end="\n\n")
    for student in database:
        print(f"Student Id: {student['id']},   Math: {student['scores'][0]},  English: {student['scores'][1]},  Computer Science: {student['scores'][2]}")
    

    
        
        
##print(dictionary["id"])  ## only prints the students id.