import smtplib

from django.shortcuts import render, redirect
from customerapp.models import Customer_query, Book_appointment
from customerapp.forms import Customer_queryForm, Book_appointmentForm, Book_appointmentForm1, Book_appointmentForm2
from doctorapp.models import Doctor_reg, Add_schedule, Doctor_pic
from doctorapp.forms import Doctor_regForm, Add_scheduleForm, Doctor_picForm


def doctor(request):
    if request.method == "POST":
        email = request.POST["email"]
        pwd = request.POST["password"]
        request.session["email"] = email
        try:
            d = Doctor_reg.objects.get(email=email, password=pwd)
            return render(request, "doctor_home.html", {'data': d, "msg": "Wow!...login successfully"})
        except Exception as e:
            return render(request, "doctor.html", {"error": e, "msg": "Sorry!...your are entered invalid credentials"})
    return render(request, "doctor.html", {})


def doctor_reg(request):
    if request.method == "POST":
        details = Doctor_regForm(request.POST)
        email = request.POST["email"]
        if Doctor_reg.objects.filter(email=email).exists():
            return render(request, "doctor_reg.html",
                          {"msg": "Sorry!,this email is already exists. pls register with another email"})
        else:
            if details.is_valid():
                try:
                    details.save()
                    return render(request, "doctor.html", {"msg": "Great!, you successfully registered"})
                except:
                    return render(request, "doctor_reg.html", {})
    return render(request, "doctor_reg.html", {})


def doctor_edit(request):
    email = request.session["email"]
    drs = Doctor_reg.objects.get(email=email)
    return render(request, "doctor_edit.html", {"doctors": drs})


def doctor_profile_update(request):
    if request.method == "POST":
        email = request.session["email"]
        drs = Doctor_reg.objects.get(email=email)
        form = Doctor_regForm(request.POST, instance=drs)
        if form.is_valid():
            form.save()
            return render(request, "doctor_home.html", {"msg": "Great!...successfully updated your profile."})
    return render(request, "doctor_profile_update.html", {})


def is_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def doctor_change_pwd(request):
    if is_login(request):
        if request.method == "POST":
            pwd = request.POST["password"]
            new_pwd = request.POST["new_password"]
            email = request.session["email"]
            try:
                form = Doctor_reg.objects.get(email=email, password=pwd)
                form.password = new_pwd
                form.save()
                return redirect('/doctor_logout', {"msg": "Great! successfully change your password"})
            except:
                return render(request, "doctor_change_pwd.html", {})
        return render(request, "doctor_change_pwd.html", {})
    else:
        return render(request, "doctor.html", {})


def doctor_forgot_pwd(request):
    if request.method == "POST":
        email = request.POST["email"]
        try:
            dr = Doctor_reg.objects.get(email=email)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("jarugulla77@gmail.com", "Sriramatherdam@99")
            msg = "Greetings! from admin team, your password is " + dr.password
            server.sendmail("jarugulla77@gmail.com", [email], msg)
            server.quit()
            return render(request, "doctor.html", {})
        except Exception as e:
            return render(request, "doctor_forgot.html", {"msg": e})
    return render(request, "doctor_forgot.html", {})


def doctor_home(request):
    return render(request, "doctor_home.html", {})


def doctor_logout(request):
    request.session["email"] = ""
    del request.session["email"]
    return render(request, "doctor.html", {})


def doctor_profile_pic(request):
    email = request.session['email']
    dr_details = Doctor_reg.objects.get(email=email)
    return render(request, "doctor_profile_pic.html", {"dr_details": dr_details})


def doctor_profile_pic_upload(request):
    if request.method == "POST":
        image = Doctor_picForm(request.POST, request.FILES)
        if image.is_valid():
            image.save()
            return render(request, "doctor_profile_pic.html", {"msg": "Successfully profile pic uploaded."})
    return render(request, "doctor_profile_pic.html", {})


def dr_profile_pic_display(request):
    if request.method == "GET":
        email = request.session['email']
        dr_details = Doctor_reg.objects.get(email=email)
        dr_pic = Doctor_pic.objects.filter(name_id=dr_details.id)
        return render(request, "dr_profile_display.html",
                      {"dr_pic": dr_pic, "dr_details": dr_details})
    return render(request, "dr_profile_display.html", {})


