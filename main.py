import os

from flask import Flask, render_template, request, send_file
from fpdf import FPDF
from PIL import Image

app = Flask(__name__)

# Route pour afficher le formulaire d'upload
@app.route('/')
def home():
    return render_template('index.html')

# Route pour traiter l'upload et la conversion
@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        image = request.files['image']

        if image:
            # Créer un objet Image à partir du fichier uploadé
            img = Image.open(image)
            img_filename = 'temp_image.png'
            img.save(img_filename)

            # Création d'un objet PDF
            pdf = FPDF()
            pdf.add_page()
            pdf.image(img_filename, 10, 10, 150, 150)

            # Enregistrement du PDF
            pdf_output_filename = 'converted.pdf'
            pdf.output(pdf_output_filename)

            # Suppression de l'image temporaire
            os.remove(img_filename)

            # Envoi du fichier PDF en réponse
            return send_file(pdf_output_filename, as_attachment=True)

# Exécution de l'application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
