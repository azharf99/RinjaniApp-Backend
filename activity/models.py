from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils import timezone

# Create your models here.
class Choice(models.TextChoices):
    YES = 'Yes', "Ya"
    NO = 'No', "Tidak"

class General(models.Model):
    tipe = models.CharField(max_length=20, default="Umum")
    tanggal = models.DateField()
    usia = models.IntegerField(help_text="dalam Bulan")
    berat_badan = models.FloatField()
    tinggi_badan = models.FloatField()
    suhu_tubuh = models.FloatField(blank=True)
    perkembangan = models.TextField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"Data {self.tipe} {self.tanggal}"
    

    def get_absolute_url(self):
        return reverse('general')

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("General")
        verbose_name_plural = _("Generals")
        ordering = ["-tanggal"]
        db_table = "activity_general"


class Food(models.Model):
    tipe = models.CharField(max_length=20, default="Makan")
    tanggal = models.DateField()
    waktu = models.TimeField()
    makanan = models.CharField(max_length=200)
    porsi_suapan = models.FloatField()
    durasi_makan = models.FloatField(blank=True)
    catatan_makan = models.TextField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"Data {self.tipe} {self.tanggal} {self.waktu}"
    
    def get_absolute_url(self):
        return reverse('food')

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Food")
        verbose_name_plural = _("Foods")
        ordering = ["-tanggal", "-waktu"]
        db_table = "activity_food"


class Breast(models.Model):
    tipe = models.CharField(max_length=20, default="Menyusui")
    tanggal = models.DateField()
    waktu = models.TimeField()
    durasi_nyusu = models.FloatField()
    catatan_nyusu = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"Data {self.tipe} {self.tanggal} {self.waktu}"
    
    def get_absolute_url(self):
        return reverse('breast')

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Breast")
        verbose_name_plural = _("Breasts")
        ordering = ["-tanggal", "-waktu"]
        db_table = "activity_breast"


class Sleep(models.Model):
    tipe = models.CharField(max_length=20, default="Tidur")
    tanggal = models.DateField()
    waktu = models.TimeField()
    durasi_tidur = models.FloatField()
    catatan_tidur = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"Data {self.tipe} {self.tanggal} {self.waktu}"
    
    def get_absolute_url(self):
        return reverse('sleep')

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Sleep")
        verbose_name_plural = _("Sleeps")
        ordering = ["-tanggal", "-waktu"]
        db_table = "activity_sleep"



class Hygiene(models.Model):
    class Water(models.TextChoices):
        NORMAL = 'Normal', "Dingin"
        WARM = 'Warm', "Hangat"

    class Bath(models.TextChoices):
        MORNING = 'Morning', "Pagi"
        EVENING = 'Evening', "Sore"
        EMERGENCY = 'Emergency', "Darurat"

    tipe = models.CharField(max_length=20, default="Mandi")
    tanggal = models.DateField()
    waktu = models.TimeField()
    mandi = models.CharField(max_length=10, choices=Bath.choices)
    durasi_mandi = models.FloatField(blank=True)
    merk_sabun = models.CharField(max_length=50)
    jenis_air = models.CharField(max_length=6, choices=Water.choices, default=Water.WARM)
    gosok_kepala = models.CharField(max_length=3, choices=Choice.choices, default=Choice.YES)
    gosok_gigi = models.CharField(max_length=3, choices=Choice.choices, default=Choice.YES)
    gosok_lidah = models.CharField(max_length=3, choices=Choice.choices, default=Choice.YES)
    catatan_mandi = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"Data {self.tipe} {self.tanggal} {self.waktu}"
    
    def get_absolute_url(self):
        return reverse('hygiene')

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Hygiene")
        verbose_name_plural = _("Hygienes")
        ordering = ["-tanggal", "-waktu"]
        db_table = "activity_hygiene"



class Diaper(models.Model):
    tipe = models.CharField(max_length=20, default="Popok")
    tanggal = models.DateField()
    waktu = models.TimeField()
    bab = models.CharField(max_length=3, choices=Choice.choices, default=Choice.NO)
    tekstur_bab = models.CharField(max_length=100, blank=True)
    warna_bab = models.CharField(max_length=100, blank=True)
    catatan_diaper = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"Data {self.tipe} {self.tanggal} {self.waktu}"
    
    def get_absolute_url(self):
        return reverse('diaper')

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Diaper")
        verbose_name_plural = _("Diapers")
        ordering = ["-tanggal", "-waktu"]
        db_table = "activity_diaper"



class Medicine(models.Model):
    tipe = models.CharField(max_length=20, default="Obat")
    tanggal = models.DateField()
    waktu = models.TimeField()
    nama_obat = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    manfaat = models.CharField(max_length=200)
    vaksin = models.CharField(max_length=3, choices=Choice.choices, default=Choice.YES)
    catatan_kesehatan = models.TextField(max_length=300, default="Alhamdlillah Sehat")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"Data {self.tipe} {self.tanggal} {self.waktu}"
    
    def get_absolute_url(self):
        return reverse('medicine')

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Medicine")
        verbose_name_plural = _("Medicines")
        ordering = ["-tanggal", "-waktu"]
        db_table = "activity_medicine"