from robot_control_class import RobotControl


class MoveRobot:
    def __init__(self, motion, speed, time):
        self.robotcontrol = RobotControl()
        self.motion = motion
        self.speed = speed
        self.time = time

    def do_maze(self):
        i = 0
        # glf = self.robotcontrol.get_front_laser(360)
        while (i <= 1):
            self.move_straight()
            self.rotate(80)
            i += 1

        self.move_straight()
        self.rotate(-180)
        self.move_straight()
        self.move_straight()

    def move_straight(self):
        self.robotcontrol.move_straight_time(self.motion, self.speed, self.time)

    def rotate(self, degree):
        self.robotcontrol.rotate(degree)


mr1 = MoveRobot('forward', 1.1, 4)
mr1.do_maze()

