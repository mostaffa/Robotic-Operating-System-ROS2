# Ros2 Commands

## Prerequisites
- [Creating a workspace](./WORK_SPACE.MD)
- [Creating a package](./CREATE_PACKAGE.MD)
- [Creating a node](./CREATE_NODE.MD)

## Commands
1. 
```bash
ros2 run package_name executable_name
# where package_name is the name of the package and executable_name is the name of the executable.
```
2. 
```bash
 # To show all the nodes in the system.
 ros2 node list
 ```
3. 
```bash
 # To show the information about a node.
 ros2 node info node_name
 ```
4. 
```bash
 # To show the information about a topic.
 ros2 topic info topic_name
 ```
5. 
```bash
 # To show All topics.
 ros2 topic list
 ```
 6.  
 ```bash
 # To show the information about a service.
 ros2 interface show /topic_name
 ```
 7. 
```bash
# To show all the services, in GUI.
rqt_graph
```
8. 
```bash
# To show all messages.
ros2 topic echo /topic_name
