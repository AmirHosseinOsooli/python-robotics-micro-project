# ⚡ Quick Start Guide

Get your maze navigation robot running in **5 minutes**!

## 🔧 Prerequisites Check

```bash
# Check ROS installation
echo $ROS_DISTRO

# Check Python
python --version

# Verify ROS packages
rospack find geometry_msgs
rospack find nav_msgs
```

## 🚀 Run the Project

### Step 1: Launch Simulation (Terminal 1)

```bash
# For TurtleBot
roslaunch turtlebot_gazebo turtlebot_world.launch

# For Summit XL
roslaunch summit_xl_gazebo summit_xl.launch
```

### Step 2: Run Navigation (Terminal 2)

```bash
cd ~/catkin_ws/src/python-robotics-micro-project/src
python maze_navigation.py
```

## 🎯 What You'll See

1. Robot moves forward (~4.4m)
2. Rotates 80° counterclockwise
3. Moves forward again
4. Rotates 80° again
5. Moves forward
6. Rotates 180° clockwise
7. Moves forward twice (exits maze)

## 🔧 Customize Navigation

Edit `maze_navigation.py`:

```python
# Change speed
mr1 = MoveRobot('forward', 0.5, 4)  # 0.5 m/s instead of 1.1

# Change rotation angles in do_maze()
self.rotate(90)  # 90° instead of 80°
```

## 🐛 Quick Troubleshooting

**Robot doesn't move?**
```bash
rostopic echo /cmd_vel
# Should see velocity commands
```

**TF error?**
```bash
rosrun tf tf_echo /odom /base_link
# Should show transform
```

**Import error?**
```bash
# Make sure you're in the right directory
cd ~/catkin_ws/src/python-robotics-micro-project/src
python maze_navigation.py
```

## ✅ Success!

You should see the robot navigating autonomously through the maze!

**Next:** Read full [README.md](README.md) for technical details
