from flask import Flask, jsonify, render_template_string
import psutil
import platform
import cpuinfo

app = Flask(__name__)

def get_system_info():
    info = {
        "İşletim Sistemi": platform.system(),
        "Sürüm": platform.version(),
        "Mimari": platform.machine(),
        "İşlemci": cpuinfo.get_cpu_info()["brand_raw"],
        "CPU Çekirdekleri": psutil.cpu_count(logical=False),
        "Toplam RAM": f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB",
        "Pil Durumu": psutil.sensors_battery().percent if psutil.sensors_battery() else "Mevcut değil"
    }
    return info

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Telefon Bilgi Aracı</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin: 20px; }
        table { margin: 0 auto; border-collapse: collapse; width: 50%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f4f4f4; }
    </style>
</head>
<body>
    <h1>Telefon Bilgi Aracı</h1>
    <table>
        {% for key, value in info.items() %}
        <tr><th>{{ key }}</th><td>{{ value }}</td></tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route("/")
def home():
    system_info = get_system_info()
    return render_template_string(HTML_TEMPLATE, info=system_info)

@app.route("/api/info")
def api_info():
    return jsonify(get_system_info())

if __name__ == "__main__":
    app.run(debug=True)
