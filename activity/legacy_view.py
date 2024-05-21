from django.shortcuts import render, redirect

import activity.models
from activity.models import General, Food, Breast, Sleep, Hygiene, Diaper, Medicine

from activity.forms import GeneralForm, FoodForm, BreastForm, SleepForm, HygineForm, MedicineForm, DiaperForm
import datetime


# Menampilkan halaman home

def index(request):
    return render(request, 'home.html')

# Menampilkan halaman menu edit data
def edit_data(request):
    return render(request, 'edit-data.html')

# Menampilkan halaman menu delete data
def delete_data(request):
    return render(request, 'delete-data.html')

# Menampilkan halaman menu input semua data
def input_data(request):
    form_general = GeneralForm()
    form_food = FoodForm()
    form_breast = BreastForm()
    form_sleep = SleepForm()
    form_hygiene = HygineForm()
    form_diaper = DiaperForm()
    form_medicine = MedicineForm()
    context = {
        'form_general': form_general,
        'form_food': form_food,
        'form_breast': form_breast,
        'form_hygiene': form_hygiene,
        'form_diaper': form_diaper,
        'form_sleep': form_sleep,
        'form_medicine': form_medicine,
    }

    if request.method == 'POST':
        form_general = GeneralForm(request.POST)
        form_food = FoodForm(request.POST)
        form_breast = BreastForm(request.POST)
        form_sleep = SleepForm(request.POST)
        form_hygiene = HygineForm(request.POST)
        form_diaper = DiaperForm(request.POST)
        form_medicine = MedicineForm(request.POST)

        if form_general.is_valid():
            form_general.save()
        if form_breast.is_valid():
            form_breast.save()
        if form_sleep.is_valid():
            form_sleep.save()
        if form_hygiene.is_valid():
            form_hygiene.save()
        if form_diaper.is_valid():
            form_diaper.save()
        if form_medicine.is_valid():
            form_medicine.save()
        if form_food.is_valid():
            form_food.save()

    else:
        form_general = GeneralForm()
        form_food = FoodForm()
        form_breast = BreastForm()
        form_sleep = SleepForm()
        form_hygiene = HygineForm()
        form_diaper = DiaperForm()
        form_medicine = MedicineForm()

    return render(request, 'input-menu.html', context=context)
   
# Menampilkan halaman data per tanggal
def show_data(request):
    hari_ini = datetime.date.today().__format__("%Y-%m-%d")
    data = request.POST.get('data')
    try:
        data_g = General.objects.all().filter(tanggal__exact=data)
        data_f = Food.objects.all().filter(tanggal__exact=data)
        data_b = Breast.objects.all().filter(tanggal__exact=data)
        data_s = Sleep.objects.all().filter(tanggal__exact=data)
        data_h = Hygiene.objects.all().filter(tanggal__exact=data)
        data_d = Diaper.objects.all().filter(tanggal__exact=data)
        data_m = Medicine.objects.all().filter(tanggal__exact=data)
    except activity.models.General.DoesNotExist :
        data_g = None
    except activity.models.Food.DoesNotExist :
        data_f = None
    except activity.models.Breast.DoesNotExist :
        data_b = None
    except activity.models.Sleep.DoesNotExist :
        data_s = None
    except activity.models.Hygiene.DoesNotExist :
        data_h = None
    except activity.models.Diaper.DoesNotExist :
        data_d = None
    except activity.models.Medicine.DoesNotExist :
        data_m = None

    if data == None:
        poe = hari_ini
        kapan = datetime.date.fromisoformat(poe).strftime("%A, %d-%m-%Y")
    else:
        poe = data
        kapan = datetime.date.fromisoformat(poe).strftime("%A, %d-%m-%Y")

    context = {
        'today': hari_ini,
        'poe' : kapan,
        'data_g': data_g,
        'data_f': data_f,
        'data_b': data_b,
        'data_s': data_s,
        'data_h': data_h,
        'data_d': data_d,
        'data_m': data_m,
    }

    return render(request, 'show_data.html', context=context)

# Menampilkan halaman umum
def general(request):
    datas = General.objects.order_by('-tanggal')
    form = GeneralForm()
    context = {
        'datas': datas,
        'form': form,
    }

    if request.method == 'POST':
        form = GeneralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('general')
    else:
        form = GeneralForm()

    return render(request, 'general.html', context=context)

# Menampilkan halaman detail umum
def general_detail(request, pk):
    detail = General.objects.get(id=pk)
    context = {
        'detail': detail,
    }
    return render(request, 'general_detail.html', context=context)

# Menampilkan halaman edit umum
def general_edit(request, pk):
    data = General.objects.get(id=pk)
    form = GeneralForm(instance=data)
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = GeneralForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('general')

    return render(request, 'form-edit.html', context=context)

# Menampilkan halaman delete umum
def general_delete(request, pk):
    data = General.objects.get(id=pk)
    context = {
        'data': data,
    }
    if request.method == 'POST':
        data.delete()
        return redirect('general')
    return render(request, 'form-delete.html', context=context) 

# Menampilkan halaman makanan
def food(request):
    datas = Food.objects.order_by('-tanggal', '-waktu')
    form = FoodForm()
    context = {
        'datas': datas,
        'form': form,
    }
    if request.method == 'POST':
        tanggal = request.POST.get('tanggal')
        waktu = request.POST.get('waktu')
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food')
    else:
        form = FoodForm()
    return render(request, 'food.html', context=context)

