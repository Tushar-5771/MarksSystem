# Generated by Django 3.0.8 on 2020-07-19 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MidData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ErNo', models.CharField(max_length=20)),
                ('advancePython', models.IntegerField(blank=True, default=0, null=True)),
                ('PDC', models.IntegerField()),
                ('SE', models.IntegerField()),
                ('WDD', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
