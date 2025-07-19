from django.shortcuts import render
from abacatepay import AbacatePay

def home(request):
    return render(request, 'app_portal/home.html')

def gerar_pix(request):
    abacate = AbacatePay(api_key='abc_dev_Asxa6uuEGTatFzUsXsMuLkjQ')
    qrcode = abacate.pixQrCode.create({
        "amount": 500000
    })
    return render(request, 'app_portal/pix.html', {
        'qr_code_img': qrcode.brcode_base64,
        'qr_code_str': qrcode.brcode,
    })