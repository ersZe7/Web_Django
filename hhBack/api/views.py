from django.http import JsonResponse
from .models import Company, Vacancy

def get_companies(request):
    companies = Company.objects.all()
    data = [{'id': company.id, 'name': company.name} for company in companies]
    return JsonResponse(data, safe=False)

def get_company(request, id):
    company = Company.objects.get(id=id)
    data = {
        'id': company.id,
        'name': company.name,
        'description': company.description,
        'city': company.city,
        'address': company.address
    }
    return JsonResponse(data)

def get_vacancies_by_company(request, id):
    vacancies = Vacancy.objects.filter(company_id=id)
    data = [{'id': vacancy.id, 'name': vacancy.name} for vacancy in vacancies]
    return JsonResponse(data, safe=False)

def get_vacancies(request):
    vacancies = Vacancy.objects.all()
    data = [{'id': vacancy.id, 'name': vacancy.name} for vacancy in vacancies]
    return JsonResponse(data, safe=False)

def get_vacancy(request, id):
    vacancy = Vacancy.objects.get(id=id)
    data = {
        'id': vacancy.id,
        'name': vacancy.name,
        'description': vacancy.description,
        'salary': vacancy.salary,
        'company': vacancy.company.name
    }
    return JsonResponse(data)

def get_top_ten_vacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    data = [{'id': vacancy.id, 'name': vacancy.name, 'salary': vacancy.salary} for vacancy in vacancies]
    return JsonResponse(data, safe=False)
