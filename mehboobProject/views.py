from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse

from .models import User, StudentsAdmission, ContactRequest

# Create your views here.
def index_view(request):
    # return render(request, "mehboobProject/index.html")
    return render(request, "mehboobProject/index.html")

def htmlRender(request, name):
    fileName = name.split(".")
    return render(request, f"mehboobProject/{name}", {
        "fileName": fileName[0]
    })

def register(request):
    if request.method == "POST":
        fullName = request.POST["fullName"]
        username = request.POST["username"]
        email = request.POST["email"]
        phone = request.POST["phoneNumber"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        gender = request.POST["gender"]

        if password != confirmation:
            return render(request, "mehboobProject/Rform.html", {
                "message": "Passwords must match."
            })
        
        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return render(request, "mehboobProject/Rform", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, "mehboobProject/Rform.html")
    
def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "mehboobProject/login.html", {
                "message": "Invalid username and/or password."
            })
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def studentAddmission_view(request):

    # taking all date from the form
    if request.method == "POST":
        student_name = request.POST["student_name"]
        dob = request.POST["dob"]
        age = request.POST["age"]
        gender = request.POST["gender"]

        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]

        previous_school = request.POST["previous_school"]
        previous_class = request.POST["previous_class"]
        percentage = request.POST["percentage"]


        # creating a studentAddmission object
        obj = StudentsAdmission(
            student_name=student_name,
            dob=dob,
            age=age,
            gender=gender,
            email=email,
            phone=phone,
            address=address,
            previous_school=previous_school,
            previous_class=previous_class,
            percentage=percentage
        )

        obj.save()

        return render(request, "mehboobProject/index.html", {
            "message": f"From for the Addmission of {student_name} is submitted successfully!"
        })
    else:
        return HttpResponseRedirect(reverse('htmlRender', kwargs={"name": "admission.html"}))
    
def contactRequest_view(request):
    
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        obj = ContactRequest(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        obj.save()

        return render(request, "mehboobProject/index.html", {
            "message" : "Thank you for contacting us we will reachout to you after sometime."
        })
    else:
        return HttpResponseRedirect(reverse('htmlRender', kwargs={"name": "contact.html"}))

