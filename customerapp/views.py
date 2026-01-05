from django.shortcuts import render, redirect
from doctorapp.models import Doctor_reg
from customerapp.models import Contact, Customer_reg, Customer_pic, Customer_query, Book_appointment
from customerapp.forms import ContactForm, Customer_regForm, Customer_picForm, Customer_queryForm, Book_appointmentForm
from adminsapp.models import Add_news
import smtplib


# Create your views here.
def index(request):
    return render(request, "index.html", {})


def about(request):
    return render(request, "about.html", {})


def news(request):
    news_details=Add_news.objects.all()
    return render(request, "news.html", {"news_details":news_details})


def services(request):
    return render(request, "services.html", {})


def customer(request):
    if request.method == "POST":
        email = request.POST["email"]
        pwd = request.POST["password"]
        request.session["email"] = email
        try:
            l = Customer_reg.objects.get(email=email, password=pwd)
            return render(request, "customer_home.html", {"login": l, "msg": "Wow!...login successfully"})
        except Exception as e:
            return render(request, "customer.html", {"msg": "Sorry!...your are entered invalid credentials"})
    return render(request, "customer.html", {})


def customer_reg(request):
    if request.method == "POST":
        details = Customer_regForm(request.POST)
        email = request.POST["email"]
        if Customer_reg.objects.filter(email=email).exists():
            return render(request, "Customer_reg.html",
                          {"msg": "Sorry!...this email is already exists. please register with new email"})
        else:
            if details.is_valid():
                try:
                    details.save()
                    return render(request, "customer.html", {"msg": "Great!, you successfully registered"})
                except:
                    return render(request, "customer_reg.html", {})
    return render(request, "customer_reg.html", {})


def customer_home(request):
    return render(request, "customer_home.html", {})


def customer_logout(request):
    request.session["email"] = ""
    del request.session["email"]
    return render(request, "customer.html", {"msg": "Great! successfully logout your account"})


def customer_edit(request):
    email = request.session["email"]
    customer = Customer_reg.objects.get(email=email)
    return render(request, "customer_edit.html", {"customers": customer})


def customer_profile_update(request):
    if request.method == "POST":
        email = request.session["email"]
        custom = Customer_reg.objects.get(email=email)
        form = Customer_regForm(request.POST, instance=custom)
        if form.is_valid():
            form.save()
        return render(request, "customer_home.html", {"msg": "Great!...successfully updated your profile."})
    return render(request, "customer_edit.html", {})


def is_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def customer_change_pwd(request):
    if is_login(request):
        if request.method == "POST":
            email = request.session["email"]
            pwd = request.POST["password"]
            new_pwd = request.POST["new password"]
            try:
                form = Customer_reg.objects.get(email=email, password=pwd)
                form.password = new_pwd
                form.save()
                return redirect('/customer_logout')
            except:
                return render(request, "customer_change_pwd.html", {})

        return render(request, "customer_change_pwd.html", {})
    else:
        return render(request, "customer.html", {})


def customer_profile_pic_upload(request):
    email = request.session['email']
    customer_details = Customer_reg.objects.get(email=email)
    return render(request, "customer_profile_pic.html", {"customer_details": customer_details})


def customer_profile_pic(request):
    if request.method == "POST":
        image = Customer_picForm(request.POST, request.FILES)
        if image.is_valid():
            image.save()
            return render(request, "customer_profile_pic.html", {"msg": "Successfully profile pic uploaded."})
    return render(request, "customer_profile_pic.html", {})


def customer_pic_display(request):
    if request.method == "GET":
        email = request.session['email']
        customer_details = Customer_reg.objects.get(email=email)
        customer_pic = Customer_pic.objects.filter(name_id=customer_details.id)

        return render(request, "customer_profile_display.html",
                      {"customer_pic": customer_pic, "customer_details": customer_details})


def customer_forgot_pwd(request):
    if request.method == "POST":
        email = request.POST["email"]
        try:
            cust = Customer_reg.objects.get(email=email)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("jarugulla77@gmail.com", "Sriramatherdam@99")
            message = "greetings! from admin team. your pwd is " + cust.password
            server.sendmail("jarugulla77@gmail.com", [email], message)
            server.quit()
            msg = "successfully sent your password"
            return render(request, "customer.html", {"msg": msg})
        except:
            msg = "email not register"
            return render(request, "customer_forgot.html", {"msg": msg})
    return render(request, "customer_forgot.html", {})


def contact(request):
    if request.method == "POST":
        details = ContactForm(request.POST)
        if details.is_valid():
            try:
                details.save()
            except:
                return render(request, "contact.html", {})

    return render(request, "contact.html", {})


def customer_query(request):
    if request.method == "POST":
        query = Customer_queryForm(request.POST)
        if query.is_valid():
            query.save()
            return render(request, "customer_home.html", {})
    email1 = request.session["email"]
    doctor = Doctor_reg.objects.all()
    return render(request, "customer_query.html", {"email": email1, "doctors": doctor})


def customer_all_queries(request):
    email1 = request.session["email"]
    queries = Customer_query.objects.filter(email=email1)
    return render(request, "customer_all_queries.html", {"queries": queries})


def delete_customer_query(request, id):
    customer_query = Customer_query.objects.get(id=id)
    customer_query.delete()
    return redirect("/customer_all_queries")
    # return render(request, "customer_all_queries.html", {})


def customer_book_appointment(request):
    drs_names = Doctor_reg.objects.all()
    email = request.session["email"]
    customer = Customer_reg.objects.get(email=email)
    return render(request, "customer_book_appointment.html", {"customer": customer, "drs_names": drs_names})


def book_appointment(request):
    if request.method == "POST":
        appointment = Book_appointmentForm(request.POST)
        if appointment.is_valid():
            appointment.save()
            return render(request, "customer_home.html", {})
    return render(request, "customer_book_appointment.html", {})


def response_from_my_dr(request):
    email = request.session['email']
    customer_details = Customer_reg.objects.get(email=email)

    if Book_appointment.objects.filter(customer_name_id=customer_details.id).exists():
        booking_details = Book_appointment.objects.filter(customer_name_id=customer_details.id)
        return render(request, "response_from_my_dr.html", {"booking_details": booking_details})
    else:
        msg = "You doesn't booked any appointment,to meet a Doctor."
        return render(request, "response_from_my_dr.html", {"message": msg})
