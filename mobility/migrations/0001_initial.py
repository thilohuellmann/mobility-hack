# Generated by Django 2.1 on 2018-10-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('job_id', models.IntegerField()),
                ('supporter_id', models.IntegerField()),
                ('senior_id', models.IntegerField()),
                ('application_status', models.CharField(choices=[('applied', 'applied'), ('confirmed', 'confirmed'), ('rejected', 'rejected')], default='applied', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('senior_id', models.IntegerField()),
                ('rated', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('draft', 'draft'), ('pending', 'pending'), ('confirmed', 'confirmed'), ('done', 'done'), ('expired', 'expired')], default='draft', max_length=255)),
                ('job_type', models.CharField(choices=[('one_way', 'one_way'), ('round_trip', 'round_trip')], max_length=255)),
                ('start_time_type', models.CharField(choices=[('fixed', 'fixed'), ('flexible', 'flexible')], max_length=255, null=True)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('time_slot', models.CharField(choices=[('morning', 'morning'), ('noon', 'noon'), ('afternoon', 'afternoon'), ('evening', 'evening')], max_length=255, null=True)),
                ('supporter_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Senior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('profile_image', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female'), ('d', 'diverse')], max_length=255)),
                ('birth_date', models.DateField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('bio', models.CharField(blank=True, max_length=1200, null=True)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('profile_image', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female'), ('d', 'diverse')], max_length=255)),
                ('birth_date', models.DateField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('bio', models.CharField(max_length=1200)),
                ('phone', models.CharField(max_length=20)),
                ('radius', models.IntegerField(choices=[(1, '1km'), (2, '2km'), (5, '5km'), (10, '10km')])),
            ],
        ),
    ]