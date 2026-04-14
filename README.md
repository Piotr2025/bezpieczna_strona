
#pip install flask
#pip install flask
#cd bezpieczna_strona-main
#python app.py

<img width="770" height="336" alt="image" src="https://github.com/user-attachments/assets/ab6c8556-506a-483e-9a38-a7391f44fea0" />


Zastosowane zabezpieczenia
RCE (Remote Code Execution)	endswith + Image.open	Blokujemy wykonywalne rozszerzenia i sprawdzamy, czy w środku nie ma kodu zamiast zdjęcia.
Path Traversal	secure_filename	Funkcja usuwa ../, więc haker nie może uciec z folderu uploads do systemu.
XSS (Cross-Site Scripting)	img.save()	Ponowne zapisanie obrazu (re-encoding) usuwa doklejone skrypty kradnące hasła.
ZIP Bomb	MAX_CONTENT_LENGTH	Serwer odcina połączenie, jeśli plik przekroczy 2MB, chroniąc nas przed przeladowaniem danych.
Nadpisywanie zasobów	uuid.uuid4()	Każdy plik ma unikalne ID. Haker nie może podmienić np. Twojego logo.png swoim plikiem.


Strona w przeglądarce: http://127.0.0.1:5000/
