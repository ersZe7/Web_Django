from django.urls import path
from .views import get_companies, get_company, get_vacancies_by_company, get_vacancies, get_vacancy, get_top_ten_vacancies

urlpatterns = [
    path('companies/', get_companies),
    path('companies/<int:id>/', get_company),
    path('companies/<int:id>/vacancies/', get_vacancies_by_company),
    path('vacancies/', get_vacancies),
    path('vacancies/<int:id>/', get_vacancy),
    path('vacancies/top_ten/', get_top_ten_vacancies),
]
