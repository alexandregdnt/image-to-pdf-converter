import os

from fpdf import FPDF
from PIL import Image


def convert_image_to_pdf(image):
    img = Image.open(image)
    img_filename = 'temp_image.png'
    img.save(img_filename)

    pdf = FPDF()
    pdf.add_page()
    pdf.image(img_filename, 10, 10, 150, 150)
    pdf_output_filename = 'converted.pdf'
    pdf.output(pdf_output_filename)

    os.remove(img_filename)
    return pdf_output_filename
