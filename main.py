from flask import Flask, render_template, request
from utils.email_sender import send_email_with_pdf
from utils.pdf_converter import convert_image_to_pdf

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def upload_and_convert():
    if request.method == 'POST':
        image = request.files['image']
        recipient_email = request.form['email']

        if image and recipient_email:
            pdf_filename = convert_image_to_pdf(image)
            send_email_with_pdf(recipient_email, pdf_filename)
            return "Email envoyé avec succès!"

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
