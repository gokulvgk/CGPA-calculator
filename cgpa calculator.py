def getcgpa(semester) -> int:
    print()
    print(f"{semester[-1][-1]:+^100}")
    print()
    totalcredits=0
    productsum=0
    for course in semester:
            if course == semester[-1]:
                break
            while True:
                try:
                    grade=input(f"Enter the grade you got in {course[1]} ({course[0]}): ").upper()
                    product=gradedict[grade]*course[2]
                    break
                except:
                    print("enter an appropriate grade")
                 
            productsum+=product 
            totalcredits+=course[2]

    print(f"your cgpa in {semester[-1][-1]} is {productsum/totalcredits}")
    return productsum/totalcredits 
    
gradedict={'S': 10,'A': 9 ,'B': 8 ,'C': 7 ,'D': 6 ,'E': 5 ,'U': 0 ,'RC': 0,'RA': 0}
sem1det=[['ELA4101','PROFESSIONAL ENGLISH AND SOFT SKILLS',3],
         ['MAA4101', 'Matrices and Calculus', 4],
         ['CYA4101', 'Engineering Materials', 3],
         ['CSA4101', 'Problem Solving Using C',3],
         ['EEB4101','introduction to Digital System',3],
         ['GEA4131', 'Engineering Immersion Lab',0.5], 
         ['CYA4131','Materials Chemistry Lab',1],
         [' semester 1 ']]
sem2det=[['MAA4117','Analytical Mathematics ',4],
         ['PHA4102','Engineering Physics',3],
         ['ELA4101','Professional English and soft skills',3],
         ['GEA4102 ','Sustainable Engineering Systems',2],
         ['ITB4101','Engineering and Design ',3],
         ['ITB4117','Object Oriented Programming in Java',3],
         ['ITB4118','Data Structures and Algorithms ',4],
         ['GEA4131',' Engineering Immersion Lab ',0.5,],
         ['PHA4131','Engineering Physics lab',1],
         [' semester 2 ']]
sem3det=[['MAA4201', 'Partial Differential Equations and Transforms', 4],
         ['ITB4201', 'Database Technologies', 3],
         ['ITB4202', 'Advanced Java Programming', 4],
         ['GEA4216', 'Professional Ethics and Life Skills', 2],
         ['','Department Elective-I', 3], 
         ['','Non Department Elective-l', 2], 
         ['ITB4231', 'Advanced Java Programming Lab', 1],
         ['ITB4232', 'Database Technologies Lab', 1],
         ['ITB4233', 'Design Project - I', 2],
         [' semester 3 ']]
sem4det=[['MAA4216', 'Probability and Statistics', 4],
        ['ITB4216', 'Data communications and networking', 4],
        ['ITB4217', 'Operating Systems', 4],
        ['ITB4218', 'Web and Mobile Programming', 4],
        ['','Department Elective-II', 3],  
        ['','Non Department Elective-II', 2],  
        ['ITB4241', 'Web and Mobile Programming Lab', 1],
        ['ITB4242', 'System Programming Lab', 1],
        ['ITB4243', 'Design Project - II', 2],
        [' semester 4 ']]
sem5det=[['MAA4301', 'Optimization Techniques', 4],
         ['ITB4301', 'Artificial Intelligence', 4],
         ['ITB4302', 'Software Design and Modeling', 4],
         ['ITB4303', 'Embedded System Programming', 4],
         ['','Department Elective-III', 3],  
         ['','Non Department Elective-III', 2],  
         ['ITB4331', 'Embedded System Programming Lab', 1],
         ['ITB4332', 'Software Design and Modeling Lab', 1],
         ['ITB4333', 'Design Project - III', 2],
         [' semester 5 ']]
C_sem1det=[['ELA4101','PROFESSIONAL ENGLISH AND SOFT SKILLS',3],
           ['MAA4101', 'Matrices and Calculus', 4],
           ['CYA4101', 'Engineering Materials', 3],
           ['CSA4101', 'Problem Solving Using C',3],
           ['EEB4101','introduction to Digital System',3],
           ['GEA4131', 'Engineering Immersion Lab',0.5], 
           ['CYA4131','Materials Chemistry Lab',1],
           [' semester 1 ']]
