from django.db import models

# Create your models here.
class school(models.Model):
    id=models.AutoField(primary_key=True)
    schoolName=models.CharField(max_length=350)
    location=models.CharField(max_length=60)
    SchoolType=models.CharField(max_length=100)

    def __str__(self):
        return self.schoolName
    
class student(models.Model):
    id=models.AutoField(primary_key=True)
    StudentName=models.CharField(max_length=50)
    Age=models.IntegerField()
    level=models.CharField(max_length=60)
    school=models.ForeignKey(school, on_delete=models.CASCADE,related_name="Student",null=True)

    def __str__(self):
        return self.StudentName
    