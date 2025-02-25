import qrcode

def generate_qr_code(link, output_file):
    # Create QR code
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
        box_size=10,  # size of each box in the QR code grid
        border=4,  # border size (minimum is 4)
    )

    qr.add_data(link)  # Add the link data to the QR code
    qr.make(fit=True)  # Fit the QR code within the size constraints

    # Create an image of the QR code
    img = qr.make_image(fill='black', back_color='white')

    # Save the image
    img.save(output_file)
    print(f"QR Code saved as {output_file}")

# Usage example
link = "https://www.example.com"
output_file = "qrcode.png"
generate_qr_code(link, output_file)
