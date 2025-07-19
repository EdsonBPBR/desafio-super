from abacatepay import AbacatePay
abacate = AbacatePay(api_key='abc_dev_Asxa6uuEGTatFzUsXsMuLkjQ')
qrcode = abacate.pixQrCode.create({
    "amount": 100
})