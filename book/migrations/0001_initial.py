# Generated by Django 4.1.7 on 2023-03-07 01:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorInfo',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='身份证号')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('telephone', models.CharField(max_length=20, verbose_name='联系方式')),
                ('age', models.IntegerField(default=30, verbose_name='年龄')),
                ('sex', models.CharField(default='男', max_length=2, verbose_name='性别')),
            ],
        ),
        migrations.CreateModel(
            name='BookClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='图书类别')),
            ],
        ),
        migrations.CreateModel(
            name='BookISBN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=50, verbose_name='图书ISBN')),
            ],
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='图书名称')),
                ('price', models.IntegerField(default=20, verbose_name='价格')),
                ('image',
                 models.ImageField(default='upload/default.jpg', upload_to='upload/%Y/%m', verbose_name='封面')),
                ('desc', models.CharField(default='', max_length=200, verbose_name='图书简介')),
                ('ishot', models.BooleanField(default=True, verbose_name='是否畅销')),
                ('moredesc', models.TextField(default='', verbose_name='更多介绍')),
                ('authorinfo', models.ManyToManyField(to='book.authorinfo')),
                ('bookclass', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                to='book.bookclass', verbose_name='图书类别')),
                ('bookisbn', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book.bookisbn')),
            ],
        ),
    ]
