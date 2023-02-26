from dronekit import Command, connect, VehicleMode, LocationGlobalRelative
import time
from pymavlink import mavutil


connectinString = '127.0.0.1:14550'
iha = connect(connectinString, wait_ready=True)


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
        print(f"iha hedefe yükseliyor : \n" + str(iha.location.global_relative_frame.alt))

    print("İha istenilen irtifaya yükseldi.\n")


def gorev(X1,Y1,X2,Y2,X3,Y3,X4,Y4):
    

    x_orta1 = (X1+X2)/2
    y_orta1 = (Y1+Y2)/2

    x_ortaa1 = (X3+X4)/2
    y_ortaa1 = (Y3+Y4)/2

    x_orta2 = (X1+x_orta1)/2
    y_orta2 = (Y1+y_orta1)/2

    x_ortaa2 = (X3+x_ortaa1)/2
    y_ortaa2 = (Y3+y_ortaa1)/2

    x_orta3 = (X2 + x_orta1)/2
    y_orta3 = (Y2 + y_orta1)/2

    x_ortaa3 = (X4+x_ortaa1)/2
    y_ortaa3 = (Y4+y_ortaa1)/2

    x_orta4 = (X1+x_orta2)/2
    y_orta4 = (Y1+y_orta2)/2

    x_ortaa4 = (X3+x_ortaa2)/2
    y_ortaa4 = (Y3+y_ortaa2)/2

    x_orta5 = (x_orta2+x_orta1)/2
    y_orta5 = (y_orta2+y_orta1)/2

    x_ortaa5 = (x_ortaa2+x_ortaa1)/2
    y_ortaa5 = (y_ortaa2+y_ortaa1)/2

    x_orta6 = (x_orta3+x_orta1)/2
    y_orta6 = (y_orta3+y_orta1)/2

    x_ortaa6 = (x_ortaa3+x_ortaa1)/2
    y_ortaa6 = (y_ortaa3+y_ortaa1)/2

    x_orta7 = (x_orta3 + X2)/2
    y_orta7 = (y_orta3 + Y2)/2

    x_ortaa7 = (x_ortaa3 + X4)/2
    y_ortaa7 = (y_ortaa3 + Y4)/2

    
    global komut
    komut = iha.commands
    komut.clear()
    time.sleep(1)

    #takeoff
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 0, 10))


    #waypointler
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, X1, Y1, 7))
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, X3, Y3, 7))

    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, x_ortaa4, y_ortaa4, 7))
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, x_orta4, y_orta4, 7))

    #if True:
     #   komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_DELAY, 0, 0, 0, 0, 0, 5, 0, 0, 0))


    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, x_orta2, y_orta2, 7))
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, x_ortaa2, y_ortaa2, 7))

    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, x_ortaa5, y_ortaa5, 7))
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, x_orta5, y_orta5, 7))

    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, x_orta1, y_orta1, 7))
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, x_ortaa1, y_ortaa1, 7))

    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, x_ortaa6, y_ortaa6, 7))
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, x_orta6, y_orta6, 7))

    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, x_orta3, y_orta3, 7))
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, x_ortaa3, y_ortaa3, 7))

    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, x_ortaa7, y_ortaa7, 7))
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, x_orta7, y_orta7, 7))

    while iha.location.global_relative_frame.alt > 13:
        print("irtifa > 13")
        time.sleep(1)

    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, X2, Y2, 7))
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, X4, Y4, 7))


   

    #rtl ---> iha rtl yaptığında irtifa 15 metre ye çıkartıyo 
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    #gorev bitiş doğrulama
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    komut.upload()
    print(" Alan tarama komutlari yukleniyor.\n")
    




armOlVeYuksel(10)

gorev(-35.36311653, 149.16515387, -35.36257891, 149.16515057, -35.36311115, 149.16471547, -35.36257622, 149.16471547)


komut.next = 0
iha.mode = VehicleMode("AUTO")
time.sleep(1)
print(f"iha : " + str(iha.mode) + " moduna alindi.\n")

while True:
    next_komut = komut.next
    print(f"Siradaki komut : {next_komut}\n")
    time.sleep(2.5)
    print(f"Konum X : " + str(iha.location.global_relative_frame.lat))
    print(f"Konum Y : " + str(iha.location.global_relative_frame.lon))
    print(f"Konum Z : " + str(iha.location.global_relative_frame.alt))
    print("----------------------------")
   
    if next_komut is 10:
        print("alanin yarisi tarandi")
        print("alanin yarisi tarandi")
        print("alanin yarisi tarandi")


    time.sleep(1)
    if next_komut is 18:
        print(" Alan Tarama Gorevi Bitti\n")
        

    if next_komut is 20:

        print("RTL yapiliyor...\n")
        time.sleep(3)
        break

