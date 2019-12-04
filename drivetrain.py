import wpilib
from wpilib.drive import MecanumDrive

class DrivetrainController:

    def __init__(self, robot):
        
        #Motor Setup
        self.frontRightMotor = wpilib.Victor(2) #Yellow doesn't
        self.frontLeftMotor = wpilib.Victor(3) #Blue 
        self.backRightMotor = wpilib.Victor(0) #Red
        self.backLeftMotor = wpilib.Victor(5) #Orange doesn't

        #Mechanum Drive setup
        robot.drive = MecanumDrive(self.frontLeftMotor,
                                    self.backLeftMotor,
                                    self.frontRightMotor,
                                    self.backRightMotor)

    def teleopPeriodic(self, robot):

        #Joystick Axis'
        stick1_X = robot.stick1.getX()
        stick2_X = robot.stick2.getX()
        stick1_Y = robot.stick1.getY()

        #Dead Zone
        if stick1_X > -.05 and stick1_X < .05:
            stick1_X = 0
        if stick2_X > -.05 and stick2_X < .05:
            stick2_X = 0
        if stick1_Y > -.05 and stick1_Y < .05:
            stick1_Y = 0

        #Movement Setup
        robot.drive.driveCartesian( stick2_X, stick1_Y, stick1_X, 0)

    def autonomousInit(self, robot):
        robot.drive.setSafteyEnabled( False )

    def teleopInit(self, robot):
        robot.drive.setSafteyEnabled( True )
