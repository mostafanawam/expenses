from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login,logout

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if(email=="" or password==""):
            if(email==""):
                error_message = 'Email field is required'
                return render(request, 'login.html', {'error_message': error_message})
            if(password==""):
                error_message = 'Password field is required'
                return render(request, 'login.html', {'error_message': error_message})
        
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Replace 'home' with the appropriate URL name
        else:
            error_message = 'Invalid username or password. Please try again.'
            return render(request, 'login.html', {'error_message': error_message})
        
    return render(request, 'login.html')
   



def expenses_page(request,pk):

    return render(request, 'expenses.html')

from weasyprint import HTML, CSS
from django.template.loader import get_template
from django.http import HttpResponse

def invoice_page(request,pk):
    if request.method == 'POST':
        context = {'data': 'Your data goes here 12'}

        template_path=f'invoice/invoice_template.html'
        template = get_template(template_path)
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

        HTML(string=html).write_pdf(response)

        # pdf_file = HTML(string=html).write_pdf(
        #     'assets/invoices/test.pdf',
        #     stylesheets=[
        #         # CSS('reports/templates/style.css')
        #     ]
        # )

        return response
        # return render(request, 'invoice.html')
 
    return render(request, 'invoice.html')


def user_logout(request):

    logout(request)

    return redirect("/login/")

def companies_page(request):
    # if request.user.is_authenticated:
    #     return render(request, 'companies.html')
    context={
        "companies":[
            {
                "id":"1",
                "name":"company1",
                "description":"Description of Company 1.",
                "color":"bg-primary"
            },
            {
                "id":"2",
                "name":"company2",
                "description":"Description of Company 2.",
                "color":"bg-success"

            },
            {
                "id":"3",
                "name":"company3",
                "description":"Description of Company 3.",
                "color":"bg-secondary"

            }
        ]
    }
    return render(request, 'companies.html',context=context)


def files(request,pk):
    # if request.user.is_authenticated:
    #     return render(request, 'companies.html')

    return render(request, 'files.html')
