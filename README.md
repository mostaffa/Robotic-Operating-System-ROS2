# Robotic-Operating-System-ROS2-

## Table Of Contents
- [Introduction](#introduction).
- [Installation](#installation).
- [Creating a workspace](#creating-a-workspace).
- [Creating a package](#creating-a-package).
- [Creating a node](#creating-a-node).
- [Ros2 Commands](#ros2-commands).
- [Creating a publisher](#creating-a-publisher).
- [Creating a subscriber](#creating-a-subscriber).
- [Creating a service](#creating-a-service).
- [Creating a client](#creating-a-client).
- [Creating a launch file](#creating-a-launch-file).
- [Creating a parameter file](#creating-a-parameter-file).
- [Creating a action server](#creating-a-action-server).
- [Creating a action client](#creating-a-action-client).
- [Creating a service client](#creating-a-service-client).
- [Creating a service server](#creating-a-service-server).
- [Creating a parameter client](#creating-a-parameter-client).
- [Creating a parameter server](#creating-a-parameter-server).

## Introduction
- ROS2 is a set of software libraries and tools that help you build robot applications. From drivers to state-of-the-art algorithms, and with powerful developer tools, ROS2 has what you need for your next robotics project. And it's all open source.

In this Repo, in `Ubuntu 22.04` a `ros2`, `humble` with `colcon` is used to create a workspace, package, node, publisher, subscriber, service, client, launch file, parameter file, action server, action client, service client, service server, parameter client, and parameter server.

## Installation
- Visit the [ROS2](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html) website to install ROS2 on your system.
- To install ROS2, follow the steps below:
  - Open the terminal and run the following commands:
    ```bash
    locale  # check for UTF-8

    sudo apt update && sudo apt install locales
    sudo locale-gen en_US en_US.UTF-8
    sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
    export LANG=en_US.UTF-8

    locale  # verify settings
    sudo apt install software-properties-common
    sudo add-apt-repository universe
    # add the ROS 2 GPG key with apt.
    sudo apt update && sudo apt install curl -y
    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
    # add the repository to your sources list.
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
    # install ROS 2 packages.
    sudo apt update
    sudo apt install ros-humble-desktop
    sudo apt install ros-dev-tools
    ```

## Creating a workspace
- See the [Create a Work Space](./WORK_SPACE.MD) documentation file in this repo.

## Creating a package
- See the [Create a Package](./CREATE_PACKAGE.MD) documentation file in this repo.

## Creating a node
- See the [Create a Node](./CREATE_NODE.MD) documentation file in this repo.

## Ros2 Commands
- See the [Ros2 Commands](./ROS2_COMMANDS.MD) documentation file in this repo.

## Creating a publisher
- See the [Create a Publisher](./CREATE_PUBLISHER.MD) documentation file in this repo.