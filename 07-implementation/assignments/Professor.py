import json
import Staff


class Professor(Staff.Staff):
    def __init__(self, name,users,courses):
        self.users = users
        self.all_courses = courses
        self.name = name
        self.courses = self.users[name]['courses']
        self.password = self.users[name]['password']

    def add_student(self, name, course):
        assignments = self.all_courses[course]['assignments']
        for key in assignments:
            assignments[key]['grade'] = "N/A"
            assignments[key]['submission_date'] = "N/A"
            assignments[key]['submission'] = "N/A"
            assignments[key]['ontime'] = "N/A"
            del assignments[key]['due_date']
        self.users[self.name]['courses'][course] = assignments
        self.update_user_db()

    def drop_student(self, name, course):
        del self.users[name]['courses'][course]
        self.update_user_db()


