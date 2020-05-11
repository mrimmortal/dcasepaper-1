# Generated by Django 3.0.3 on 2020-05-11 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='med_profile_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.IntegerField()),
                ('p_habbit', models.CharField(max_length=128)),
                ('p_level_of_higine', models.CharField(max_length=64)),
                ('p_cosmatic_concern', models.CharField(max_length=128)),
                ('p_medical_history', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='pat_profile_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.IntegerField()),
                ('p_name', models.CharField(max_length=64)),
                ('p_dob', models.DateField()),
                ('p_address', models.CharField(max_length=128)),
                ('p_email', models.EmailField(max_length=254)),
                ('p_mobile', models.CharField(max_length=10)),
                ('p_aniversary', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='pat_treatment_history_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.IntegerField()),
                ('d_id_treated_by', models.CharField(max_length=64)),
                ('treatment_id', models.IntegerField()),
                ('visit_date', models.DateField()),
                ('observations', models.CharField(max_length=64)),
                ('treatment_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='treatment_plan_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_id', models.IntegerField()),
                ('d_id', models.IntegerField()),
                ('treatment_name', models.CharField(max_length=128)),
                ('treatment_amount', models.IntegerField()),
            ],
        ),
    ]
