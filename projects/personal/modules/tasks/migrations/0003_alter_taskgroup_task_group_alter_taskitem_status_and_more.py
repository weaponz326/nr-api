# Generated by Django 4.1 on 2022-08-26 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_taskitem_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskgroup',
            name='task_group',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='taskitem',
            name='status',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='taskitem',
            name='task_item',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
