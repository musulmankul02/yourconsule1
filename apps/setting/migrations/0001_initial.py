# Generated by Django 4.2 on 2024-02-25 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.TextField(verbose_name='Первое описание')),
                ('desscriptions2', models.TextField(verbose_name='Второе описание')),
                ('image', models.ImageField(upload_to='about_image', verbose_name='Фотография')),
                ('experience', models.CharField(max_length=255, verbose_name='опыт')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Обратные связи',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years', models.CharField(max_length=255, verbose_name='Год')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='history_image', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Наши истории',
                'verbose_name_plural': 'Наша история',
            },
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clients', models.CharField(max_length=255, verbose_name='Активные клиенты')),
                ('review', models.CharField(max_length=255, verbose_name='Положительных отзывов')),
                ('team', models.CharField(max_length=255, verbose_name='Юристов')),
            ],
            options={
                'verbose_name': 'Мы в числах',
                'verbose_name_plural': 'Мы в числах',
            },
        ),
    ]
