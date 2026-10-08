# Q4
motorB = ev3_motorB()
motorC = ev3_motorC()
def move_by(distance):
    diameter = 5.6
    speed = 100
    time = 36*speed*distance/(math_pi*diameter)
    
    ev3_runForTime(motorC, time, speed)
    ev3_runForTime(motorB, time, speed)
    
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

move_by(10)
turn_left()
move_by(5)
turn_right()
move_by(15)