# Se agrega la libreria PySerial
import serial 
# Se agrega la libreria time para poder dar un tiempo para que se abra el puerto serial
import time

# Instancia del puerto de lectura y tiempo maximo de espera
arduinoActuacion = serial.Serial('COM4', 250000, timeout = 2) 
time.sleep(1) #Tiempo para la la apertura del puerto serial
arduinoActuacion.flush()
arduinoActuacion.setDTR()

# for x in range (1, 10):
print("Se envio")
dato = str("Se envio")
arduinoActuacion.write(dato.encode('utf-8'))
arduinoActuacion.flush()
time.sleep(0.1)
arduinoActuacion.close()