from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from google.oauth2 import service_account
from googleapiclient.discovery import build
import json

app = Flask(__name__)
CORS(app)  # Permitir CORS para que el frontend pueda hacer peticiones

# Configuración
CREDENTIALS_FILE = 'credentials.json'  # Tu archivo JSON con las credenciales
SPREADSHEET_ID = '1pOoMLLaFWJpI-i7Hc9VTnNDB73s-aZftJWpcEktij48'  # ⬅️ COLOCA AQUÍ EL ID DE TU GOOGLE SHEET
RANGE_NAME = 'Respuestas de formulario 1!A:H'  # ⬅️ AJUSTA EL RANGO (A:H = columnas A hasta H)

def get_sheets_service():
    """Crea el servicio de Google Sheets usando las credenciales."""
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE,
        scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
    )
    service = build('sheets', 'v4', credentials=credentials)
    return service

@app.route('/')
def index():
    """Sirve el archivo HTML principal."""
    return send_from_directory('.', 'index.html')

@app.route('/api/data')
def get_data():
    """Endpoint que obtiene los datos de Google Sheets."""
    try:
        service = get_sheets_service()
        sheet = service.spreadsheets()
        
        # Obtener datos
        result = sheet.values().get(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME
        ).execute()
        
        values = result.get('values', [])
        
        if not values:
            return jsonify({'error': 'No se encontraron datos'}), 404
        
        # Convertir a formato JSON
        headers = values[0]  # Primera fila son los encabezados
        data = []
        
        for row in values[1:]:  # Saltar encabezados
            # Asegurarse de que la fila tenga suficientes columnas
            while len(row) < len(headers):
                row.append('')
            
            row_dict = {}
            for i, header in enumerate(headers):
                row_dict[header] = row[i] if i < len(row) else ''
            
            data.append(row_dict)
        
        return jsonify(data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health')
def health():
    """Endpoint de salud para verificar que el servidor está funcionando."""
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    print("🚀 Servidor iniciado en http://localhost:5000")
    print("📊 Endpoint de datos: http://localhost:5000/api/data")
    app.run(debug=True, port=5000)
