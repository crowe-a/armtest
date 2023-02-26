from dronekit import Command, connect, VehicleMode, LocationGlobalRelative
import time
from pymavlink import mavutil




connectinString = '127.0.0.1:14550'
iha = connect(connectinString, wait_ready=True)
komut = iha.commands

def armOlVeYuksel(irtifa):
    while iha.is_armable is not True:
        print("iha arm edilebilir durumda değil.\n")
        time.sleep(1)
    
    print("iha arm edilebilir durumda.\n")

    iha.mode = VehicleMode("GUIDED")
    time.sleep(1)

    print("iha " +str(iha.mode)+ " moduna alindi.\n")

    iha.armed = True
    while iha.armed is not True:
        print("iha arm ediliyor...\n")
        time.sleep(1)
    print("iha arm edildi.\n")

    iha.simple_takeoff(irtifa)

    while iha.location.global_relative_frame.alt < irtifa*0.91:
        time.sleep(1)
        print(f"iha hedefe yükseliyor : " + str(iha.location.global_relative_frame.alt))
        print("iha's Latitude              =  ", iha.location.global_relative_frame.lat)
        print("iha's Longitude             =  ", iha.location.global_relative_frame.lon)

    print("İha istenilen irtifaya yükseldi.\n")
    time.sleep(5)
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH, 0, 0, 0, 0, 0, 0, 0, 0, 0))


armOlVeYuksel(5)
