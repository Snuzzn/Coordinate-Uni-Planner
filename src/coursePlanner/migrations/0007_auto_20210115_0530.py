# Generated by Django 3.1.3 on 2021-01-15 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursePlanner', '0006_auto_20210115_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='myGrade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