# Menampilkan halaman detail makanan
def food_detail(request, pk):
    detail = Food.objects.get(id=pk)
    context = {
        'detail': detail,
    }
    return render(request, 'food_detail.html', context=context)

# Menampilkan halaman edit makanan
def food_edit(request, pk):
    data = Food.objects.get(id=pk)
    print(data)
    form = FoodForm(instance=data)
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = FoodForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('food')

    return render(request, 'form-edit.html', context=context)

# Menampilkan halaman delete makanan
def food_delete(request, pk):
    data = Food.objects.get(id=pk)
    context = {
        'data': data,
    }
    if request.method == 'POST':
        data.delete()
        return redirect('food')
    return render(request, 'form-delete.html', context=context) 

# Menampilkan halaman menyusui
def breast(request):
    datas = Breast.objects.order_by('-tanggal', '-waktu')
    form = BreastForm()
    context = {
        'datas': datas,
        'form': form,
    }
    if request.method == 'POST':
        form = BreastForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('breast')
    else:
        form = BreastForm()

    return render(request, 'breast.html', context=context)

# Menampilkan halaman detail menyusui
def breast_detail(request, pk):
    detail = Breast.objects.get(id=pk)
    context = {
        'detail': detail,
    }
    return render(request, 'breast_detail.html', context=context)

# Menampilkan halaman edit menyusui
def breast_edit(request, pk):
    data = Breast.objects.get(id=pk)
    print(data)
    form = BreastForm(instance=data)
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = BreastForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('breast')

    return render(request, 'form-edit.html', context=context)

# Menampilkan halaman delete menyusui
def breast_delete(request, pk):
    data = Breast.objects.get(id=pk)
    context = {
        'data': data,
    }
    if request.method == 'POST':
        data.delete()
        return redirect('breast')
    return render(request, 'form-delete.html', context=context) 

# Menampilkan halaman  tidur
def sleep(request):
    datas = Sleep.objects.order_by('-tanggal', '-waktu')
    form = SleepForm()
    context = {
        'datas': datas,
        'form': form,
    }
    if request.method == 'POST':
        form = SleepForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sleep')
    else:
        form = SleepForm()
    return render(request, 'sleep.html', context=context)

# Menampilkan halaman detail tidur
def sleep_detail(request, pk):
    detail = Sleep.objects.get(id=pk)
    context = {
        'detail': detail,
    }
    return render(request, 'sleep_detail.html', context=context)

# Menampilkan halaman edit tidur
def sleep_edit(request, pk):
    data = Sleep.objects.get(id=pk)
    print(data)
    form = SleepForm(instance=data)
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = SleepForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('sleep')

    return render(request, 'form-edit.html', context=context)

# Menampilkan halaman delete tidur
def sleep_delete(request, pk):
    data = Sleep.objects.get(id=pk)
    context = {
        'data': data,
    }
    if request.method == 'POST':
        data.delete()
        return redirect('sleep')
    return render(request, 'form-delete.html', context=context) 

# Menampilkan halaman popok
def diaper(request):
    datas = Diaper.objects.order_by('-tanggal', '-waktu')
    form = DiaperForm()
    context = {
        'datas': datas,
        'form': form,
    }
    if request.method == 'POST':
        form = DiaperForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diaper')
    else:
        form = DiaperForm()
    return render(request, 'diaper.html', context=context)

# Menampilkan halaman detail tidur
def diaper_detail(request, pk):
    detail = Diaper.objects.get(id=pk)
    context = {
        'detail': detail,
    }
    return render(request, 'diaper_detail.html', context=context)

# Menampilkan halaman edit tidur
def diaper_edit(request, pk):
    data = Diaper.objects.get(id=pk)
    print(data)
    form = DiaperForm(instance=data)
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = DiaperForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('diaper')

    return render(request, 'form-edit.html', context=context)

# Menampilkan halaman delete tidur
def diaper_delete(request, pk):
    data = Diaper.objects.get(id=pk)
    context = {
        'data': data,
    }
    if request.method == 'POST':
        data.delete()
        return redirect('diaper')
    return render(request, 'form-delete.html', context=context) 

# Menampilkan halaman kesehatan
def medicine(request):
    datas = Medicine.objects.order_by('-tanggal', '-waktu')
    form = MedicineForm()
    context = {
        'datas': datas,
        'form': form,
    }
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine')
    else:
        form = MedicineForm()
    return render(request, 'medicine.html', context=context)

# Menampilkan halaman detail kesehatan
def medicine_detail(request, pk):
    detail = Medicine.objects.get(id=pk)
    context = {
        'detail': detail,
    }
    return render(request, 'medicine_detail.html', context=context)

# Menampilkan halaman edit kesehatan
def medicine_edit(request, pk):
    data = Medicine.objects.get(id=pk)
    print(data)
    form = MedicineForm(instance=data)
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('medicine')

    return render(request, 'form-edit.html', context=context)

# Menampilkan halaman delete kesehatan
def medicine_delete(request, pk):
    data = Medicine.objects.get(id=pk)
    context = {
        'data': data,
    }
    if request.method == 'POST':
        data.delete()
        return redirect('medicine')
    return render(request, 'form-delete.html', context=context) 
