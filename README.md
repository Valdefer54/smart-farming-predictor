# Proyecto Final - Sistema Predictor de Cultivos

Este repositorio contiene una pequeña aplicación Flask que carga un modelo de ML (Random Forest) para recomendar cultivos según características del suelo y clima.

**Estructura**
- `main.py`: servidor Flask y endpoints.
- `ui/templates/inteface.html`: interfaz web para introducir datos y ver la recomendación.
- `model_ml/random_forest_model.joblib`: archivo del modelo entrenado (binario).
- `model_ml/predict.py`: funciones para cargar el modelo y predecir.

**Requisitos**
- Python 3.10+ (o la versión que uses en tu entorno virtual)
- pip

Se recomiendan las siguientes dependencias (si no tienes `requirements.txt`):
- `Flask`
- `joblib`
- `pandas`
- `scikit-learn` (solo si vas a reentrenar o inspeccionar el modelo)

**Instrucciones (Windows / PowerShell)**

1) Abrir PowerShell en la carpeta del proyecto (ejemplo):

```powershell
cd "C:\Users\Usuario\Desktop\Proyecto Final Programación III"
```

2) Crear y activar un entorno virtual (recomendado):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3) Instalar dependencias (si tienes `requirements.txt`):

```powershell
pip install -r requirements.txt
```

Si no tienes `requirements.txt`, instala las dependencias principales:

```powershell
pip install flask joblib pandas scikit-learn
```

4) Ejecutar la aplicación:

```powershell
python .\main.py
# Abrir la interfaz en el navegador
Start-Process http://127.0.0.1:5000
```

5) Probar el endpoint desde la interfaz: llena el formulario y presiona `ANALIZAR SUELO`. El HTML hace POST a `/predecir` y espera `status: 'success'` en la respuesta JSON.

**Subir el repositorio a GitHub**

A continuación tienes pasos mínimos para crear el repositorio remoto y subir tu código (PowerShell):

1. Inicializar git, añadir archivos y hacer commit:

```powershell
git init
git add .
git commit -m "Inicial: proyecto predictor de cultivos"
```

2. Crear repositorio en GitHub (opciones):
- Opción A (interfaz web): crea un nuevo repositorio en https://github.com/new y copia la URL remota.
- Opción B (gh CLI, si la tienes):

```powershell
gh repo create NOMBRE_REPO --public --source . --remote origin --push
```

3. Si creaste el repo en la web, añade el remoto y sube:

```powershell
# Reemplaza <URL_REMOTO> por la URL que te dio GitHub (HTTPS o SSH)
git remote add origin <URL_REMOTO>
git branch -M main
git push -u origin main
```

**Recomendaciones importantes antes de subir**
- Evita subir archivos binarios grandes (como el archivo del modelo) si no quieres que el repositorio crezca demasiado. Considera usar `git-lfs` para `random_forest_model.joblib`.
- Crear un archivo `.gitignore` con al menos:

```
.venv/
__pycache__/
*.pyc
model_ml/*.joblib
.env
```

Comandos para agregar `.gitignore` y commitear:

```powershell
# Crear .gitignore (puedes editarlo luego)
@"
.venv/
__pycache__/
*.pyc
model_ml/*.joblib
.env
"@ > .gitignore

git add .gitignore
git commit -m "Añadir .gitignore"
```

**Notas adicionales**
- Si el modelo `random_forest_model.joblib` está fuera del control de versiones, guarda una copia fuera del repo o usa Git LFS. Para instalar y usar Git LFS:

```powershell
choco install git-lfs    # si usas Chocolatey
git lfs install
git lfs track "model_ml/*.joblib"
git add .gitattributes
git add model_ml/random_forest_model.joblib
git commit -m "Añadir modelo con LFS"
git push origin main
```

- Si la ruta a las plantillas cambia, Flask tiene el argumento `template_folder` en `Flask(__name__, template_folder='ui/templates')` (ya configurado en `main.py`).

Si quieres, puedo:
- Generar `requirements.txt` automáticamente con las dependencias detectadas.
- Añadir un archivo `.gitattributes` y configurar Git LFS por ti.
- Crear el repo en GitHub si me das el nombre (usa `gh` CLI o dame permiso para ejecutar comandos localmente).

¡Listo! README creado con los pasos básicos para configurar y subir tu proyecto a GitHub.
