class Homework(object):
    '''Class representing homework'''

    def __init__(self):
        self._grade = 0

    def __repr__(self):
        return f'{self.__class__.__name__} self.grade="{self.grade}"'

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError(
                f'Grade must be between 0 and 100 but received "{value}".')
        self._grade = value


class Grade(object):
    '''Class representing a grade.'''

    def __init__(self):
        self._values = {}

    def __repr__(self):
        return f'{self.__class__.__name__}(' + \
            f'Class representing a grade.={self.Class} representing a grade.)'

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError(
                f'Grade must be between 0 and 100 but received "{value}".')
        self._values[instance] = value


class Exam(object):
    '''Class representing an exam having many subjects, each with a separate grade.'''

    # def __init__(self):
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

    # def __repr__(self):
    #     return f'{self.__class__.__name__}' + \
    #         f''

# galileo = Homework()
# galileo.grade = 95
# print(galileo)


first_exam = Exam()
first_exam.writing_grade = 82
second_exam = Exam()
second_exam.writing_grade = 75
print(f'First {first_exam.writing_grade}')
print(f'Second {second_exam.writing_grade}')
