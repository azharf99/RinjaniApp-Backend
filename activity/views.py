from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from activity.models import General, Food, Breast, Sleep, Hygiene, Diaper, Medicine
from activity.forms import GeneralForm, FoodForm, BreastForm, SleepForm, HygineForm, MedicineForm, DiaperForm
from rest_framework import serializers, viewsets
from rest_framework import permissions

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'date_joined']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


# General
class GeneralSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = General
        fields = ['url', 'tanggal', 'usia', 'berat_badan', 'tinggi_badan', 'suhu_tubuh', 'perkembangan', 'created_at', 'updated_at']

class GeneralViewSet(viewsets.ModelViewSet):
    queryset = General.objects.all()
    serializer_class = GeneralSerializer
    # permission_classes = [permissions.IsAuthenticated]


# Food
class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ['url', 'tanggal', 'waktu', 'makanan', 'porsi_suapan', 'durasi_makan', 'catatan_makan', 'created_at', 'updated_at']

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    # permission_classes = [permissions.IsAuthenticated]


# Breast
class BreastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breast
        fields = ['url', 'tanggal', 'waktu', 'durasi_nyusu', 'catatan_nyusu', 'created_at', 'updated_at']

class BreastViewSet(viewsets.ModelViewSet):
    queryset = Breast.objects.all()
    serializer_class = BreastSerializer
    # permission_classes = [permissions.IsAuthenticated]


# Diaper
class DiaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diaper
        fields = ['url', 'tanggal', 'waktu', 'bab', 'tekstur_bab', 'warna_bab', 'catatan_diaper', 'created_at', 'updated_at']

class DiaperViewSet(viewsets.ModelViewSet):
    queryset = Diaper.objects.all()
    serializer_class = DiaperSerializer
    # permission_classes = [permissions.IsAuthenticated]


# Hygiene
class HygieneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hygiene
        fields = ['url', 'tanggal', 'waktu', 'mandi', 'durasi_mandi', 'merk_sabun', 'jenis_air', 'gosok_kepala', 'gosok_gigi', 'gosok_lidah', 'catatan_mandi', 'created_at', 'updated_at']

class HygieneViewSet(viewsets.ModelViewSet):
    queryset = Hygiene.objects.all()
    serializer_class = HygieneSerializer
    # permission_classes = [permissions.IsAuthenticated]



# Medicine
class MedicineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medicine
        fields = ['url', 'tanggal', 'tanggal', 'waktu', 'nama_obat', 'dosis', 'manfaat', 'vaksin', 'catatan_kesehatan', 'created_at', 'updated_at']

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    # permission_classes = [permissions.IsAuthenticated]



# Sleep
class SleepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sleep
        fields = ['url', 'waktu', 'durasi_tidur', 'catatan_tidur', 'created_at', 'updated_at']

class SleepViewSet(viewsets.ModelViewSet):
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer
    # permission_classes = [permissions.IsAuthenticated]




















