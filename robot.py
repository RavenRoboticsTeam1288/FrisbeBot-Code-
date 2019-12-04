import wpilib
from networktables import NetworkTables
from drivetrain import DrivetrainController
from pivot import pivot_arm
from throw import FrisbeeThrower

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):

        self.sd = NetworkTables.getTable('SmartDashboard')

        #Joystick/gamepad setup
        self.stick1 = wpilib.Joystick(1) #Right
        self.stick2 = wpilib.Joystick(2) #Left
        self.gamepad = wpilib.Joystick(3) #Operator Controller

	#Drivetrain Controller Setup, create the drive control object for the robot
        self.drivetrainController = DrivetrainController(self) 

        #Frisbee Thrower Setup
        self.frisbeeThrower = FrisbeeThrower(self)

        #Thower Angle Setup
        self.pivotArm = pivot_arm(self) 
 
    def autonomousInit(self):
        pass
    
    def autonomousPeriodic(self):
        self.teleopPeriodic()

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):

        #Drivetrain Controller
        self.drivetrainController.teleopPeriodic(self)
		
        #Flywheel and Kicker
        self.frisbeeThrower.teleopPeriodic(self)

        #Pivot Angle
        self.pivotArm.teleopPeriodic(self)

            
if __name__ == '__main__':
    wpilib.run(MyRobot)
