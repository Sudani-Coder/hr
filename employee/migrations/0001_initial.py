# Generated by Django 3.1.5 on 2021-01-10 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ssn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=250)),
                ('Minit', models.CharField(max_length=250)),
                ('Lname', models.CharField(max_length=250)),
                ('Bdate', models.CharField(max_length=250)),
                ('Address', models.CharField(max_length=250)),
                ('Sex', models.CharField(max_length=250)),
                ('Salary', models.CharField(max_length=250)),
                ('Super_ssn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.ssn')),
                ('dno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.dnumber')),
            ],
            options={
                'verbose_name_plural': "Emplyee's",
            },
        ),
    ]