## Steganography

# Image Steganography using Python and OpenCV

Using steganography techniques, this Python script allows users to hide text messages inside images. It includes functionalities for encrypting text, embedding it into selected images, and extracting hidden messages from encrypted images.

## Features

- **Encryption and Hiding**: Users can choose an image file, enter a secure passcode, and provide text to hide within the image. The script encrypts and embeds the text into the image using the RGB color channels.
  
- **Extraction**: Users can extract hidden text from an encrypted image by providing the correct decryption passcode.

## Requirements

- Python 3.x
- OpenCV library (`cv2`)
- Standard Python libraries: `string`, `os`

## Setup

1. **Install Python**: Ensure Python 3.x is installed on your system.
   
2. **Install OpenCV**: Install OpenCV using pip if not already installed:
   ```
   pip install opencv-python
   ```

3. **Clone the Repository**: Clone this repository to your local machine:
   ```
   git clone <repository_url>
   ```

4. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the cloned repository.
   - Run the script:
     ```
     python steganography.py
     ```

## Usage

1. **Input Requirements**:
   - **Image**: Provide the path to the image file.
   - **Passcode**: Enter a passcode containing at least one uppercase letter, one lowercase letter, one digit, and one special character.
   - **Text to Hide**: Enter the text you want to hide within the image.

2. **Encryption**:
   - The script encrypts the text and embeds it into the image. The resulting encrypted image (`encrypted_img.jpg`) is saved in the same directory.

3. **Extraction**:
   - Choose option `1` to extract data from the encrypted image.
   - Enter the same passcode used for encryption to extract and display the hidden text.

## Example

1. Provide the path to an image file (`1.jpeg`).
2. Enter a passcode (`Lavanya@123`).
3. Enter text to hide (`This is hidden message`).
4. The script will encrypt the message and save it as `encrypted_img.jpg`.
5. Choose to extract data, enter the passcode again, and the hidden text will be displayed.



Feel free to adjust the details according to your project structure and specific implementation. Include additional sections or details as needed to provide comprehensive instructions for users.
