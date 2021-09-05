# Generated by Django 3.1.2 on 2021-09-05 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('st_id', models.CharField(blank=True, max_length=264, null=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=264, null=True, verbose_name='Name')),
                ('age', models.CharField(blank=True, max_length=264, null=True, verbose_name='Age')),
                ('Sex', models.CharField(blank=True, max_length=30, null=True, verbose_name='Sex')),
                ('fatherName', models.CharField(blank=True, max_length=264, null=True, verbose_name='Father Name')),
                ('motherName', models.CharField(blank=True, max_length=264, null=True, verbose_name='Mother Name')),
                ('lastEducation', models.CharField(blank=True, max_length=300, null=True, verbose_name='Last Education')),
            ],
        ),
    ]