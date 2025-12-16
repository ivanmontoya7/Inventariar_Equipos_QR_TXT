El programa está dividido en 3 partes porque Github no permite más de 20MB en archivos y el ejecutable pesa 28MB. Puedes descargar los 3, seleccionarlos en conjunto, descomprimirlos con 7-Zip, y el resultado será el ejecutable completo.

Descarga la última versión de Python y PyInstaller y ejecuta en la terminal de Python:

pyinstaller --onefile --noconsole Inventario.py

Para crear el .exe sin necesidad de dependencias, dentro de la carpeta dist. El .exe es un portable y no necesita de la carpeta build para funcionar ni del fichero Inventario.spec para funcionar
