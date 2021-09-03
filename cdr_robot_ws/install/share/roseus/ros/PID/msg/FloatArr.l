;; Auto-generated. Do not edit!


(when (boundp 'PID::FloatArr)
  (if (not (find-package "PID"))
    (make-package "PID"))
  (shadow 'FloatArr (find-package "PID")))
(unless (find-package "PID::FLOATARR")
  (make-package "PID::FLOATARR"))

(in-package "ROS")
;;//! \htmlinclude FloatArr.msg.html


(defclass PID::FloatArr
  :super ros::object
  :slots (_v _theta ))

(defmethod PID::FloatArr
  (:init
   (&key
    ((:v __v) 0.0)
    ((:theta __theta) 0.0)
    )
   (send-super :init)
   (setq _v (float __v))
   (setq _theta (float __theta))
   self)
  (:v
   (&optional __v)
   (if __v (setq _v __v)) _v)
  (:theta
   (&optional __theta)
   (if __theta (setq _theta __theta)) _theta)
  (:serialization-length
   ()
   (+
    ;; float32 _v
    4
    ;; float32 _theta
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _v
       (sys::poke _v (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _theta
       (sys::poke _theta (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _v
     (setq _v (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _theta
     (setq _theta (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get PID::FloatArr :md5sum-) "a5efdc7608f256f976ad7573b0f4e032")
(setf (get PID::FloatArr :datatype-) "PID/FloatArr")
(setf (get PID::FloatArr :definition-)
      "float32 v
float32 theta
")



(provide :PID/FloatArr "a5efdc7608f256f976ad7573b0f4e032")


