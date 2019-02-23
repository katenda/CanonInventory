"""CanonInventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from .views import *
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [

    #receptionist view cars
    url(r'^receptionist_view_cars$', receptionist_view_cars, name="receptionist_view_cars"),
    url(r'^receptionist_view_complaints$', receptionist_view_complaints, name="receptionist_view_complaints"),
    url(r'^receptionist_view_drivers$', receptionist_view_drivers, name="receptionist_view_drivers"),
    url(r'^receptionist_add_complaint$', receptionist_add_complaint, name="receptionist_add_complaint"),

    url(r'^operations_edit_car/(?P<pk>\d+)$',operations_edit_car,name='operations_edit_car'),
    url(r'^operations_edit_driver/(?P<pk>\d+)$',operations_edit_driver,name='operations_edit_driver'),
    url(r'^receptionist_edit_complaint/(?P<pk>\d+)$',receptionist_edit_complaint,name='receptionist_edit_complaint'),

    url(r'^operations_delete_car/(?P<pk>\d+)$', operations_delete_car, name="operations_delete_car"),
    url(r'^receptionist_delete_complaint/(?P<pk>\d+)$', receptionist_delete_complaint, name="receptionist_delete_complaint"),
    url(r'^operations_delete_driver/(?P<pk>\d+)$', operations_delete_driver, name="operations_delete_driver"),

    url(r'^receptionist_forward_complaint/(?P<pk>\d+)$', receptionist_forward_complaint, name="receptionist_forward_complaint"),

    url(r'^operations_home$', operations_home, name="operations_home"),
    url(r'^operations_view_cars$', operations_view_cars, name="operations_view_cars"),
    url(r'^operations_view_drivers$', operations_view_drivers, name="operations_view_drivers"),

    url(r'^operations_add_car/$', operations_add_car, name="operations_add_car"),
    url(r'^operations_add_driver$', operations_add_driver, name="operations_add_driver"),

    url(r'^operations_view_complaints$', operations_view_complaints, name="operations_view_complaints"),

    url(r'^operations_export_cars$', operations_export_cars, name="operations_export_cars"),
    url(r'^operations_export_drivers$', operations_export_drivers, name="operations_export_drivers"),

    url(r'^operations_view_driver_payments$', operations_view_driver_payments, name="operations_view_driver_payments"),

    url(r'^accountant_home$', accountant_home, name="accountant_home"),

    url(r'^accountant_make_driver_payments$', accountant_make_driver_payments, name="accountant_make_driver_payments"),

    url(r'^print_driverPayment_receipt/(?P<pk>\d+)$', generate_driver_payment_receipt.as_view(), name="print_driverPayment_receipt"),

    url(r'^accountant_print_driverfinancial_report/(?P<driver_name>\w+)/$', accountant_generate_driver_financial_report.as_view(), name="accountant_print_driverfinancial_report"),

    url(r'^driver_general_financial_report$', driver_general_financial_report, name="driver_general_financial_report"),

    url(r'^print_general_financial_report$', print_general_financial_report.as_view(), name="print_general_financial_report"),

    url(r'^operations_handle_complaint/(?P<pk>\d+)$', operations_handle_complaint, name="operations_handle_complaint"),

    url(r'^operations_view_car_details/(?P<pk>\d+)$', operations_view_car_details, name="operations_view_car_details"),

    url(r'^generate_operations_driver_financial_statement/(?P<driver_name>\w+)/$', generate_operations_driver_financial_statement.as_view(), name="generate_operations_driver_financial_statement"),

    url(r'^monthly_archiving_script$', monthly_archiving_script, name="monthly_archiving_script"),



    #accountant major urls

    url(r'^display_cashiers/', display_cashiers, name='display_cashiers'),
    url(r'^display_viewstaff/', display_viewstaff, name='display_viewstaff'),

    url(r'^enter_expenditure/', enter_expenditure, name='enter_expenditure'),
    url(r'^enter_sundryexpense', enter_sundryexpense ,name='enter_sundryexpense'),
    url(r'^pay_salary/',pay_salary, name='pay_salary'),

    url(r'^sundryreport', sundryreport ,name='sundryreport'),
    url(r'^salaryreport/', salaryreport, name='salaryreport'),
    url(r'^expenditurereport/', expenditurereport, name='expenditurereport'),


    url(r'^salariespdf/', salariespdf.as_view() ,name='salariespdf'),
    url(r'^sundrypdf/', sundrypdf.as_view() ,name='sundrypdf'),
    url(r'^expenditurepdf/', expenditurepdf.as_view() ,name='expenditurepdf'),

    url(r'^expensereceipt/', expensereceipt.as_view() ,name='expensereceipt'),
    url(r'^salaryreceipt/', salaryreceipt.as_view() ,name='salaryreceipt'),
    url(r'^sundryreceipt/', sundryreceipt.as_view() ,name='sundryreceipt'),



    #################
    #manager urls
    url(r'^user_login$', user_login, name="user_login"),

]
