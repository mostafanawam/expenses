from django.urls import path
from .views import  *

app_name = "main"
urlpatterns = [
    
    path('logout/',user_logout, name='logout'),
    path('login/',user_login, name='login'),

    path('companies/',companies_page, name='companies_page'),



    path('companies/<int:pk>/files/',files, name='company_files'),
    path('companies/<int:pk>/expenses/',expenses_page, name='company_expenses'),
    path('companies/<int:pk>/invoice/',invoice_page, name='company_invoice'),

    # path('register/',user_register, name='register'),

]
