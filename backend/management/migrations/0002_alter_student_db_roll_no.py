# Generated by Django 4.1.3 on 2022-11-28 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_db',
            name='roll_no',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
