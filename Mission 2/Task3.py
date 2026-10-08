# NOT TESTED DO NOT SUBMIT

motorB = ev3_motorB()
motorC = ev3_motorC()

def move_by(distance, dir):
    diameter = 5.6
    speed = 100
    time = 36*speed*distance/(math_pi*diameter)
    
    ev3_runForTime(motorC, time, speed*dir)
    ev3_runForTime(motorB, time, speed*dir)
    
    ev3_motorSetStopAction(motorB, 'brake')
    ev3_motorSetStopAction(motorC, 'brake')
    
    ev3_motorStart(motorB)
    ev3_motorStart(motorC)
    
    ev3_pause(time+100)

def turn_left():
    ev3_runToRelativePosition(motorB, -180, 50)
    ev3_runToRelativePosition(motorC, 180, 50)
    
    ev3_motorSetStopAction(motorB, 'brake')
    ev3_motorSetStopAction(motorC, 'brake')
    ev3_pause(4000)
    
def turn_right():
    ev3_runToRelativePosition(motorB, 180, 50)
    ev3_runToRelativePosition(motorC, -180, 50)
    
    ev3_motorSetStopAction(motorB, 'brake')
    ev3_motorSetStopAction(motorC, 'brake')
    ev3_pause(4000)
    
threshold1 = 10
threshold2 = 20
reverseDistance = 30


sensor = ev3_ultrasonicSensor()

ev3_motorSetSpeed(motorB, 100)
ev3_motorSetSpeed(motorC, 100)


def check(threshold):
    distance = ev3_ultrasonicSensorDistance(sensor)/10
    return distance > threshold
    
while(check(threshold1)):
    ev3_motorStart(motorB)
    ev3_motorStart(motorC)

ev3_motorStop(motorB)
ev3_motorStop(motorC)

shouldTurnRight = random_random() > 0.5


if(shouldTurnRight):
    turn_right()
    while(True):
        move_by(10, 1)
        turn_left()
        if(check(threshold2)):
            break
        turn_right()
else:
    turn_left()
    while(True):
        move_by(10, 1)
        turn_right()
        if(check(threshold2)):
            break
        turn_left()
    

move_by(40, 1)