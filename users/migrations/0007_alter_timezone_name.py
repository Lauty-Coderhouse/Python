from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_timezone_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timezone',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
