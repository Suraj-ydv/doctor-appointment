from doctorapp.models import Doctor_reg, Add_schedule,Doctor_pic
from django import forms


class Doctor_regForm(forms.ModelForm):
    class Meta:
        model = Doctor_reg
        fields = "__all__"


class Add_scheduleForm(forms.ModelForm):
    class Meta:
        model = Add_schedule
        fields = "__all__"


class Doctor_picForm(forms.ModelForm):
    class Meta:
        model = Doctor_pic
        fields = ['name', 'doctor_Img']