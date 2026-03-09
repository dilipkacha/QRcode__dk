import qrcode
from django.shortcuts import render,redirect
from .models import QRCode
from PIL import Image

from django.shortcuts import get_object_or_404


def home(request):

    qr = None

    if request.method == "POST":

        qr_type = request.POST.get("type")
        data = request.POST.get("data")
        color = request.POST.get("color")

        qr_img = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )

        qr_img.add_data(data)
        qr_img.make(fit=True)

        img = qr_img.make_image(fill_color=color, back_color="white")

        path = f"media/qr_codes/{data}.png"
        img.save(path)

        qr = QRCode.objects.create(
            qr_type=qr_type,
            data=data,
            color=color,
            qr_image=f"qr_codes/{data}.png"
        )

    return render(request,"index.html",{"qr":qr})

def track(request,id):

    qr = get_object_or_404(QRCode,id=id)

    qr.scans += 1
    qr.save()

    return redirect(qr.data)