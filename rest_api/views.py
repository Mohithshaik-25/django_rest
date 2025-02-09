from rest_framework import generics
from .models import Rest_prac
from .serializers import RestPracSerializer
import requests
from django.shortcuts import redirect


class RestPracListCreateView(generics.ListCreateAPIView):
    queryset = Rest_prac.objects.all()
    serializer_class = RestPracSerializer

# Retrieve, update, and delete view for Rest_prac
class RestPracDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rest_prac.objects.all()
    serializer_class = RestPracSerializer

from django.shortcuts import render, HttpResponse

def home(req):
    return render(req,"home.html")
def register(request):
    if request.method == "POST":
        # Get the form data from the request
        name = request.POST.get('name')  # Retrieve 'name' from the form
        password = request.POST.get('password')  # Retrieve 'password' from the form

        # Define the REST API endpoint
        api_url = "http://127.0.0.1:8000/api/rest-prac/"

        # Prepare the data to send to the API
        data = {
            "name": name,
            "password": password
        }

        try:
            # Use requests.post to send data to the API
            response = requests.post(api_url, json=data)  # Use the requests library here

            # Check if the data was successfully sent
            if response.status_code == 201:  # HTTP 201 Created
                return redirect("update")
            else:
                return HttpResponse(f"Error: {response.status_code} - {response.text}")

        except Exception as e:
            # Handle any errors that occur during the API call
            return HttpResponse(f"An error occurred: {str(e)}")

    # Render the registration form for GET requests
    return render(request, "register.html")
def update(req):
    if req.method=="POST":
        name=req.POST.get("name")
        id=req.POST.get("id")
        api_url= f"http://127.0.0.1:8000/api/rest-prac/{id}/"
        data={
            "name":name
        }
        try:
            response=requests.patch(api_url,json=data)
            if response.status_code==200:
                return redirect("home")
            else:
                return HttpResponse(f"Error: {response.status_code} - {response.text}")
        except Exception as e:

            return HttpResponse(f"An error occurred: {str(e)}")

    # Render the registration form for GET requests
    return render(req, "update.html")