# Encrypting a pdf file

from PyPDF2 import PdfFileWriter, PdfReader
from getpass import getpass

# prompt= "Enter password" is an argument in the getpass function, which is a reminder to the user
# Use "with" to open the context menu

pdfwritter = PdfFileWriter()                  # Create class objects
pdf = PdfReader("")                           # Pass the file path as an argument


for page in range(pdf.numPages):              # Get all pages of the file using a loop
    pdfwritter.add_page(pdf.pages[page])      # Reads and adds every page
password = getpass(prompt="Введите пароль")   # Requests a password for encryption
pdfwritter.encrypt(password)                  # Encrypting a file
with open("protected.pdf","wb.") as file:     # Opens the file for writing in binary mode
    pdfwritter.write(file)                    # Writes data to the file