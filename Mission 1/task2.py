# Q2
motorB = ev3_motorB()
motorC = ev3_motorC()

distance = 10
diameter = 5.6
speed = 100
time = 36*speed*distance/(math_pi*diameter)

ev3_runForTime(motorC, time, speed)
ev3_runForTime(motorB, time, speed)

ev3_motorSetStopAction(motorB, 'brake')
ev3_motorSetStopAction(motorC, 'brake')
ev3_pause(time+100)