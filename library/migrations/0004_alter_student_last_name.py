# Generated by Django 5.0.2 on 2024-03-02 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_student_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
