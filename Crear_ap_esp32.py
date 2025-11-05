# ESP32_PRINCIPAL_AP.py
import network
import time

# Configuración del AP
SSID = "MiRedESP32"
PASSWORD = "12345678"  # Debe tener al menos 8 caracteres

ap = network.WLAN(network.AP_IF)
ap.config(essid=SSID, password=PASSWORD, authmode=network.AUTH_WPA_WPA2_PSK)
ap.active(True)

# Opcional: fijar IP del AP (por defecto suele ser 192.168.4.1)
ap.ifconfig(('192.168.4.1', '255.255.255.0', '192.168.4.1', '8.8.8.8'))

print("ESP32 Principal: Access Point activo")
print("SSID:", SSID)
print("IP del AP:", ap.ifconfig()[0])

(SOLO AP)
