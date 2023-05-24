# Generated by Django 4.2 on 2023-04-18 09:55

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('looser', models.BooleanField(default=False)),
            ],
            managers=[
                ('objects', main.models.PlayerManager()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=0)),
                ('next_game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.game')),
                ('players', models.ManyToManyField(blank=True, related_name='+', to='main.player')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.player')),
            ],
            managers=[
                ('objects', main.models.GameManager()),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games', models.ManyToManyField(blank=True, related_name='+', to='main.game')),
                ('players', models.ManyToManyField(blank=True, related_name='+', to='main.player')),
            ],
            managers=[
                ('objects', main.models.CompetitionManager()),
            ],
        ),
    ]
