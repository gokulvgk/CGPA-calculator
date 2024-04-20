from typing import List, Union, Dict
import shutil

# Define a type alias for a course detail
CourseDetail = List[Union[str,int]]

# Define a type alias for a semester details
SemesterDetails = List[CourseDetail]

# Define a type alias for a gradedict
GradeDict = Dict[str, int]

def get_cgpa(semester: SemesterDetails, gradedict: GradeDict) -> float:
    """
    Calculate CGPA for a given semester.

    Args:
        semester: Details of the semester including course code, name, and credits.
        gradedict: Dictionary containing grade points for each grade.

    Returns:
        CGPA for the semester.
    """
    print()
    print(f"{semester[-1][-1]:+^{console_width}}")
    print()
    total_credits: int = 0
    product_sum: int = 0
    
    for course in semester: 
        if course == semester[-1]:
            break
        while True:
            try:
                grade = input(f"Enter the grade you got in {course[1]} ({course[0]}): ").upper()
                product = gradedict[grade] * course[2]
                break
            except KeyError:
                print("Enter an appropriate grade")
                
        product_sum += product 
        total_credits += course[2]

    cgpa: float = product_sum / total_credits
    print(f"\nYour CGPA in {semester[-1][-1]} is {cgpa:.2f}")
    return cgpa

def calculate_average_cgpa(section_semesters: List[SemesterDetails], gradedict: GradeDict) -> float:
    """
    Calculate the average CGPA for a given section.

    Args:
        section_semesters: List of semester details for the section.
        gradedict: Dictionary containing grade points for each grade.

    Returns:
        Average CGPA for the section.
    """
    sum_cgpa: int = 0
    sem_count: int = 0

    for sem in section_semesters:
        cgpa = get_cgpa(sem, gradedict)
        sum_cgpa += cgpa
        sem_count += 1

    return sum_cgpa / sem_count

