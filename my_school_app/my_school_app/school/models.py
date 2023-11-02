from django.db import models

class school(models.Model):
    school_Name = models.CharField(max_length=50, help_text='School Name')
    school_Address = models.CharField(max_length=100, help_text='School Address')
    school_tel = models.CharField(max_length=50, help_text='School Telephone Number')
    school_email = models.EmailField()
    Typeofschool = (
        ('Nursery', 'Nursery & Early Years'),
        ('Primary', 'Primary & Junior Schools'),
        ('Secondary', 'Secondary Schools'),
        ('Independent', 'Independent Schools')
    )
    school_type = models.CharField(max_length=50, choices=Typeofschool)

    def __str__(self):
        return self.school_Name


class className (models.Model):
    class_Name = models.CharField(max_length=50, help_text='Class Name')
    schoolID = models.ForeignKey('school', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.class_Name
    
class student (models.Model):
    student_firstName = models.CharField(max_length=20, help_text='Student First Name')
    student_lastName = models.CharField(max_length=20, help_text='Student Last Name')
    student_dateOfBirth = models.DateField()
    Gen = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    student_gender = models.CharField(max_length=10, choices=Gen)
    schoolID = models.ForeignKey('school', on_delete=models.CASCADE, null=True)
    classID = models.ForeignKey('className', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.student_firstName} {self.student_lastName}"


class teacher(models.Model):
    teacher_firstName = models.CharField(max_length=20, help_text='Teacher First Name')
    teacher_lastName = models.CharField(max_length=20, help_text='Teacher Last Name')
    teacher_email = models.EmailField()
    Ext = (
        ('mr', 'Mr.'),
        ('ms', 'Ms.'),
        ('miss', 'Miss')
    )
    extension = models.CharField(max_length=10, choices=Ext)
    schoolID = models.ForeignKey('school', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.teacher_firstName} {self.teacher_lastName}"


