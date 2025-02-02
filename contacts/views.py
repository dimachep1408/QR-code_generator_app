from django.shortcuts import render, redirect

# Create your views here.

def render_contact_page(request):

    if request.user.is_authenticated:
        username = request.user
    else:
        username = "none"
        return redirect("/")
    
    return render(request, "contacts.html", context = {"username" : username})