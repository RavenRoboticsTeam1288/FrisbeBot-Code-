import wpilib

class pivot_arm():
#None of it works
    def __init__(self, robot):

        self.pivot = wpilib.Victor(8)
        self.pivotspeedup = .3
        self.pivotspeeddown = -.3
        self.pivotArm = False
    def teleopPeriodic(self, robot):

        if robot.gamepad.getRawButton(5):
            self.pivotArm = True
            self.pivot.set(self.pivotspeedup)

        elif robot.gamepad.getRawButton(6):
            self.pivotArm = True
            self.pivot.set(self.pivotspeeddown)

        else:
            self.pivotArm = False
            self.pivot.set(0)
        


