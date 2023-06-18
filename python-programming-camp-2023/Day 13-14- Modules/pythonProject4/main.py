import pyqrcode

url = input("yazi yaz"):

qr_code = pyqrcode.create(url)
qr_code.svg('qrcode.svg',scale=5)