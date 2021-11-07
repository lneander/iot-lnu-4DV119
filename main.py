import time
import socket
import machine
import pycom
import ssl

#with open('/sd/log.txt', 'w') as fs:
    #fs.write('Application started/n/n')

pin21 = machine.DAC('P21')       # Setup output pin used to power the soil moisture sensor. 0 to 3.3V
pin21.write(0)                   # Make sure that the sensor is off

adc = machine.ADC()              # create an "Analog to Digital Conversion" object for analog input pins
pin15 = adc.channel(pin='P15', attn=machine.ADC.ATTN_11DB)   # Soil moisture sensor. Analog value. https://www.electrokit.com/uploads/productfile/41015/41015738_-_Soil_Moisture_Sensor.pdf
pin16 = adc.channel(pin='P16', attn=machine.ADC.ATTN_11DB)   # Light sensor, 0-10 kOhm
pin17 = adc.channel(pin='P17')   # Temp sensor, MCP9700E https://www.electrokit.com/uploads/productfile/41011/21942e-2.pdf

host = 'xxx.yyy.se'

while True:
    try:
        pycom.rgbled(0x000500) # Indicate "New measurement cycle" with green light
        s = socket.socket()
        addr = socket.getaddrinfo(host,80)[0][-1]
        #s = ssl.wrap_socket(s)
        print('socket connected to ' + host)
        s.connect(addr)
        pin21.write(1) # Power up the soil moisture sensor with 3.3V
        time.sleep(0.1) # Short delay before soil moisture is measured.
        data = '1,' + str(pin15.voltage()) + ',' + str(pin16.voltage()) + ',' + str(((pin17.voltage() - 500.0) / 10.0))
        pin21.write(0) # Turn of the soil moisture sensor
        httpreq = 'POST /MessageHandler.ashx HTTP/1.1 \r\nHOST: '+ host + '\r\nContent-Length: ' + str(len(data)) + '\r\nConnection: keep-alive \r\n\r\n' + data
        print(data)
        s.send(httpreq) # We are not interested in the response. Error handling is handled on the server side.
        pycom.heartbeat(False) # Turn of the LED
        time.sleep(2) # Don't close the socket to fast.
        s.close()
        time.sleep(299.9) # 300 seconds = 5 min
    except Exception as e:
        pycom.rgbled(0x050000) # Indicate failure with red light
        with open('/sd/log.txt', 'a') as output:
	       output.write(repr(e)) # Write exception to a logfile for later examination
        #raise e # Don't raise an error. Try to continue the loop.
    else:
        print(data)
