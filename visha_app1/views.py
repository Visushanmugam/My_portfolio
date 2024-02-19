from django.shortcuts import render,  redirect
from visha_app1.forms import PortfolioContactform

# Create your views here.


def home_page(request):
    if request.method == "POST":
        form = PortfolioContactform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'template/index.html', context={"form":"Message send sucess!"})
        return render(request, 'template/index.html', context={"form":"Message send fail!"})
    return render(request, 'template/index.html')


