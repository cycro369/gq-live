# Generated by Django 3.0 on 2020-05-22 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Grade', models.CharField(choices=[('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=200, null=True)),
                ('Section', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Grade and Sections',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('LRN', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200, null=True)),
                ('Levels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.Level')),
            ],
            options={
                'verbose_name_plural': 'Student Lists',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Filipino', models.CharField(max_length=200, null=True)),
                ('English', models.CharField(max_length=200, null=True)),
                ('Mathematics', models.CharField(max_length=200, null=True)),
                ('Science', models.CharField(max_length=200, null=True)),
                ('AP', models.CharField(max_length=200, null=True)),
                ('ESP', models.CharField(max_length=200, null=True)),
                ('TLE', models.CharField(max_length=200, null=True)),
                ('MAPEH', models.CharField(max_length=200, null=True)),
                ('GenAvg', models.CharField(max_length=200, null=True)),
                ('Status', models.CharField(choices=[('RETAINED', 'RETAINED'), ('PROMOTED', 'PROMOTED')], max_length=200, null=True)),
                ('Levels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.Level')),
                ('Student_LRN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.Student')),
            ],
            options={
                'verbose_name_plural': 'Student Grades',
                'ordering': ('-Student_LRN',),
            },
        ),
    ]
