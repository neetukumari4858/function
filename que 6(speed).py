def function(speed):
    speed1=speed-70
    point=speed1//5
    if speed<70:
        print("ok")
    elif point>=12:
        print("licence suspended")
    elif speed>70:
        print(point,"point")
speed=int(input("enter the speed"))
function(speed)