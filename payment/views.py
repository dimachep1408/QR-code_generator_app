from django.shortcuts import render, redirect
from .models import RandomCodes
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from create_qr_code.models import QrCodes
from registration.models import Profile
import random


# Create your views here.




def render_first_step_payment_page(request):

    error = ""

    user_now = request.user

    



    if user_now.is_authenticated:
        if request.method == "POST":

            email_input = request.POST.get("email")
            password_input = request.POST.get("password")

            print([user_now.password])
            print([password_input])

            if check_password(password_input, user_now.password):
                try:
                    random_code_obj = random.randint(99999, 999999)
                    RandomCodes.objects.create(random_code = random_code_obj, user = user_now)
                except:
                    RandomCodes.objects.get(user_id = user_now.id).delete()
                    RandomCodes.objects.create(random_code = random_code_obj, user = user_now)
                try:
                    send_mail(
                        subject= "Your check code to qr-code generator",
                        message= f"Your check code is : {random_code_obj}",
                        from_email= "qrcodesgenerator0",
                        recipient_list= [f"{email_input}"],
                        fail_silently= False
                    )
                    return redirect("/second_step/")
                except: 
                    error = "email is not exist"
            else:
                error = "incorrect password"
                
    else:
        return redirect("/registration/")

    
        


    return render(request, "first_step_payment.html", context = {"error" : error})




def render_second_step_payment_page(request):
    error = ""
    user_now = request.user

    if request.method == "POST":
        try:
            secret_code_model = RandomCodes.objects.get(user_id = user_now.id).random_code
            secret_code_input = request.POST.get("secret_code")

            print(secret_code_input)
            print(secret_code_model)

            if secret_code_input == secret_code_model:
                return redirect("/third_step/")
            else:
                error = "incorrect code"
                
        except:
            error = "incorrect code"

    return render(request, "second_step_payment.html", context = {"error" : error})


    

def render_third_step_payment_page(request):

    username = request.user
    user = User.objects.get(username = username)
    profile = Profile.objects.get(user = user)

    qr_codes = QrCodes.objects.filter(user_id = username.id, desktop = 0)

    if len(qr_codes) >= 10:
        count = 0
        for qr_code in qr_codes:
            if count >= 10:
                qr_code.workable = False
                qr_code.save()
            count += 1


    profile.subscribe = "standart"

    profile.save()




    error = ""
    return render(request, "third_step_payment.html", context = {"error" : error})