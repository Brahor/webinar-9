class Student:
    def __init__(self, student_id, name, enrollment_date):
        self.student_id = student_id
        self.name = name
        self.enrollment_date = enrollment_date
        self.classes = []  
        self.grades = {}  

class Teacher:
    def __init__(self, teacher_id, name, hire_date):
        self.teacher_id = teacher_id
        self.name = name
        self.hire_date = hire_date
        self.classes = []  

class Subject:
    def __init__(self, subject_id, name):
        self.subject_id = subject_id
        self.name = name

class SchoolClass:
    def __init__(self, class_id, name, subject, teacher, time_schedule):
        self.class_id = class_id
        self.name = name
        self.subject = subject
        self.teacher = teacher
        self.time_schedule = time_schedule  
        self.students = []

class Classroom:
    def __init__(self, classroom_id, name, capacity):
        self.classroom_id = classroom_id
        self.name = name
        self.capacity = capacity

class Grade:
    def __init__(self, student, school_class, grade):
        self.student = student
        self.school_class = school_class
        self.grade = grade


students = []
teachers = []
subjects = []
classes = []
classrooms = []
grades = []


def add_student(student_id, name, enrollment_date):
    student = Student(student_id, name, enrollment_date)
    students.append(student)
    return student

def add_teacher(teacher_id, name, hire_date):
    teacher = Teacher(teacher_id, name, hire_date)
    teachers.append(teacher)
    return teacher

def add_subject(subject_id, name):
    subject = Subject(subject_id, name)
    subjects.append(subject)
    return subject

def add_class(class_id, name, subject_id, teacher_id, time_schedule):
    subject = next((sub for sub in subjects if sub.subject_id == subject_id), None)
    teacher = next((teach for teach in teachers if teach.teacher_id == teacher_id), None)
    if subject is not None and teacher is not None:
        school_class = SchoolClass(class_id, name, subject, teacher, time_schedule)
        classes.append(school_class)
        return school_class
    else:
        return None

def add_classroom(classroom_id, name, capacity):
    classroom = Classroom(classroom_id, name, capacity)
    classrooms.append(classroom)
    return classroom

def enroll_student_in_class(student_id, class_id):
    student = next((stu for stu in students if stu.student_id == student_id), None)
    school_class = next((cla for cla in classes if cla.class_id == class_id), None)
    if student is not None and school_class is not None:
        student.classes.append(school_class)
        school_class.students.append(student)
        return True
    else:
        return False

# testing


student1 = add_student('S001', 'Jane Fedotova', '2021-09-01')
teacher1 = add_teacher('T001', 'JohnsonUK Lelegin', '2020-08-15')
subject1 = add_subject('SUB001', 'Python')
class1 = add_class('C001', 'Algebra 101', 'SUB001', 'T001', {'Monday': '09:00-10:00', 'Wednesday': '09:00-10:00'})
classroom1 = add_classroom('CR001', 'Room 101', 30)


enrollment_success = enroll_student_in_class('S001', 'C001')

print(f"Enrollment successful: {enrollment_success}")
