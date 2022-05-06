from pickle import GET
from tokenize import Name
from unicodedata import name
from urllib import request
from django.shortcuts import redirect, render
from Book.models import Book
from django.http import HttpResponse     # becase admint ko samne whateve opration you are performing admin has to unserstant that why import

# Create your views here.


# def homepage(request):      #one is a Http request and other is defaltu reserve argument request
    # print(request.method)   # it gives request method like get as shows in console
    # a = [1,2,3,4]                      # in admin it shows output like 1,2,3,4
    # a= "[1,2,3,4]"                     # in admin it shows output like [1,2,3,4]
    # return HttpResponse("Hello Hi")
    # return render(request, template_name="home.html") # render ky akrta hai home.html page ka data read krta hai 


def homepage(request):
    print(request.method)
    # print(request.POST, type(request.POST))
    if request.method == "POST":               # ye isliye jab bhi me url pe hit karti hu to error ati h o nahi ane k liye
        Book_Name= request.POST.get("bname")
        Book_price = request.POST.get("bprice")
        Book_qynt = request.POST.get("bqynt")
        # print(Book_Name,Book_price,Book_qynt)
        Book.objects.create(Name= Book_Name,price= Book_price, Book_qynt=Book_qynt)     # becase we are reading data in database sql

        return redirect("homepage")

    elif request.method == "GET":
        return render(request,template_name="home.html")   #


def show_all_book(request):
    all_book= Book.objects.all()
    data = {"books": all_book}
    return render(request,"show_all.html", context=data)

def Edit_Data(request,id):
    all_book = Book.objects.get(id=id)
    return render(request,"home.html",context={'Single_data': all_book})

def delete(request,id):
    all_book = Book.objects.get(id=id)
    all_book.delete()
    return render(request,'show_all_book')




