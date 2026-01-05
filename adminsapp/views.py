from django.shortcuts import render, redirect
from adminsapp.models import Admins, Add_news
from customerapp.models import Customer_reg, Customer_query, Book_appointment
from doctorapp.models import Doctor_reg
from adminsapp.forms import Add_newsForm
import datetime


# form adminsapp.forms import AdminsForm

# Create your views here.
def admins(request):
    if request.method == "POST":
        u_name = request.POST["username"]
        pwd = request.POST["password"]
        request.session["username"] = u_name
        try:
            form = Admins.objects.get(username=u_name, password=pwd)
            return render(request, "admins_home.html", {"form": form})
        except Exception as e:
            print(e)
            return render(request, "admins.html", {"msg": "Sorry!...your are entered invalid credentials"})
    return render(request, "admins.html", {})


def admins_logout(request):
    request.session["username"] = ""
    del request.session["username"]
    return render(request, "admins.html", {})


def admins_home(request):
    return render(request, "admins_home.html", {})


def delete_doctor(request, id):
    dr_details = Doctor_reg.objects.get(id=id)
    dr_details.delete()
    return redirect("/doctors_list")


def delete_customer(request, id):
    customer_details = Customer_reg.objects.get(id=id)
    customer_details.delete()
    return redirect('/customers_list')


def admins_change_pwd(request):
    if request.method == "POST":
        pwd = request.POST["password"]
        new_pwd = request.POST["new password"]
        u_name = request.session["username"]
        try:
            admin_details = Admins.objects.get(username=u_name, password=pwd)
            admin_details.password = new_pwd
            admin_details.save()
            return redirect("/admins_logout")
        except Exception as e:
            return render(request, "admins_change_pwd.html", {"msg": e})
    return render(request, "admins_change_pwd.html", {})


def customers_list(request):
    all_customers = Customer_reg.objects.all()
    return render(request, "customers_list.html", {"customers": all_customers})


def doctors_list(request):
    all_drs = Doctor_reg.objects.all()
    return render(request, "doctors_list.html", {"all_drs": all_drs})


def all_queries_responses(request):
    all_queries = Customer_query.objects.all()
    return render(request, "all_queries_responses.html", {"all_queries": all_queries})


def all_booking_appointments(request):
    all_bookings = Book_appointment.objects.all()
    return render(request, "all_booking_appointments.html", {"all_bookings": all_bookings})


def add_news_by_admin(request):
    return render(request, "add_news_by_admin.html", {})


def added_news(request):
    if request.method == "POST":
        add_news = Add_newsForm(request.POST, request.FILES)
        if add_news.is_valid():
            add_news.save()
            return render(request, "admins_home.html", {"msg": "Successfully added your news"})
    return render(request, "add_news_by_admin.html", {})


def all_news_by_admin(request):
    all_news = Add_news.objects.all()
    return render(request, "all_news.html", {"all_news": all_news})


def edit_news(request, id):
    news = Add_news.objects.get(id=id)
    return render(request, "edit_news.html", {"news": news})


def update_news(request):
    if request.method == "POST":
        news_id = request.POST['id']
        news_details = Add_news.objects.get(id=news_id)
        news_form = Add_newsForm(request.POST, request.FILES, instance=news_details)
        if news_form.is_valid():
            news_form.save()
            return redirect("all_news_by_admin")
    return render(request, "edit_news.html", {})


def delete_news(request, id):
    news_details=Add_news.objects.get(id=id)
    news_details.delete()
    return redirect("all_news_by_admin")
