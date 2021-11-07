# Expertkompetens
## Project report - Plant monitoring

###### tags: `IoT` `plant` `soil moisture` `temperature` `light`
---
**Table of Contents**


[Tutorial on how to build a device monitoring soil moisture, temperature and light](https://github.com/lneander/iot-lnu-4DV119#tutorial-on-how-to-build-a-device-monitoring-soil-moisture-temperature-and-light)

[Objectives](https://github.com/lneander/iot-lnu-4DV119#objectives)

[Material](https://github.com/lneander/iot-lnu-4DV119#material)

[Environment setup](https://github.com/lneander/iot-lnu-4DV119#environment-setup)

[Putting everything together](https://github.com/lneander/iot-lnu-4DV119#putting-everything-together)

[Limitations and way forward](https://github.com/lneander/iot-lnu-4DV119#limitations-and-way-forward)

[Platforms and infrastructure](https://github.com/lneander/iot-lnu-4DV119#platforms-and-infrastructure)

[Description of functionality](https://github.com/lneander/iot-lnu-4DV119#description-of-functionality)

[The code](https://github.com/lneander/iot-lnu-4DV119#the-code)

[The physical network layer](https://github.com/lneander/iot-lnu-4DV119#the-physical-network-layer)

[Visualisation and user interface](https://github.com/lneander/iot-lnu-4DV119#visualisation-and-user-interface)

[Finalizing the design](https://github.com/lneander/iot-lnu-4DV119#finalizing-the-design)


## Tutorial on how to build a device monitoring soil moisture, temperature and light.

- [ ] The project title is 'Plant monitoring'
- [ ] Lars Neander, participant of the LNU course 4DV119 / Expertkompetens
- [ ] The goal with the project is to implement the full IoT stack from measuring values with sensors and a Lopy4 to visualize the collected data.
- [ ] The time spent on the project is approximately 40 hours.

### Objectives

Water is essential for plants and they need different amount of water depending on the season. It can be useful to have a device that helps us to indicate when a plant actually needs watering.
The purpose of the device is to maximize growth/health of a plant.
The expected insights is how light and temperature affects the need for water.

### Material

In the table below you can find all components needed to build this device. The column "Item Number" contains links to more detailed information.


| Component | Retailer         | Item number | Price [sek] | Description |
| --------- | ---------------- | -----------|------ | ------------ |
| Starter kit | Electrokit.com |[41017619](https://www.electrokit.com/produkt/lnu-1dt305-tillampad-iot-lopy4-and-sensors-bundle/)| 949.00 | Lopy4 and sensors bundle.|
| Lopy4 | Electrokit.com |[Pycom](https://pycom.io/product/lopy4/)| Incl. in starter kit | MicroPython programmable board with analog and digital in-/outputs. Communicates via WiFi, LoRa, Sigfox and Bluetooth.|
| Expansion board | Electrokit.com | [Pycom](https://pycom.io/product/expansion-board-3-0/) | Incl. in starter kit | Enables USB connection to the Lopy4 which is needed during development. Also make it easier to connect the Lopy4's in- and outputs to the breadboard.|
| Breadboard | Electrokit.com |[10160840](https://www.electrokit.com/produkt/kopplingsdack-840-anslutningar/)| Incl. in starter kit | Used for connect components during development. |
| Battery | Electrokit.com | [41012875](https://www.electrokit.com/produkt/batteri-lipo-3-7v-4400mah/) | 249.00| 4400mAh. Used when the device not is connected to a USB cable. |
| Soil moisture sensor | Electrokit.com | [41015738](https://www.electrokit.com/produkt/jordfuktighetssensor/) | 29.00 | Measures the moisture in soil by differences in resistance. Dry soil equals high resistance and high voltage on the analog output signal |
| Temperature sensor | Electrokit.com | [41011628](https://www.electrokit.com/produkt/mcp9700-e-to-to-92-temperaturgivare/) | Incl. in starter kit | Analog temperature sensor with a linear voltage output. |
| Light sensor | Electrokit.com | [40850001](https://www.electrokit.com/produkt/fotomotstand-cds-2-5-kohm/) | Incl. in starter kit | Light sensitive resistor. The more light the less resistance. |
| 10kOhm resistor | Electrokit.com | [41015987](https://www.electrokit.com/produkt/motstand-metallfilm-0-125w-1-10kohm-10k/) | Incl. in starter kit | Standard resistor. |
| Jumper cables | Electrokit.com | [41015221](https://www.electrokit.com/produkt/labbsladdar-100mm-hane-hane-30-pack/) | Incl. in starter kit | Used to connect components on the bread board. |

### Environment setup

In this project Atom has been used as IDE to write the Micropython code. From Atom you can easily transfer your code to the Lopy4. You will at least need a file named main.py which always is executed at startup after the optional boot.py has been executed.

Some overall steps to get started:
- [ ] Install [Node.js](https://nodejs.org/en/download/). Needed to run Atom.
- [ ] Install [Atom](https://atom.io/)
- [ ] Install Pymakr plugin in Atom by selecting menu "File - Settings" in Atom. Select the tab "Install" in the Settings window and search for Pymakr and select install. pymakr is used to connect Atom and Lopy4.
- [ ] Create a file named main.py and use some [example code](https://docs.pycom.io/tutorials/basic/rgbled/) from Pycom to make sure that everything is ok.
- [ ] You upload your project files, see Yellow square in fig. 1, by pressing "Upload project to device" button in the Pymakr console, see red square in fig 1. It's also possible to run a selected file or selected lines in a file by pressing the "Run selected file" button.

More details about "Getting started" can be found on [Pycom website](https://docs.pycom.io/gettingstarted/).

Fig. 1. Atom IDE with Pymakr console at the bottom
![Atom](https://github.com/lneander/iot-lnu-4DV119/blob/main/doc/images/AtomIDE.png?raw=true)


### Putting everything together

For this POC all circuit connections are made on a breadboard.
#### Circuit diagram
Fig. 2.Circuit diagram
![Circuit diagram](https://github.com/lneander/iot-lnu-4DV119/blob/main/doc/images/CircuitDiagram.png?raw=true)

#### Limitations and way forward
For this POC a USB charge has been used as a power source. A commercial version should probably be powered by a battery and the sensors, the Lopy4 and the battery should be placed in a minimalistic box. Due to the battery more consideration should be taken to energy efficiency.


### Platforms and infrastructure

The choice of IoT stack is mainly based on our company strategy. In general we build our own platforms and host them on premise. If a standard solutions are available and is more cost effective it should be used. During this project different platforms has been tested (dotted in the figure ).

Fig. 3. IoT stack
![IoT stack](https://github.com/lneander/iot-lnu-4DV119/blob/main/doc/images/IoTStack.png?raw=true)

The selected solution doesn't cost any extra for my company, we already have web- and database servers.

#### Description of functionality
The sensors are connected to a Lopy4 that regularly measures and post the values to a web service. The web service is just a single .ashx page (ASP.Net Web Handler file) that takes the posted data from the Lopy4 and store it in a MS SQL server database. The collected data is shown on a web page, mostly to make sure that values are collected. To visualize and analyze the data Microsoft BI is used. The self written web service also supports Json formated data from the Helium platform. During devlopment I also tested to use LoRa instead of WiFi. My first test was to send data to Pybytes.


### The code

In boot.py the configuration of the WiFi connection is made. A SD card is also mounted so it can be used to write events to in case of an exception.

Main.py mainly contains a loop that measures sensor values every N seconds and post the data to a service.
The code is as simple as possible and the amount of data posted is minimalistic which is a good feature if LoRa is used to transfer data. The device itself doesn't have any GUI so I use different colors on the LED to signal different states. For example if an exception occurs the LED turns red. If so I can try to restart/soft reset the Lopy4 and if the exception occurs again a examination of the logfile may help to solve the problem.


```
except Exception as e:
      pycom.rgbled(0x050000) # Indicate failure with red light
      with open('/sd/log.txt', 'a') as output:
       output.write(repr(e)) # Write exception to a logfile for later examination
```

### The physical network layer
WiFi is used to send the data via a HTTP Post from the Lopy4 to the service. The format is as minimalistic as possible: [System ID],[Sensor Value 1],[Sensor Value 2],[Sensor Value 3]. To make this work the Lopy4 has to be connected to a WiFi network. The URL to the service is hard-coded in the Micropython code so no configuration is necessary. The choice to use WiFi is based on:
- [ ] Free to use
- [ ] Good coverage
- [ ] No limitation of how much data to transfer
- [ ] Power consumption is not an issue because a USB charger is used as power source

The service is built and tested to also accept Json formated data from the LoRa network Helium. With some changes in code I can start using LoRa if WiFi not is an option. If a battery must be used as the power source some more consideration should be taken to power consumption. For example use deep sleep and not to measure/send data to often.

During this POC a new measurement has been done every 5 minutes.


### Visualisation and user interface

A web page is available to monitor that the system works and gives the possible to use the phone to monitor new values for example when you have watered the plant. I have created a Microsoft BI report to visualize the data. The data is stored in a MS SQL server database. That's what we use at work so thats my choice. No alerts are sent yet,but when enough data is collected I hopefully can determine a limit when the plant needs water. It should be an easy task to trigger a message from the service.

Fig. 4. Web page with sensor values and comments
![ Web page example](https://github.com/lneander/iot-lnu-4DV119/blob/main/doc/images/WebPage.png?raw=true)

Fig. 5. BI report
![BI report](https://github.com/lneander/iot-lnu-4DV119/blob/main/doc/images/BIReport.png?raw=true)


### Finalizing the design

The selected project gives good knowledge of working with IoT devices. From setting up sensors, transfer and store sensor values and finally to display the data. But the time-cycle of watering a plant makes it hard to make any good insights due to the short time period of the project.

My goal was to create a IoT device to get knowledge that I can use at work. Goal accomplished! I'm satisfied with my new knowledge that is a good starting point for working with IoT devices.

Fig. 6. The device doing a measurement
![The device](https://github.com/lneander/iot-lnu-4DV119/blob/main/doc/images/Device1.jpg?raw=true)

Fig. 7. Added (soiled) a cable so the device doesn't have to be in the pot
![The device](https://github.com/lneander/iot-lnu-4DV119/blob/main/doc/images/Device2.jpg?raw=true)

Fig. 8. The first plant to monitor was a lemon tree. The pot is so big so the sensor doesn't detect when watering the plant.
![The device](https://github.com/lneander/iot-lnu-4DV119/blob/main/doc/images/Device3.jpg?raw=true)
