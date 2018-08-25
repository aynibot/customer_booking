# Generated by Django 2.0 on 2018-07-12 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32, verbose_name='課程名稱')),
                ('desc', models.CharField(max_length=60, verbose_name='課程簡介')),
                ('description', models.TextField(default='', verbose_name='課程說明')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourseApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourseSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_date', models.CharField(db_index=True, max_length=32, verbose_name='開課日期')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heal.Course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('line_id', models.CharField(max_length=128, unique=True)),
                ('name', models.CharField(default='', max_length=64)),
                ('display_name', models.CharField(default='', max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='courseapply',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heal.CourseSchedule'),
        ),
        migrations.AddField(
            model_name='courseapply',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heal.Member'),
        ),
    ]
