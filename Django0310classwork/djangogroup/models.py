from django.db import models

class School(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Klass(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.TextField()
    school = models.ForeignKey(School)
    def __str__(self):
        return self.name

class Lesson(models.Model):
    klass = models.ForeignKey(Klass)
    teacher = models.ForeignKey(Teacher)
    student = models.ForeignKey(Student)
    year = models.PositiveSmallIntegerField()
    def __str__(self):
        return " : ".join([
                self.klass.name,
                self.teacher.name,
                self.student.name,
                str(self.year)
        ])

class Team(models.Model):
    name = models.TextField()
    scored = models.PositiveSmallIntegerField()
    missed = models.PositiveSmallIntegerField()
    def __str__(self):
        return " : ".join([
            self.name,
            str(self.scored),
            str(self.missed)
        ])


class TableTable(models.Model):
    field = models.CharField()
