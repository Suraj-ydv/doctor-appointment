"""Myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from customerapp import views as customer_views
from doctorapp import views as doctor_views
from adminsapp import views as admins_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', customer_views.index, name='index'),
    path('about', customer_views.about, name='about'),
    path('news', customer_views.news, name='news'),
    path('contact', customer_views.contact, name='contact'),
    path('services', customer_views.services, name='services'),
    path('customer', customer_views.customer, name='customer'),
    path('customer_reg', customer_views.customer_reg, name="customer_reg"),
    path('customer_home', customer_views.customer_home, name="customer_home"),
    path('customer_change_pwd', customer_views.customer_change_pwd, name="customer_change_pwd"),
    path('customer_profile_update', customer_views.customer_profile_update, name="customer_profile_update"),
    path('customer_logout', customer_views.customer_logout, name="customer_logout"),
    path('customer_forgot_pwd', customer_views.customer_forgot_pwd, name="customer_forgot_pwd"),
    path('customer_edit', customer_views.customer_edit, name="customer_edit"),
    path('customer_profile_pic', customer_views.customer_profile_pic, name="customer_profile_pic"),
    path('customer_profile_pic_upload', customer_views.customer_profile_pic_upload, name="customer_profile_pic_upload"),
    path('customer_pic_display', customer_views.customer_pic_display, name="customer_pic_display"),
    path('customer_query', customer_views.customer_query, name="customer_query"),
    path('customer_all_queries', customer_views.customer_all_queries, name="customer_all_queries"),
    path('delete_customer_query/<id>', customer_views.delete_customer_query, name="delete_customer_query"),
    path('customer_book_appointment', customer_views.customer_book_appointment, name="customer_book_appointment"),
    path('book_appointment', customer_views.book_appointment, name="book_appointment"),
    path('response_from_my_dr', customer_views.response_from_my_dr, name="response_from_my_dr"),
    path('doctor', doctor_views.doctor, name='doctor'),
    path('doctor_reg', doctor_views.doctor_reg, name="doctor_reg"),
    path('doctor_edit', doctor_views.doctor_edit, name="doctor_edit"),
    path('doctor_profile_update', doctor_views.doctor_profile_update, name="doctor_profile_update"),
    path('doctor_home', doctor_views.doctor_home, name="doctor_home"),
    path('doctor_change_pwd', doctor_views.doctor_change_pwd, name="doctor_change_pwd"),
    path('doctor_forgot_pwd', doctor_views.doctor_forgot_pwd, name="doctor_forgot_pwd"),
    path('dr_add_schedule', doctor_views.dr_add_schedule, name="dr_add_schedule"),
    path('doctor_schedules', doctor_views.doctor_schedules, name="doctor_schedules"),
    path('edit_schedule/<id>', doctor_views.edit_schedule, name="edit_schedule"),
    path('update_schedule', doctor_views.update_schedule, name="update_schedule"),
    path('delete_schedule/<id>', doctor_views.delete_schedule, name="delete_schedule"),
    path('doctor_logout', doctor_views.doctor_logout, name="doctor_logout"),
    path('doctor_profile_pic', doctor_views.doctor_profile_pic, name="doctor_profile_pic"),
    path('doctor_profile_pic_upload', doctor_views.doctor_profile_pic_upload, name="doctor_profile_pic_upload"),
    path('dr_profile_pic_display', doctor_views.dr_profile_pic_display, name="dr_profile_pic_display"),
    path('dr_queries_from_customer', doctor_views.dr_queries_from_customer, name="dr_queries_from_customer"),
    path('response_to_customer/<int:id>', doctor_views.response_to_customer, name="response_to_customer"),
    path('dr_responded', doctor_views.dr_responded, name="dr_responded"),
    path('booking_requests_from_customer', doctor_views.booking_requests_from_customer,
         name="booking_requests_from_customer"),
    path('accept_request/<id>', doctor_views.accept_request, name="accept_request"),
    path('reject_request/<id>', doctor_views.reject_request, name="reject_request"),
    path('reschedule_patient_request/<id>', doctor_views.reschedule_patient_request, name="reschedule_patient_request"),
    path('reschedule_request/', doctor_views.reschedule_request, name="reschedule_request"),
    path('prescription/', doctor_views.prescription, name="prescription"),
    path('prescription_to_customer/<id>', doctor_views.prescription_to_customer, name="prescription_to_customer"),
    path('admins', admins_views.admins, name='admins'),
    path('admins_logout', admins_views.admins_logout, name='admins_logout'),
    path('admins_home', admins_views.admins_home, name='admins_home'),
    path('added_news', admins_views.added_news, name='added_news'),
    path('add_news_by_admin', admins_views.add_news_by_admin, name='add_news_by_admin'),
    path('all_news_by_admin', admins_views.all_news_by_admin, name='all_news_by_admin'),
    path('edit_news/<id>', admins_views.edit_news, name='edit_news'),
    path('update_news', admins_views.update_news, name='update_news'),
    path('delete_news/<id>', admins_views.delete_news, name='delete_news'),
    path('customers_list', admins_views.customers_list, name='customers_list'),
    path('doctors_list', admins_views.doctors_list, name='doctors_list'),
    path('delete_doctor/<int:id>', admins_views.delete_doctor, name="delete_doctor"),
    path('admins_change_pwd', admins_views.admins_change_pwd, name='admins_change_pwd'),
    path('delete_customer/<int:id>', admins_views.delete_customer, name="delete_customer"),
    path('all_queries_responses', admins_views.all_queries_responses, name="all_queries_responses"),
    path('all_booking_appointments', admins_views.all_booking_appointments, name="all_booking_appointments"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
