from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_img_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img_profile',
            field=models.ImageField(blank=True, default='profile_images/default-user.jpg', null=True, upload_to='profile_images'),
        ),
    ]
