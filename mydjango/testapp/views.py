from django.shortcuts import render
from django.shortcuts import HttpResponse
from testapp import models
# Create your views here.

user_list1 = [
    {"user":"jack", "pwd":"123"},
    {"user":"tom", "pwd":"456"},
]
def index(request):
    #return HttpResponse("hello World!")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        #print(username,password)
        models.UserInfo.objects.create(user=username, pwd=password)
        #temp = {"user":username, "pwd":password}
        #user_list.append(temp)
    user_list = models.UserInfo.objects.all()
    return render(request, "index.html", {"data":user_list})
