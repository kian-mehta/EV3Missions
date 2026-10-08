# Q3
motorB = ev3_motorB()
motorC = ev3_motorC()
ev3_runToRelativePosition(motorB, -180, 50)
ev3_runToRelativePosition(motorC, 180, 50)

ev3_motorSetStopAction(motorB, 'brake')
ev3_motorSetStopAction(motorC, 'brake')
ev3_pause(4000)