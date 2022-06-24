# Generated by Django 3.2.5 on 2021-08-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_teacher_course_year_of_admission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_attendance',
            name='Course_Code_Attendance',
            field=models.ManyToManyField(null=True, to='student.Courses'),
        ),
        migrations.AlterField(
            model_name='student_attendance',
            name='Roll_Number_Attendance',
            field=models.ManyToManyField(null=True, to='student.Student'),
        ),
        migrations.AlterField(
            model_name='student_attendance',
            name='Semester',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student_attendance',
            name='Teacher_Id_Attendance',
            field=models.ManyToManyField(null=True, to='student.Teacher'),
        ),
    ]
