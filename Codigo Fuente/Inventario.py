import platform
import psutil
import wmi
import qrcode

c = wmi.WMI()
system_info = c.Win32_ComputerSystem()[0]
bios_info = c.Win32_BIOS()[0]

ram = str(round(psutil.virtual_memory().total / (1024**3)))
disco_duro= str()

disk = psutil.disk_usage('C:\\')
disco_duro = str(round(disk.total / (1024**3)))

data = {
    "Usuario Vinculado": system_info.UserName,
    "Nombre del equipo": system_info.DNSHostName,
    "Numero_serie": bios_info.SerialNumber,
    "Marca": system_info.Manufacturer,
    "Modelo": system_info.SystemFamily,
    "SKU": system_info.SystemSKUNumber,
    "Informacion Adicional Modelo": system_info.Model,
    "RAM": ram + " GB",
    "Disco Duro": disco_duro + " GB",
    "Sistema Operativo": c.Win32_OperatingSystem()[0].Caption,
}

data_txt=str(data)
data_txt=data_txt.replace(",","\n")
data_txt=data_txt.replace("'","")
data_txt=data_txt.replace("{","")
data_txt=data_txt.replace("}","")
img = qrcode.make(data_txt)
img.save("QR.png")
f = open("Informacion_Sistema.txt", "w")
f.write(data_txt)
f.close()