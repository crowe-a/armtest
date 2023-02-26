#!/usr/bin/env python

#..................................................................................
# Author  :  Bunyamin Ethem Demir
# Github  :  https://github.com/TechnicalVillager
# Website :  http://technicalvillager.github.io/
# Source  :  https://github.com/TechnicalVillager/geo-coords-dronekit/
#..................................................................................

# Import Necessary Packages
from dronekit import connect


# Connecting the Vehicle
connection_string="127.0.0.1:14550"

vehicle = connect(connection_string, baud=57600, wait_ready=True)

# Printing Vehicle's Latitude
print("Vehicle's Latitude              =  ", vehicle.location.global_relative_frame.lat)

# Printing Vehicle's Longitude
print("Vehicle's Longitude             =  ", vehicle.location.global_relative_frame.lon)