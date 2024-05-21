from django import forms

from activity.models import General, Food, Breast, Diaper, Medicine, Hygiene, Sleep

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class GeneralForm(forms.ModelForm):
    class Meta:
        model = General
        fields = '__all__'
        exclude = ['tipe']
        widgets = {
            'tanggal': DateInput(),
        }

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'
        exclude = ['tipe', ]
        widgets = {
            'tanggal': DateInput(),
            'waktu': TimeInput(),
        }

class BreastForm(forms.ModelForm):
    class Meta:
        model = Breast
        fields = '__all__'
        exclude = ['tipe', ]
        widgets = {
            'tanggal': DateInput(),
            'waktu': TimeInput(),
        }

class SleepForm(forms.ModelForm):
    class Meta:
        model = Sleep
        fields = '__all__'
        exclude = ['tipe', ]
        widgets = {
            'tanggal': DateInput(),
            'waktu': TimeInput(),
        }

class HygineForm(forms.ModelForm):
    class Meta:
        model = Hygiene
        fields = '__all__'
        exclude = ['tipe', ]
        widgets = {
            'tanggal': DateInput(),
            'waktu': TimeInput(),
        }

class DiaperForm(forms.ModelForm):
    class Meta:
        model = Diaper
        fields = '__all__'
        exclude = ['tipe', ]
        widgets = {
            'tanggal': DateInput(),
            'waktu': TimeInput(),
        }

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
        exclude = ['tipe', ]
        widgets = {
            'tanggal': DateInput(),
            'waktu': TimeInput(),
        }