class Student(object):
    def Student(self, fullName, lastName, group, avarageMark, sciWork):
        self.fullName = fullName
        self.lastName = lastName
        self.group = group
        self.avarageMark = avarageMark


    def getScholarship(self, stipend):
        if self.avarageMark == 5:
            stipend = 100
        else:
            stipend = 80
        return "%s иммеет стипедию в размере %s" % (self.fullName, stipend)

class Aspirant(Student):
    def getScholarship(self, stipend):
        if self.avarageMark == 5:
            stipend = 200
        else:
            stipend = 180
        return "%s иммеет стипедию в размере %s" % (self.fullName, stipend)

if __name__ == "__main__":
    student = [
        ["Ihor", "Yushchuk", "SA", 3, False],
        ["Andrew", "Lototskiy", "SA", 5, True],
        ["Alex", "Polishchuk", "SA", 5, False],
        ["Dmitriy", "Polishchuk", "SA", 4, True]]
    try:
        for i in range(len(student)):
            if student[i][4] == True:
                s = Aspirant()
                s.Student(student[i][0], student[i][1], student[i][2], student[i][3], student[i][4])
                print(s.getScholarship(stipend = 0))
            elif student[i][4] == False:
                s = Student()
                s.Student(student[i][0], student[i][1], student[i][2], student[i][3], student[i][4])
                print(s.getScholarship(stipend = 0))
    except:
        print("Введені невірні дані!!!")
    

