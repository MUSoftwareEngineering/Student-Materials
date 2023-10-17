import json
import User

class Staff(User.User):

    def update_course_db(self):
        with open('Data/courses.json', 'w') as fp:
            json.dump(self.all_courses, fp)

    def create_assignment(self,assignment_name, due_date, course):
        assignment = {
            assignment_name: {
                'due_date': due_date
            }
        }
        self.all_courses[course]['assignments'].update(assignment)
        self.update_course_db()

    def change_grade(self,user,course,assignment,grade):
        self.users[user]['courses'][course][assignment]['grade'] = 0
        self.update_user_db()

    def check_grades(self,name,course):
        assignments = self.users[name]['courses'][course]
        grades = []
        for key in assignments:
            grades.append([key, assignments[key]['grade']])
        return grades



