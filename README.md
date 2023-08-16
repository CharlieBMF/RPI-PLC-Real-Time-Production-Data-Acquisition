# RPI-PLC-Real-Time-Production-Data-Acquisition
Script allowing to acquire real time data from Mitsubishi PLC on production line. Acquired data is being sent to API.

# Hardware

1) RaspberryPi4 4GB

![image](https://github.com/CharlieBMF/RPI-PLC-Real-Time-Production-Data-Acquisition/assets/109242797/77af1f65-03b1-4570-8cf1-aad30f068c34)

2) Mitsubishi PLC Q Series (possible to use different type)

![image](https://github.com/CharlieBMF/RPI-PLC-Real-Time-Production-Data-Acquisition/assets/109242797/90649183-77d0-464e-8278-05d2d856b687)

# Topology

It is necessary to connect all PLC CPU's by ETH in one network. RPI script has access to connect with each PLC. 

![image](https://github.com/CharlieBMF/RPI-PLC-Real-Time-Production-Data-Acquisition/assets/109242797/f12275a5-c30a-4335-a190-a75aca4f8a24)

# Description 

The software has been divided into 3 main scripts:
<ol>
  <li> Conf.py - defines each PLC's address, connection, endpoint, data to acquire </li>
  <li> Machines.py - defines class for each machine (PLC) with necessary methods </li>
  <li> main.py - main loop script </li>
</ol>

When the software starts, machine classes are created according to the machines defined in conf.py.


