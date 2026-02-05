# 📊 Domiciliaciones con Service Account

## 🔐 Esta es la opción MÁS SEGURA usando Service Account de Google

Tu archivo JSON con las credenciales ya está listo. Ahora solo necesitas configurar el sistema.

## 📁 Estructura de archivos

```
tu-carpeta/
  ├── server.py              (servidor backend)
  ├── index.html             (aplicación web)
  ├── credentials.json       (tu archivo con las credenciales)
  └── requirements.txt       (dependencias de Python)
```

## 🚀 Instalación y Configuración

### Paso 1: Instalar Python (si no lo tienes)

Descarga Python desde: https://www.python.org/downloads/

### Paso 2: Instalar dependencias

Abre tu terminal/consola en la carpeta del proyecto y ejecuta:

```bash
pip install -r requirements.txt
```

### Paso 3: Configurar el archivo credentials.json

Guarda tu archivo JSON que me compartiste como `credentials.json` en la misma carpeta.

### Paso 4: Obtener el ID de tu Google Sheet

1. Abre tu Google Sheet
2. Mira la URL, se verá algo así:
   ```
   https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUaNd3pKDY9XLxXUW8A/edit
   ```
3. El ID es la parte larga entre `/d/` y `/edit`:
   ```
   1BxiMVs0XRA5nFMdKvBdBZjgmUaNd3pKDY9XLxXUW8A
   ```

### Paso 5: Dar acceso a la Service Account

**MUY IMPORTANTE:** Tu Service Account necesita permisos para leer el Google Sheet.

1. Abre tu Google Sheet
2. Haz clic en **"Compartir"**
3. Pega este email (está en tu credentials.json):
   ```
   interaccionesi6-python@interaccionesi6.iam.gserviceaccount.com
   ```
4. Dale permisos de **"Lector"**
5. Haz clic en **"Enviar"**

### Paso 6: Configurar el server.py

Abre `server.py` y edita estas líneas:

```python
SPREADSHEET_ID = 'TU_SPREADSHEET_ID_AQUI'  # ⬅️ Pega el ID del Paso 4
RANGE_NAME = 'Hoja 1!A:H'  # ⬅️ Ajusta el nombre de tu hoja y el rango
```

**Ejemplos de RANGE_NAME:**
- `'Hoja 1!A:H'` - Lee de la columna A hasta la H en "Hoja 1"
- `'Domiciliaciones!A:Z'` - Lee de A a Z en la hoja "Domiciliaciones"
- `'Sheet1!A1:H1000'` - Lee primeras 1000 filas

## ▶️ Ejecutar la aplicación

### Paso 1: Iniciar el servidor

En tu terminal, ejecuta:

```bash
python server.py
```

Deberías ver:
```
🚀 Servidor iniciado en http://localhost:5000
📊 Endpoint de datos: http://localhost:5000/api/data
```

### Paso 2: Abrir la aplicación

Abre tu navegador y ve a:
```
http://localhost:5000
```

¡Listo! Ya deberías ver tus datos. 🎉

## 🔄 Uso diario

1. **Iniciar el servidor:**
   ```bash
   python server.py
   ```

2. **Abrir en el navegador:**
   ```
   http://localhost:5000
   ```

3. **Para actualizar datos:** Haz clic en el botón "🔄 Actualizar Datos"

4. **Para detener el servidor:** Presiona `Ctrl + C` en la terminal

## 🌐 Desplegar en producción

### Opción 1: Render.com (Gratis)

1. Sube tu código a GitHub (sin el credentials.json)
2. Ve a [Render.com](https://render.com)
3. Crea un nuevo "Web Service"
4. Conecta tu repositorio
5. En "Environment Variables", agrega las credenciales

### Opción 2: PythonAnywhere (Gratis)

1. Crea una cuenta en [PythonAnywhere](https://www.pythonanywhere.com)
2. Sube tus archivos
3. Configura una Web App con Flask
4. Sube el credentials.json de forma segura

### Opción 3: Google Cloud Run

1. Crea un contenedor Docker
2. Sube a Google Cloud Run
3. Las credenciales ya estarán disponibles automáticamente

## 🐛 Solución de Problemas

### Error: "No module named 'flask'"

**Solución:** Instala las dependencias
```bash
pip install -r requirements.txt
```

### Error: "Permission denied" al acceder al Sheet

**Solución:** 
- Verifica que compartiste el Sheet con la service account
- El email correcto es: `interaccionesi6-python@interaccionesi6.iam.gserviceaccount.com`

### Error: "Spreadsheet not found"

**Solución:**
- Verifica que el SPREADSHEET_ID sea correcto
- Asegúrate de que la Service Account tenga acceso

### Error: "Invalid credentials"

**Solución:**
- Verifica que el archivo `credentials.json` esté en la carpeta correcta
- Asegúrate de que el JSON sea válido

### Los datos no se muestran en la tabla

**Solución:**
- Verifica los nombres de las columnas en tu Sheet
- Ajusta el mapeo en `index.html` líneas 332-338
- Revisa la consola del navegador (F12) para ver errores

## 🔒 Seguridad

✅ **Ventajas de Service Account:**
- No expones API Keys públicamente
- Control granular de permisos
- Más seguro que publicar el Sheet
- Puedes revocar acceso en cualquier momento

⚠️ **Importante:**
- **NUNCA** subas `credentials.json` a GitHub público
- Añade `credentials.json` a tu `.gitignore`
- Usa variables de entorno en producción

## 📊 Estructura de datos esperada

Tu Google Sheet debe tener estas columnas (o similares):

| Marca temporal | Area_Registro | Dirección de correo electrónico | Registro_SIU | Fecha_Proximo_Cargo | Monto_Domiciliacion | Matricula2 |
|----------------|---------------|----------------------------------|--------------|---------------------|---------------------|------------|
| 8 jul 2025... | Exito Estudiantil | email@example.com | 8 jul 2025 | 10 jul 2025 | 51962406864 | 200588949 |

Si tus columnas tienen otros nombres, ajusta el código en `index.html`.

## 🔄 Actualización automática

El servidor lee los datos directamente desde Google Sheets cada vez que:
- Cargas la página
- Haces clic en "🔄 Actualizar Datos"

No necesitas reiniciar el servidor para ver cambios en el Sheet.

## 💡 Tips

1. **Mantén el servidor corriendo:** Mientras uses la app, el servidor debe estar activo
2. **Puerto ocupado:** Si el puerto 5000 está ocupado, cámbialo en `server.py` (línea final)
3. **Acceso remoto:** Para acceder desde otra computadora, cambia `localhost` por la IP de tu PC
4. **Logs:** El servidor muestra logs en la terminal para debugging

## 📝 Comandos útiles

```bash
# Iniciar servidor
python server.py

# Instalar dependencias
pip install -r requirements.txt

# Ver logs en tiempo real (si usas producción)
tail -f logs/app.log

# Verificar que el servidor está corriendo
curl http://localhost:5000/api/health
```

## 🆘 Soporte

Si tienes problemas:
1. Revisa los logs en la terminal
2. Abre la consola del navegador (F12)
3. Verifica que todos los pasos se completaron
4. Comprueba que la Service Account tiene acceso al Sheet

---

**¿Preguntas?** Revisa primero la sección de "Solución de Problemas" 🔧
