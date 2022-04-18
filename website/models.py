from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, account_id, account_type, email, username, enc_password):
        self.account_id = account_id
        self.account_type = account_type
        self.username = username
        self.email = email
        self.enc_password = enc_password

    def get_id(self):
        return str(self.account_id)


class Student:
    def __init__(self, student_id, firstname, lastname, join_date, account_id, enrolled):
        self.student_id = student_id
        self.firstname = firstname
        self.lastname = lastname
        self.join_date = join_date
        self.account_id = account_id
        self.enrolled = enrolled


class Teacher:
    def __init__(self, teacher_id, firstname, lastname, join_date, account_id, created_courses):
        self.teacher_id = teacher_id
        self.firstname = firstname
        self.lastname = lastname
        self.join_date = join_date
        self.account_id = account_id
        self.created_courses = created_courses


class Course:
    def __init__(self, course_id, course_title, category, description, teacher, rating):
        self.course_id = course_id
        self.course_title = course_title
        self.category = category
        self.description = description
        self.teacher = teacher
        self.rating = rating


class Content:
    def __init__(self, content_id, content_title, link, course_id, teacher_id):
        self.content_id = content_id
        self.content_title = content_title
        self.link = link
        self.course_id = course_id
        self.teacher_id = teacher_id


class Assessment:
    def __init__(self, assessment_id, assessment_title, teacher_id):
        self.assessment_id = assessment_id
        self.assessment_title = assessment_title
        self.teacher_id = teacher_id


class Question:
    def __init__(self, text, option1, option2, option3, option4, correct):
        self.text = text
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correct = correct


class Comment:
    def __init__(self):
        pass


class Feedback:
    def __init__(self):
        pass
