import json
import Professor
import TA
import Student


class System():

    def __init__(self):
        self.load_data()

    def load_data(self):
        self.users = self.load_user_db()
        self.courses = self.load_course_db()

    def reload_data(self):
        self.load_data()
        self.usr.all_courses = self.courses
        self.usr.users = self.users

    def load_user_db(self):
        with open('Data/users.json') as f:
            data = json.load(f)
        return data

    def load_course_db(self):
        with open('Data/courses.json') as f:
            data = json.load(f)
        return data

    def login(self,name, password):
        if self.check_password(name,password):
            role = self.users[name]['role']
            if role == 'professor':
                self.usr = Professor.Professor(name, self.users, self.courses)
            elif role == 'ta':
                self.usr = TA.TA(name, self.users, self.courses)
            elif role == 'student':
                self.usr = Student.Student(name, self.users, self.courses)

    def check_password(self, name, passwordEntered):
        password = self.users[name]['password']
        if passwordEntered == password:
            return True
        else:
            return False



if __name__ == "__main__":

    # Initializing system object and loading data from "DB"
    gradeSystem = System()

    # Logging in as a TA
    gradeSystem.login('cmhbf5', 'bestTA')
    # Changing grade of yted91
    gradeSystem.usr.change_grade('yted91', 'software_engineering', 'assignment1', 0)
    # Updating Data in system
    gradeSystem.reload_data()
    # Creating a new assignment
    gradeSystem.usr.create_assignment('assignment3', '04/01/20', 'cloud_computing')
    # Updating Data in system
    gradeSystem.reload_data()

    # Log in as Professor
    gradeSystem.login('goggins', 'augurrox')
    # # Add a new student to a course
    # gradeSystem.usr.add_student('yted91', 'databases')
    # # Updating Data
    # gradeSystem.reload_data()
    # # Remove a student from a course
    # gradeSystem.usr.drop_student('hdjsr7', 'databases')
    # Updating Data
    gradeSystem.reload_data()

    # Log in as a student
    gradeSystem.login('hdjsr7', 'pass1234')
    # Submit an assignment
    gradeSystem.usr.submit_assignment('cloud_computing', 'assignment1','Blahhhhh', '03/01/20')
    # Print the grades for software engineering
    grades = gradeSystem.usr.check_grades('software_engineering')
    print('\nGrades: ')
    print(grades)
    # Print the assignmets for databases
    assignments = gradeSystem.usr.view_assignments('databases')
    print('\nAssignments: ')
    print(assignments)
