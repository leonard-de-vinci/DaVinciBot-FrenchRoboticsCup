xdotool key Shift+ctrl+o
xdotool key Shift+ctrl+p
xdotool key Shift+ctrl+e
xdotool key Shift+ctrl+n
xdotool key Shift+ctrl+e
xdotool key Shift+ctrl+o

xdotool type 'roscore'
xdotool key Return
sleep 3

xdotool key Shift+ctrl+p
xdotool type 'rosrun guiControl app.py'

xdotool key Shift+ctrl+p
xdotool type 'rosrun tickviewer app.py'

xdotool key Shift+ctrl+p
xdotool type 'sudo chmod 777 /dev/ttyACM0'
xdotool key Return
sleep 2
xdotool type 'dvb'
xdotool key Return
sleep 2
xdotool type 'rqt_graph'

rosrun rosserial_python serial_node.py /dev/ttyACM0