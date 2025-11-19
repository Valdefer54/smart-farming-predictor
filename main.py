import os
import sys
from flask import Flask, render_template, request, jsonify
import webbrowser
from threading import Timer

# --- IMPORTANTE ---
# Asegúrate de que la carpeta model_ml existe y tiene un archivo __init__.py y predict.py
try:
    from model_ml.predict import predict
except ImportError as e:
    print("❌ ERROR CRÍTICO: No se encuentra el módulo de predicción.")
    print(f"Detalle: {e}")
    print("Asegúrate de estar ejecutando esto desde la carpeta raíz del proyecto.")
    sys.exit(1)

# Configuración de la app
# template_folder debe apuntar a donde tienes el HTML
app = Flask(__name__, template_folder='ui/templates')

# --- RUTA 1: Cargar la Interfaz ---
@app.route('/')
def home():
    # Asegúrate de que el archivo se llame interface.html (revisa el nombre en tu carpeta)
    try:
        return render_template('interface.html') # Corregido el typo 'inteface'
    except Exception as e:
        return f"<h2>Error cargando la plantilla</h2><p>{e}</p><p>Verifica que 'ui/templates/interface.html' exista.</p>"

# --- RUTA 2: Recibir datos y responder (SOLO UNA VEZ) ---
@app.route('/predecir', methods=['POST'])
def procesar_prediccion():
    try:
        # 1. Obtener datos
        data = request.get_json()
        print(f"📥 Datos recibidos: {data}") # Log para ver qué llega

        # 2. Validar y convertir
        valores = [
            float(data['N']),
            float(data['P']),
            float(data['K']),
            float(data['temperature']),
            float(data['humidity']),
            float(data['ph']),
            float(data['rainfall'])
        ]

        # 3. Predicción
        predicciones = predict([valores])
        
        # Manejar si devuelve un array o un valor único
        resultado_cultivo = predicciones[0] if hasattr(predicciones, '__len__') else predicciones
        
        print(f"✅ Predicción exitosa: {resultado_cultivo}")
        
        # 4. Respuesta JSON (Debe ser 'success' para que tu JS lo entienda)
        return jsonify({'status': 'success', 'resultado': resultado_cultivo})

    except Exception as e:
        # Este print saldrá en tu terminal negra, aquí verás el error real
        print(f"❌ ERROR EN EL SERVIDOR: {e}")
        # Devolvemos un JSON de error para que el JS no use el catch genérico
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Función para abrir el navegador
def abrir_navegador():
    if not os.environ.get("WERKZEUG_RUN_MAIN"): # Evita que se abra 2 veces si Flask se reinicia
        webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Timer para abrir el navegador 1.5 segundos después de iniciar
    Timer(1.5, abrir_navegador).start()
    
    print("🚀 Servidor iniciado. Tu navegador debería abrirse pronto...")
    app.run(debug=True)