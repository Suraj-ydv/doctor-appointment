from customerapp.models import Contact, Customer_reg, Customer_pic, Customer_query, Book_appointment
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class Customer_regForm(forms.ModelForm):
    class Meta:
        model = Customer_reg
        fields = "__all__"
        # exclude = ('password',)


class Customer_picForm(forms.ModelForm):
    class Meta:
        model = Customer_pic
        fields = ['name', 'customer_Img']


class Customer_queryForm(forms.ModelForm):
    class Meta:
        model = Customer_query
        # fields = ['email','title','description','appointment_date','doctor_name']
        fields = "__all__"


class Book_appointmentForm(forms.ModelForm):
    class Meta:
        model = Book_appointment
        fields = ['customer_name', 'doctor_name', 'appointment_date', 'appointment_time', 'reason_for_appointment']


class Book_appointmentForm1(forms.ModelForm):
    class Meta:
        model = Book_appointment
        fields = ['prescription', 'reason_for_appointment', 'file']


class Book_appointmentForm2(forms.ModelForm):
    class Meta:
        model = Book_appointment
        fields = ['appointment_date', 'appointment_time']
