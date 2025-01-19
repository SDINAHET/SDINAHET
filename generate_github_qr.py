import qrcode
from PIL import Image

# Create the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for logo overlay
    box_size=10,
    border=4,
)
github_url = "https://github.com/SDINAHET"
qr.add_data(github_url)
qr.make(fit=True)

# Generate the QR code image
qr_code = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Open the GitHub logo image
logo = Image.open("github_logo_v1.png")  # Ensure the logo file is in the same directory or provide full path

# Resize the logo to fit the center
logo_size = (qr_code.size[0] // 5, qr_code.size[1] // 5)  # Adjust logo size to 20% of QR size
logo = logo.resize(logo_size, Image.Resampling.LANCZOS)  # Use Resampling.LANCZOS instead of ANTIALIAS

# Calculate position to overlay the logo
pos = ((qr_code.size[0] - logo_size[0]) // 2, (qr_code.size[1] - logo_size[1]) // 2)
qr_code.paste(logo, pos)

# Save the final QR code
qr_code.save("github_qr_with_logo.png")
print("QR Code with GitHub logo saved as github_qr_with_logo.png")
