from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Smart Society Management System - CI/CD Demo")
