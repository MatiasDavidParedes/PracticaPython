# PracticaPython
PracticaPython

Crear variables de entorno:

DBA_HOST=
DBA_USER=
DBA_PASSWORD=
DBA_ESQUEMA=
SECRET_PASSWORD_KEY= #Se debe generar una clave 32 url-safe base64-encoded bytes.

Yo lo hice desde PowerShell con este comando

$bytes = New-Object Byte[] 32  # Crea un arreglo de 32 bytes.
(New-Object Security.Cryptography.RNGCryptoServiceProvider).GetBytes($bytes)  # Llena el arreglo con datos aleatorios.
$base64 = [System.Convert]::ToBase64String($bytes) -replace '\+','-' -replace '/','_' -replace '=',''  # Convierte a base64 URL-safe.
$base64


El programa se inicia desde la clase Services/Start.py.

para generar ejecutable: pyinstaller --onefile .\src\Start.py
