from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import QrCodes
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer

import qrcode
import os


def render_create_qr_code_page(request):



    if request.user.is_authenticated:
        username = request.user
        print(username)
    else:
        username = "none"
        return redirect("/")
    
    if request.method == "POST":
        # qr_code_url to encode
        qr_code_url = request.POST.get("url")
        qr_code_name = request.POST.get("name")
        qr_code_color = request.POST.get("color")
        qr_code_back_color = request.POST.get("back_color")

        if qr_code_name == "":
            return redirect("/create_qr_code_page/")
        
        print(qr_code_color)        

        qr_code = qrcode.QRCode()
        qr_code.add_data(qr_code_url)
        qr_code.make()
        

        img = qr_code.make_image(fill_color = qr_code_color, back_color = qr_code_back_color)
        img.save(os.path.abspath(__file__ + f"/../../media/qr_codes/demo/{username}_qrcode.png"))


        if "save" in request.POST:
            # try:
            QrCodes.objects.create(name = qr_code_name, image = f"/../../media/qr_codes/image/{username}/{qr_code_name}.png", user = username)
            img.save(os.path.abspath(__file__ + f"/../../media/qr_codes/image/{username}/{qr_code_name}.png"))
            # except:
            #     error = "this name already used"
        return redirect("/create_qr_code_page/")


    return render(request, "create_qr_code.html", context = {"username" : username, })