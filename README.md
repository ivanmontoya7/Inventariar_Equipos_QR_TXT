El programa está dividido en 3 partes porque Github no permite más de 20MB en archivos y el ejecutable pesa 28MB. Puedes descargar los 3, seleccionarlos en conjunto, descomprimirlos con 7-Zip, y el resultado será el ejecutable completo.

Para compilar el programa y crear un ejecutable, descarga la última versión de Python y PyInstaller y ejecuta en la terminal de Python:

pyinstaller --onefile --noconsole info_pc_qr.py

Dentro de la carpeta /dist/, te creará el .exe, el cual no necesita dependencias ni archivos adicionales para funcionar correctamente.
