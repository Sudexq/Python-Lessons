from Teacher import Teacher

class EnglishTeacher(Teacher):

    #override
    def branch(self):
        print("The teacher's branch is English")

    def teach_verbal(self):
        print("The English teacher teaches a verbal lesson.")