C_sem2det=[['IBC4101',' Introduction to Open Source Software and Open Standards',2],['MAA4117','Analytical Mathematics ',4],
           ['PHA4102','Engineering Physics',3],
           ['ELA4101','Professional English and soft skills',3],
           ['GEA4102 ','Sustainable Engineering Systems',2],
           ['ITB4101','Engineering and Design ',3],
           ['ITB4117','Object Oriented Programming in Java',3],
           ['ITB4118','Data Structures and Algorithms ',4],
           ['GEA4131',' Engineering Immersion Lab ',0.5,],
           ['PHA4131','Engineering Physics lab',1],
           [' semester 2 ']]
C_sem3det=[['IBS4201','Information Security Fundamentals',2],
           ['IBS4216','',],['MAA4201', 'Partial Differential Equations and Transforms', 4],
           ['ITB4201', 'Database Technologies', 3],
           ['ITB4202', 'Advanced Java Programming', 4],
           ['GEA4216', 'Professional Ethics and Life Skills', 2],
           ['','Department Elective-I', 3], 
           ['','Non Department Elective-l', 2], 
           ['ITB4231', 'Advanced Java Programming Lab', 1],
           ['ITB4232', 'Database Technologies Lab', 1],
           ['ITB4233', 'Design Project - I', 2],
           [' semester 3 ']]
C_sem4det=[['IBS4216','IT Physical and Systems Security ',4],
           ['IBS4217','IT Data and Application Security ',4],
           ['MAA4216', 'Probability and Statistics', 4],
           ['ITB4216', 'Data communications and networking', 4],
           ['ITB4217', 'Operating Systems', 4],
           ['ITB4218', 'Web and Mobile Programming', 4],
           ['','Department Elective-II', 3],  
           ['','Non Department Elective-II', 2],  
           ['ITB4241', 'Web and Mobile Programming Lab', 1],
           ['ITB4242', 'System Programming Lab', 1],
           ['ITB4243', 'Design Project - II', 2],
           [' semester 4 ']]
C_sem5det=[['IBC4303',' Web Programming through PHP & HTML',4],
           ['IBS4301','IT Network Security ',4],
           ['MAA4301', 'Optimization Techniques', 4],
           ['ITB4301', 'Artificial Intelligence', 4],
           ['ITB4302', 'Software Design and Modeling', 4],
           ['ITB4303', 'Embedded System Programming', 4],
           ['','Department Elective-III', 3],  
           ['','Non Department Elective-III', 2],  
           ['ITB4331', 'Embedded System Programming Lab', 1],
           ['ITB4332', 'Software Design and Modeling Lab', 1],
           ['ITB4333', 'Design Project - III', 2],
           [' semester 5 ']]

semester_list=[sem1det,sem2det,sem3det,sem4det,sem5det]
C_semester_list=[C_sem1det,C_sem2det,C_sem3det,C_sem4det,C_sem5det]
sum_cgpa=0
semcount=0
Average_cgpa=0

print("\t\t\t\tCGPA calculator for IT department by GOKUL KRISHNAN\n")
while True:
    section=input("select your section by pressing A or B\nA)general\tB)Cybersecurity\n").upper()
    if section=='A': 
        for sem in semester_list:
            cgpa =getcgpa(sem)
            sum_cgpa+=cgpa
            semcount+=1
        Average_cgpa=sum_cgpa/semcount
        break
    elif section=='B':
        for C_sem in C_semester_list:
            cgpa =getcgpa(C_sem)
            sum_cgpa+=cgpa
            semcount+=1
        Average_cgpa=sum_cgpa/semcount
        break
    else:
        print("\nEnter a valid input\n")

print()
print(f"{Average_cgpa=}")
