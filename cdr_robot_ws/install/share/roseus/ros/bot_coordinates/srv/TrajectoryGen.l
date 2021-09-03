;; Auto-generated. Do not edit!


(when (boundp 'bot_coordinates::TrajectoryGen)
  (if (not (find-package "BOT_COORDINATES"))
    (make-package "BOT_COORDINATES"))
  (shadow 'TrajectoryGen (find-package "BOT_COORDINATES")))
(unless (find-package "BOT_COORDINATES::TRAJECTORYGEN")
  (make-package "BOT_COORDINATES::TRAJECTORYGEN"))
(unless (find-package "BOT_COORDINATES::TRAJECTORYGENREQUEST")
  (make-package "BOT_COORDINATES::TRAJECTORYGENREQUEST"))
(unless (find-package "BOT_COORDINATES::TRAJECTORYGENRESPONSE")
  (make-package "BOT_COORDINATES::TRAJECTORYGENRESPONSE"))

(in-package "ROS")





(defclass bot_coordinates::TrajectoryGenRequest
  :super ros::object
  :slots (_x _y ))

(defmethod bot_coordinates::TrajectoryGenRequest
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
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
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass bot_coordinates::TrajectoryGenResponse
  :super ros::object
  :slots (_success ))

(defmethod bot_coordinates::TrajectoryGenResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass bot_coordinates::TrajectoryGen
  :super ros::object
  :slots ())

(setf (get bot_coordinates::TrajectoryGen :md5sum-) "e99dfd300d1e59a2f817598c6d8f754c")
(setf (get bot_coordinates::TrajectoryGen :datatype-) "bot_coordinates/TrajectoryGen")
(setf (get bot_coordinates::TrajectoryGen :request) bot_coordinates::TrajectoryGenRequest)
(setf (get bot_coordinates::TrajectoryGen :response) bot_coordinates::TrajectoryGenResponse)

(defmethod bot_coordinates::TrajectoryGenRequest
  (:response () (instance bot_coordinates::TrajectoryGenResponse :init)))

(setf (get bot_coordinates::TrajectoryGenRequest :md5sum-) "e99dfd300d1e59a2f817598c6d8f754c")
(setf (get bot_coordinates::TrajectoryGenRequest :datatype-) "bot_coordinates/TrajectoryGenRequest")
(setf (get bot_coordinates::TrajectoryGenRequest :definition-)
      "float32 x
float32 y
---
bool success
")

(setf (get bot_coordinates::TrajectoryGenResponse :md5sum-) "e99dfd300d1e59a2f817598c6d8f754c")
(setf (get bot_coordinates::TrajectoryGenResponse :datatype-) "bot_coordinates/TrajectoryGenResponse")
(setf (get bot_coordinates::TrajectoryGenResponse :definition-)
      "float32 x
float32 y
---
bool success
")



(provide :bot_coordinates/TrajectoryGen "e99dfd300d1e59a2f817598c6d8f754c")


