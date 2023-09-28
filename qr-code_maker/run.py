import qrcode
from PIL import Image

# Funzione per creare un QR code da un link
def create_qr_code_from_link(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("./output/qr-code.png")

# Funzione per creare un QR code da un'immagine
def create_qr_code_from_image(image_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    with open(image_path, "rb") as f:
        qr.add_data(f.read())
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("./output/qr-code.png")

# Esempio di utilizzo
input_type = input("Vuoi creare un QR code da un link o da un'immagine? (link/image): ").lower()

if input_type == "link":
    with open("src.txt","r") as source:
        link = source.read()
    create_qr_code_from_link(link)
    print("QR code creato con successo")
elif input_type == "image":
    image_path = "./src."
    estensione = input("Inserisci il formato dell'immagine senza . davanti: ")
    image_path+=estensione
    print(image_path)
    create_qr_code_from_image(image_path)
    print(f"QR code creato con successo")
else:
    print("Tipo non valido. Scegli 'link' o 'image'.")