def main() -> None:
    """
    Main function to drive the CGPA calculator.
    """
    gradedict: GradeDict = {'S': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'E': 5, 'U': 0, 'RC': 0, 'RA': 0}
        
        # Define course details of each semester for both sections
    sem1_det: SemesterDetails=[['ELA4101','PROFESSIONAL ENGLISH AND SOFT SKILLS',3],
                              ['MAA4101', 'Matrices and Calculus', 4],
                              ['CYA4101', 'Engineering Materials', 3],
                              ['CSA4101', 'Problem Solving Using C',3],
                              ['EEB4101','introduction to Digital System',3],
                              ['GEA4131', 'Engineering Immersion Lab',0.5], 
                              ['CYA4131','Materials Chemistry Lab',1],
                              [' semester 1 ']]
    sem2_det: SemesterDetails=[['MAA4117','Analytical Mathematics ',4],
                              ['PHA4102','Engineering Physics',3],
                              ['MEA4101','Engineering graphics and computer aided design ',3],
                              ['GEA4102 ','Sustainable Engineering Systems',2],
                              ['ITB4101','Engineering and Design ',3],
                              ['ITB4117','Object Oriented Programming in Java',3],
                              ['ITB4118','Data Structures and Algorithms ',4],
                              ['GEA4131',' Engineering Immersion Lab ',0.5,],
                              ['PHA4131','Engineering Physics lab',1],
                              ['ITB4141','Data Structures and Algorithms Lab',1],
                              [' semester 2 ']]
    sem3_det: SemesterDetails=[['MAA4201', 'Partial Differential Equations and Transforms', 4],
                              ['ITB4201', 'Database Technologies', 3],
                              ['ITB4202', 'Advanced Java Programming', 4],
                              ['GEA4216', 'Professional Ethics and Life Skills', 2],
                              ['ITB4231', 'Advanced Java Programming Lab', 1],
                              ['ITB4232', 'Database Technologies Lab', 1],
                              ['ITB4233', 'Design Project - I', 2],
                              ['','Department Elective-I', 3], 
                              ['','Non Department Elective-l', 2], 
                              [' semester 3 ']]
    sem4_det: SemesterDetails=[['MAA4216', 'Probability and Statistics', 4],
                              ['ITB4216', 'Data communications and networking', 4],
                              ['ITB4217', 'Operating Systems', 4],
                              ['ITB4218', 'Web and Mobile Programming', 4],
                              ['ITB4241', 'Web and Mobile Programming Lab', 1],
                              ['ITB4242', 'System Programming Lab', 1],
                              ['ITB4243', 'Design Project - II', 2],
                              ['','Department Elective-II', 3],  
                              ['','Non Department Elective-II', 2],  
                              [' semester 4 ']]
    sem5_det: SemesterDetails=[['MAA4301', 'Optimization Techniques', 4],
                              ['ITB4301', 'Artificial Intelligence', 4],
                              ['ITB4302', 'Software Design and Modeling', 4],
                              ['ITB4303', 'Embedded System Programming', 4],
                              ['ITB4331', 'Embedded System Programming Lab', 1],
                              ['ITB4332', 'Software Design and Modeling Lab', 1],
                              ['ITB4333', 'Design Project - III', 2],
                              ['','Department Elective-III', 3],  
                              ['','Non Department Elective-III', 2],  
                              [' semester 5 ']]
    C_sem1_det: SemesterDetails=[['ELA4101','PROFESSIONAL ENGLISH AND SOFT SKILLS',3],
                                ['MAA4101', 'Matrices and Calculus', 4],
                                ['CYA4101', 'Engineering Materials', 3],
                                ['CSA4101', 'Problem Solving Using C',3],
                                ['EEB4101','introduction to Digital System',3],
                                ['GEA4131', 'Engineering Immersion Lab',0.5], 
                                ['CYA4131','Materials Chemistry Lab',1],
                                [' semester 1 ']]
    C_sem2_det: SemesterDetails=[['IBC4101',' Introduction to Open Source Software and Open Standards',2],
                                ['MAA4117','Analytical Mathematics ',4],
                                ['PHA4102','Engineering Physics',3],
                                ['ELA4101','Professional English and soft skills',3],
                                ['GEA4102 ','Sustainable Engineering Systems',2],
                                ['ITB4101','Engineering and Design ',3],
                                ['ITB4117','Object Oriented Programming in Java',3],
                                ['ITB4118','Data Structures and Algorithms ',4],
                                ['GEA4131',' Engineering Immersion Lab ',0.5,],
                                ['PHA4131','Engineering Physics lab',1],
                                [' semester 2 ']]
    C_sem3_det: SemesterDetails=[['IBS4201','Information Security Fundamentals',2],
                                ['MAA4201', 'Partial Differential Equations and Transforms', 4],
                                ['ITB4201', 'Database Technologies', 3],
                                ['ITB4202', 'Advanced Java Programming', 4],
                                ['GEA4216', 'Professional Ethics and Life Skills', 2],
                                ['ITB4231', 'Advanced Java Programming Lab', 1],
                                ['ITB4232', 'Database Technologies Lab', 1],
                                ['ITB4233', 'Design Project - I', 2], 
                                ['','Non Department Elective-l', 2], 
                                [' semester 3 ']]
    C_sem4_det: SemesterDetails=[['IBS4216','IT Physical and Systems Security ',4],
                                ['IBS4217','IT Data and Application Security ',4],
                                ['MAA4216', 'Probability and Statistics', 4],
                                ['ITB4216', 'Data communications and networking', 4],
                                ['ITB4217', 'Operating Systems', 4],
                                ['ITB4218', 'Web and Mobile Programming', 4],
                                ['ITB4241', 'Web and Mobile Programming Lab', 1],
                                ['ITB4242', 'System Programming Lab', 1],
                                ['ITB4243', 'Design Project - II', 2],  
                                ['','Non Department Elective-II', 2],  
                                [' semester 4 ']]
    C_sem5_det: SemesterDetails=[['IBC4303',' Web Programming through PHP & HTML',4],
                                ['IBS4301','IT Network Security ',4],
                                ['MAA4301', 'Optimization Techniques', 4],
                                ['ITB4301', 'Artificial Intelligence', 4],
                                ['ITB4302', 'Software Design and Modeling', 4],
                                ['ITB4303', 'Embedded System Programming', 4],
                                ['ITB4331', 'Embedded System Programming Lab', 1],
                                ['ITB4332', 'Software Design and Modeling Lab', 1],
                                ['ITB4333', 'Design Project - III', 2],  
                                ['','Non Department Elective-III', 2],  
                                [' semester 5 ']]

    general_semester_list: List[SemesterDetails] = [sem1_det, sem2_det, sem3_det, sem4_det, sem5_det]
    cybersecurity_semester_list: List[SemesterDetails] = [C_sem1_det, C_sem2_det, C_sem3_det, C_sem4_det, C_sem5_det]
    print("\t\t\t\tCGPA calculator for IT department by GOKUL KRISHNAN\n")

    while True:
        section: str = input("Select your section (Type A for general, Type B for cybersecurity): ").upper()
        if section == 'A': 
            average_cgpa: float = calculate_average_cgpa(general_semester_list, gradedict)
            break
        elif section == 'B':
            average_cgpa: float = calculate_average_cgpa(cybersecurity_semester_list, gradedict)
            break
        else:
            print("Enter a valid input")

    print(f"\nYour Average CGPA is {average_cgpa:.2f}")

console_width: int = shutil.get_terminal_size().columns

if __name__ == "__main__":
    main()
    
    while True:
        # Prompt the user to enter 'X' to exit
        print("\n" + " " * (console_width // 3) + "Enter X to exit")
        
        # Get user input and convert it to uppercase for consistency
        x: str = input().upper()
        
        # Check if the user entered 'X' to exit
        if x == 'X':
            exit(1)


