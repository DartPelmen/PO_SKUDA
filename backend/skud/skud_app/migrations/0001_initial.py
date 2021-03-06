# Generated by Django 3.1.3 on 2020-11-12 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('cardType', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('levelDesc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SBC',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('sbcStatus', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('userType', models.CharField(max_length=255)),
                ('userLevel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_levels', to='skud_app.level')),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('readerType', models.CharField(max_length=255)),
                ('readerStatus', models.CharField(max_length=255)),
                ('readerSbc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reared_SBCs', to='skud_app.sbc')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logDatetime', models.DateTimeField()),
                ('logAction', models.CharField(max_length=255)),
                ('logResult', models.CharField(max_length=255)),
                ('logCard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='skud_app.card')),
                ('logLevel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='skud_app.level')),
                ('logReader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readers', to='skud_app.reader')),
                ('logSbc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SBCs', to='skud_app.sbc')),
                ('logUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='skud_app.user')),
            ],
        ),
        migrations.AddField(
            model_name='level',
            name='levelReader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Level_readers', to='skud_app.reader'),
        ),
        migrations.AddField(
            model_name='card',
            name='cardUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Сard_users', to='skud_app.user'),
        ),
    ]
