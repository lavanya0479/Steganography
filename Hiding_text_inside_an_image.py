import cv2
import string
import os

# Create dictionaries to map characters to their ASCII values and vice versa
c2a = {}
a2c = {}

for i in range(255):
    c2a[chr(i)] = i
    a2c[i] = chr(i)

# Function to validate passcode
def validate_passcode(passcode):
    has_upper = any(char.isupper() for char in passcode)
    has_lower = any(char.islower() for char in passcode)
    has_digit = any(char.isdigit() for char in passcode)
    has_special = any(char in string.punctuation for char in passcode)
    return has_upper and has_lower and has_digit and has_special

# Get the image file path from the user
img_path = input("Enter the path to the image: ")

# Read the image
img = cv2.imread(img_path)

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found or unable to load.")
    exit()

# Get dimensions of the image
rows = img.shape[0]
cols = img.shape[1]
print("Dimensions of the image:", rows, cols)

# Get passcode and validate it
while True:
    key = input("Enter a passcode (must contain uppercase, lowercase, numbers, and special characters): ")
    if validate_passcode(key):
        break
    else:
        print("Passcode must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")

text = input("Enter text to hide: ")

k_idx = 0
t_len = len(text)
z = 0  # decides plane (0 for Blue, 1 for Green, 2 for Red)
n = 0  # number of row
m = 0  # number of column

# Encrypt the text and hide it in the image
for i in range(t_len):
    img[n, m, z] = c2a[text[i]] ^ c2a[key[k_idx]]
    n += 1
    m += 1
    z = (z + 1) % 3  # cycle through color planes (B, G, R)
    k_idx = (k_idx + 1) % len(key)

# Save the encrypted image
enc_img_path = "encrypted_img.jpg"
cv2.imwrite(enc_img_path, img)
os.startfile(enc_img_path)
print("The given data is hidden successfully.")

# Get user choice to extract data from the image
choice = int(input("\nEnter 1 to extract data from Image: "))

if choice == 1:
    re_key = input("\nRe-enter passcode to extract text: ")
    dec_text = ""

    if key == re_key:
        k_idx = 0
        z = 0  # decides plane
        n = 0  # number of row
        m = 0  # number of column

        for i in range(t_len):
            dec_text += a2c[img[n, m, z] ^ c2a[key[k_idx]]]
            n += 1
            m += 1
            z = (z + 1) % 3
            k_idx = (k_idx + 1) % len(key)
        print("Encrypted text was:", dec_text)
    else:
        print("Passcode doesn't match.")
else:
    print("Thank you. EXITING.")
