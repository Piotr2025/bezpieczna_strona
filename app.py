#pip install flask
#pip install flask
#cd bezpieczna_strona-main
#python app.py
from flask import Flask, render_template, request
import os, uuid
from werkzeug.utils import secure_filename
from PIL import Image  # Biblioteka do weryfikacji i czyszczenia obrazów

app = Flask(__name__)

#  Ochrona przed ZIP BOMB i przepełnieniem RAM

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return "Brak pliku", 400

  
    # Szybka weryfikacja czy końcówka pliku jest na liście dozwolonych
    if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        return "<h1>Blad: Niedozwolone rozszerzenie!</h1><a href='/'>Wroc</a>", 400

    try:

        # Image.open sprawdza, czy to FAKTYCZNIE jest obrazek, a nie skrypt PHP/JS
  
        img = Image.open(file)

        # ZABEZPIECZENIE 4: Blokada Path Traversal 
        # Usuwa znaki typu "../", które mogłyby pozwolić hakerowi wyjść poza folder
        filename = secure_filename(file.filename)

        # ZABEZPIECZENIE 5: Blokada Nadpisywania 
        # Dodajemy unikalny kod UUID, żeby haker nie podmienił nam plików na serwerze
        unique_name = f"{uuid.uuid4().hex}_{filename}"
        save_path = os.path.join(UPLOAD_FOLDER, unique_name)

        # ZABEZPIECZENIE 6: Data Sanitization 
        # Nie zapisujemy pliku bezpośrednio. Pillow "przerysowuje" obraz piksel po pikselu,
        # co usuwa wszelki złośliwy kod ukryty w metadanych (tzw. payloads).
        img.save(save_path)

        return "<h1>Plik sprawdzony i zapisany bezpiecznie!</h1><a href='/'>Wroc</a>"

    except Exception:
       
        return "<h1>ATAK WYKRYTY: Plik nie jest poprawnym obrazem!</h1><a href='/'>Wroc</a>", 400

if __name__ == '__main__':
    app.run(debug=True)
