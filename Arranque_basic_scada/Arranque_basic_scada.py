
import serial
import time
'''Este programa debe estar arrancado siempre que visualizemos el Scada, ya que es el que actualiza
	los datos que circulan entre el controlador Web2py y nuestro arduino'''

puerta_Serie_1=serial.Serial('/dev/ttyACM0',9600,timeout=0.1)

while True:
	pot = puerta_Serie_1.readline()
	print pot
	time.sleep(1)
	try:
		temp = open('datos_bscada.txt','w')
		temp.write(pot)
		temp.close()
	except:
		pass
	try:
		puerta = open('datos_bscada_2.txt','r')
		estado_puerta = puerta.read()
		puerta.close()
	except:
		estado_puerta = 'c'
	puerta_Serie_1.write(estado_puerta)
	time.sleep(0.1)
	if pot == 'fin':
		break
