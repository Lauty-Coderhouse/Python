from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='-', max_length=48),
        ),
        migrations.AddField(
            model_name='profile',
            name='surname',
            field=models.CharField(default='-', max_length=64),
        ),
    ]
