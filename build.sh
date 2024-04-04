echo "Removing existing build, install, and log directories"
rm -rf build install log
echo "Building ROS 2 packages"
source /opt/ros/humble/setup.bash
colcon build --symlink-install