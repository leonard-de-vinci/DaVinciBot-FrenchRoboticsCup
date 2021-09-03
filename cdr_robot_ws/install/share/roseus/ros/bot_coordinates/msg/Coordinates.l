;; Auto-generated. Do not edit!


(when (boundp 'bot_coordinates::Coordinates)
  (if (not (find-package "BOT_COORDINATES"))
    (make-package "BOT_COORDINATES"))
  (shadow 'Coordinates (find-package "BOT_COORDINATES")))
(unless (find-package "BOT_COORDINATES::COORDINATES")
  (make-package "BOT_COORDINATES::COORDINATES"))

(in-package "ROS")
;;//! \htmlinclude Coordinates.msg.html


(defclass bot_coordinates::Coordinates
  :super ros::object
  :slots (_x _y _theta _xdot _ydot _thetadot ))

(defmethod bot_coordinates::Coordinates
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:theta __theta) 0.0)
    ((:xdot __xdot) 0.0)
    ((:ydot __ydot) 0.0)
    ((:thetadot __thetadot) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _theta (float __theta))
   (setq _xdot (float __xdot))
   (setq _ydot (float __ydot))
   (setq _thetadot (float __thetadot))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:theta
   (&optional __theta)
   (if __theta (setq _theta __theta)) _theta)
  (:xdot
   (&optional __xdot)
   (if __xdot (setq _xdot __xdot)) _xdot)
  (:ydot
   (&optional __ydot)
   (if __ydot (setq _ydot __ydot)) _ydot)
  (:thetadot
   (&optional __thetadot)
   (if __thetadot (setq _thetadot __thetadot)) _thetadot)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
    4
    ;; float32 _theta
    4
    ;; float32 _xdot
    4
    ;; float32 _ydot
    4
    ;; float32 _thetadot
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _theta
       (sys::poke _theta (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _xdot
       (sys::poke _xdot (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _ydot
       (sys::poke _ydot (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _thetadot
       (sys::poke _thetadot (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _theta
     (setq _theta (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _xdot
     (setq _xdot (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _ydot
     (setq _ydot (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _thetadot
     (setq _thetadot (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get bot_coordinates::Coordinates :md5sum-) "d278de612384af14d52c03a0922c6a31")
(setf (get bot_coordinates::Coordinates :datatype-) "bot_coordinates/Coordinates")
(setf (get bot_coordinates::Coordinates :definition-)
      "float32 x
float32 y
float32 theta
float32 xdot
float32 ydot
float32 thetadot
")



(provide :bot_coordinates/Coordinates "d278de612384af14d52c03a0922c6a31")


