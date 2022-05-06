from django.http import HttpResponse

def view_c(request):
    return HttpResponse(request, 'view_c')

def view_d(request):
    return HttpResponse(request, 'view_d')