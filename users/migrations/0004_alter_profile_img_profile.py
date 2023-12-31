from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_country_options_alter_profile_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img_profile',
            field=models.ImageField(blank=True, default='default-user.jpg', null=True, upload_to='profile_images'),
        ),
    ]
