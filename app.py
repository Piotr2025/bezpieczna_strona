from flask import Flask, render_template, request
import os, uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)
# Limit 2MB na plik
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    # Sprawdzanie czy to obrazek (Blokada RCE)
    if file and file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        # Czyszczenie nazwy (Blokada Path Traversal)
        filename = secure_filename(file.filename)
        # Unikalne ID (Blokada Nadpisywania)
        unique_name = f"{uuid.uuid4().hex}_{filename}"
        file.save(os.path.join(UPLOAD_FOLDER, unique_name))
        return "<h1>Plik wyslany bezpiecznie!</h1><a href='/'>Wroc</a>"
    return "<h1>Blad: Niebezpieczny plik!</h1><a href='/'>Wroc</a>", 400

if __name__ == '__main__':
    app.run(debug=True)
