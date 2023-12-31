<<<<<<< HEAD
# Generated by Django 4.2.6 on 2023-10-23 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '1) Boards (Sarlovha_boshi)',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_columns', to='home.board')),
            ],
            options={
                'verbose_name_plural': '2)Column (Sahiga qatorlari) ',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='column_task', to='home.column')),
            ],
            options={
                'verbose_name_plural': '3) Tasks (Vazifalar)',
            },
        ),
        migrations.CreateModel(
            name='Koder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kod', models.CharField(max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BoardMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_member', to='home.board')),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_inviter', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '4) Members (Chaqirilgan foydalanuvchilar)',
            },
        ),
    ]
=======
# Generated by Django 4.2.6 on 2023-10-23 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '1) Boards (Sarlovha_boshi)',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_columns', to='home.board')),
            ],
            options={
                'verbose_name_plural': '2)Column (Sahiga qatorlari) ',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='column_task', to='home.column')),
            ],
            options={
                'verbose_name_plural': '3) Tasks (Vazifalar)',
            },
        ),
        migrations.CreateModel(
            name='Koder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kod', models.CharField(max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BoardMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_member', to='home.board')),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_inviter', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '4) Members (Chaqirilgan foydalanuvchilar)',
            },
        ),
    ]
>>>>>>> d51e158 (..)
