import wpilib

class FrisbeeThrower():

    def __init__(self, robot):

        # Wheel Setup
        self.spinnyWheel = wpilib.Victor(4)

        # Flicker Setup
        self.flicker = wpilib.Victor(6)


        # Misc Variables Setup
        self.wheelSpeed = -.5
        self.flickerSpeed = .3
        self.reverseFlickerSpeed = -.1

    def teleopPeriodic(self, robot):
        # wheel movement and such
        if robot.gamepad.getRawButton(8):
            self.flicker.set(self.flickerSpeed)
        elif robot.gamepad.getRawButton(3):
            self.flicker.set(self.reverseFlickerSpeed)
        else:
            self.flicker.set(0)
            
##        else:
##            self.flicker.set(0)

            
        if robot.gamepad.getRawButton(7):
            self.spinnyWheel.set(self.wheelSpeed)
        else:
            self.spinnyWheel.set(0)

            
        
