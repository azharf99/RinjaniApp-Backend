# Generated by Django 5.0.6 on 2024-05-15 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipe', models.CharField(default='Menyusui', max_length=20)),
                ('tanggal', models.DateField()),
                ('waktu', models.TimeField()),
                ('durasi_nyusu', models.FloatField()),
                ('catatan_nyusu', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Breast',
                'verbose_name_plural': 'Breasts',
                'db_table': 'activity_breast',
                'ordering': ['-tanggal', '-waktu'],
                'indexes': [models.Index(fields=['id'], name='activity_br_id_0463b9_idx')],
            },
        ),
        migrations.CreateModel(
            name='Diaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipe', models.CharField(default='Popok', max_length=20)),
                ('tanggal', models.DateField()),
                ('waktu', models.TimeField()),
                ('bab', models.CharField(choices=[('Yes', 'Ya'), ('No', 'Tidak')], default='No', max_length=3)),
                ('tekstur_bab', models.CharField(blank=True, max_length=100)),
                ('warna_bab', models.CharField(blank=True, max_length=100)),
                ('catatan_diaper', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Diaper',
                'verbose_name_plural': 'Diapers',
                'db_table': 'activity_diaper',
                'ordering': ['-tanggal', '-waktu'],
                'indexes': [models.Index(fields=['id'], name='activity_di_id_9442e1_idx')],
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipe', models.CharField(default='Makan', max_length=20)),
                ('tanggal', models.DateField()),
                ('waktu', models.TimeField()),
                ('makanan', models.CharField(max_length=200)),
                ('porsi_suapan', models.FloatField()),
                ('durasi_makan', models.FloatField(blank=True)),
                ('catatan_makan', models.TextField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name': 'Food',
                'verbose_name_plural': 'Foods',
                'db_table': 'activity_food',
                'ordering': ['-tanggal', '-waktu'],
                'indexes': [models.Index(fields=['id'], name='activity_fo_id_809af9_idx')],
            },
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipe', models.CharField(default='Umum', max_length=20)),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('usia', models.IntegerField(help_text='dalam Bulan')),
                ('berat_badan', models.FloatField()),
                ('tinggi_badan', models.FloatField()),
                ('suhu_tubuh', models.FloatField(blank=True)),
                ('perkembangan', models.TextField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'General',
                'verbose_name_plural': 'Generals',
                'db_table': 'activity_general',
                'ordering': ['-tanggal'],
                'indexes': [models.Index(fields=['id'], name='activity_ge_id_30292f_idx')],
            },
        ),
        migrations.CreateModel(
            name='Hygiene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipe', models.CharField(default='Mandi', max_length=20)),
                ('tanggal', models.DateField()),
                ('waktu', models.TimeField()),
                ('mandi', models.CharField(choices=[('Morning', 'Pagi'), ('Evening', 'Sore'), ('Emergency', 'Darurat')], max_length=10)),
                ('durasi_mandi', models.FloatField(blank=True)),
                ('merk_sabun', models.CharField(max_length=50)),
                ('jenis_air', models.CharField(choices=[('Normal', 'Dingin'), ('Warm', 'Hangat')], default='Warm', max_length=6)),
                ('gosok_kepala', models.CharField(choices=[('Yes', 'Ya'), ('No', 'Tidak')], default='Yes', max_length=3)),
                ('gosok_gigi', models.CharField(choices=[('Yes', 'Ya'), ('No', 'Tidak')], default='Yes', max_length=3)),
                ('gosok_lidah', models.CharField(choices=[('Yes', 'Ya'), ('No', 'Tidak')], default='Yes', max_length=3)),
                ('catatan_mandi', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Hygiene',
                'verbose_name_plural': 'Hygienes',
                'db_table': 'activity_hygiene',
                'ordering': ['-tanggal', '-waktu'],
                'indexes': [models.Index(fields=['id'], name='activity_hy_id_ad883e_idx')],
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipe', models.CharField(default='Obat', max_length=20)),
                ('tanggal', models.DateField()),
                ('waktu', models.TimeField()),
                ('nama_obat', models.CharField(max_length=100)),
                ('dosis', models.CharField(max_length=100)),
                ('manfaat', models.CharField(max_length=200)),
                ('vaksin', models.CharField(choices=[('Yes', 'Ya'), ('No', 'Tidak')], default='Yes', max_length=3)),
                ('catatan_kesehatan', models.TextField(default='Alhamdlillah Sehat', max_length=300)),
            ],
            options={
                'verbose_name': 'Medicine',
                'verbose_name_plural': 'Medicines',
                'db_table': 'activity_medicine',
                'ordering': ['-tanggal', '-waktu'],
                'indexes': [models.Index(fields=['id'], name='activity_me_id_75c486_idx')],
            },
        ),
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipe', models.CharField(default='Tidur', max_length=20)),
                ('tanggal', models.DateField()),
                ('waktu', models.TimeField()),
                ('durasi_tidur', models.FloatField()),
                ('catatan_tidur', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Sleep',
                'verbose_name_plural': 'Sleeps',
                'db_table': 'activity_sleep',
                'ordering': ['-tanggal', '-waktu'],
                'indexes': [models.Index(fields=['id'], name='activity_sl_id_8c5d77_idx')],
            },
        ),
    ]