def dr_add_schedule(request):
    if request.method == "POST":
        schedule = Add_scheduleForm(request.POST)
        if schedule.is_valid():
            try:
                schedule.save()
                return render(request, "doctor_home.html", {"msg": "Successfully entered your schedule"})
            except Exception as e:
                return render(request, "dr_add_schedule.html", {"msg": e})
    email1 = request.session["email"]
    return render(request, "dr_add_schedule.html", {"email": email1})


def doctor_schedules(request):
    email = request.session['email']
    schedules = Add_schedule.objects.filter(email=email)
    return render(request, "doctor_schedules.html", {"schedules": schedules})


def delete_schedule(request, id):
    schedule = Add_schedule.objects.get(id=id)
    schedule.delete()
    return redirect('/doctor_schedules')


def edit_schedule(request, id):
    schedules = Add_schedule.objects.get(id=id)
    return render(request, "dr_schedule_edit.html", {"schedules": schedules})


def update_schedule(request):
    if request.method == "POST":
        dr_email = request.POST["email"]
        schedule = Add_schedule.objects.get(email=dr_email)
        form = Add_scheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            try:
                form.save()
                return redirect("/doctor_schedules")
            except Exception as e:
                return render(request, "dr_schedule_edit.html", {"msg": e})
    return render(request, "dr_schedule_edit.html", {})


def dr_queries_from_customer(request):
    email = request.session['email']
    dtails = Doctor_reg.objects.get(email=email)
    queries = Customer_query.objects.filter(doctor_name=dtails.id)
    return render(request, "dr_queries_from_customer.html", {"queries": queries})


def response_to_customer(request, id):
    details = Customer_query.objects.get(id=id)
    return render(request, "response_to_customer.html", {"details": details})


def dr_responded(request):
    if request.method == "POST":
        customer_id = request.POST["id"]
        details = Customer_query.objects.get(id=customer_id)
        form = Customer_queryForm(request.POST, instance=details)
        if form.is_valid():
            form.save()
            return redirect("dr_queries_from_customer")
    return render(request, "dr_queries_from_customer.html", {})


def booking_requests_from_customer(request):
    email = request.session["email"]
    doctor_details = Doctor_reg.objects.get(email=email)
    requests = Book_appointment.objects.filter(doctor_name=doctor_details.id)
    if requests.exists():

        return render(request, "booking_requests_from_customer.html", {"requests": requests})
    else:

        return render(request, "booking_requests_from_customer.html",
                      {"msg": "Sorry!,no requests are found from customer"})


def accept_request(request, id):
    customer = Book_appointment.objects.get(id=id)
    customer.status = "accepted"
    customer.save()
    return redirect("booking_requests_from_customer")


def reject_request(request, id):
    customer = Book_appointment.objects.get(id=id)
    customer.status = "rejected"
    customer.save()
    return redirect("booking_requests_from_customer")


def reschedule_patient_request(request, id):
    customer = Book_appointment.objects.get(id=id)
    return render(request, "reschedule_request.html", {"customer": customer})


def reschedule_request(request):
    if request.method == "POST":
        booking_id = request.POST['id']
        booking_details = Book_appointment.objects.get(id=booking_id)
        reschedule = Book_appointmentForm2(request.POST, instance=booking_details)
        if reschedule.is_valid():
            reschedule.save()
            booking_details.status = "rescheduled"
            booking_details.save()
            return redirect("booking_requests_from_customer")
    return render(request, "reschedule_request.html", {})


def prescription_to_customer(request, id):
    customer = Book_appointment.objects.get(id=id)
    return render(request, "prescription_to_customer.html", {"customer": customer})


def prescription(request):
    if request.method == "POST":
        booking_id = request.POST['id']
        booking_details = Book_appointment.objects.get(id=booking_id)
        response = Book_appointmentForm1(request.POST, request.FILES, instance=booking_details)
        if response.is_valid():
            response.save()
        return render(request, "prescription_to_customer.html", {"response": response})
