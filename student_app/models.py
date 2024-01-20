from django.db import models

class Grade(models.Model):
    grade = models.IntegerField()

    def __str__(self):
        return f"{self.grade}"

class Group(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=455)

    def __str__(self):
        return self.group_name

class Student(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=455)

    def __str__(self):
        return self.name
