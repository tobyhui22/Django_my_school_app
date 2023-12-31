# Generated by Django 4.2.7 on 2023-11-01 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='className',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_Name', models.CharField(help_text='Class Name', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='school',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_Name', models.CharField(help_text='School Name', max_length=50)),
                ('school_Address', models.CharField(help_text='School Address', max_length=100)),
                ('school_tel', models.CharField(help_text='School Telephone Number', max_length=50)),
                ('school_email', models.EmailField(max_length=254)),
                ('school_type', models.CharField(choices=[('Nursery', 'Nursery & Early Years'), ('Primary', 'Primary & Junior Schools'), ('Secondary', 'Secondary Schools'), ('Independent', 'Independent Schools')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_firstName', models.CharField(help_text='Teacher First Name', max_length=20)),
                ('teacher_lastName', models.CharField(help_text='Teacher Last Name', max_length=20)),
                ('teacher_email', models.EmailField(max_length=254)),
                ('extension', models.CharField(choices=[('mr', 'Mr.'), ('ms', 'Ms.'), ('miss', 'Miss')], max_length=10)),
                ('schoolID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.school')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_firstName', models.CharField(help_text='Student First Name', max_length=20)),
                ('student_lastName', models.CharField(help_text='Student Last Name', max_length=20)),
                ('student_dateOfBirth', models.DateField()),
                ('student_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('classID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.classname')),
                ('schoolID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.school')),
            ],
        ),
        migrations.AddField(
            model_name='classname',
            name='schoolID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.school'),
        ),
    ]
