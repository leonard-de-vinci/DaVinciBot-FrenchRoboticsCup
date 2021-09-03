;; Auto-generated. Do not edit!


(when (boundp 'PID::IntArr)
  (if (not (find-package "PID"))
    (make-package "PID"))
  (shadow 'IntArr (find-package "PID")))
(unless (find-package "PID::INTARR")
  (make-package "PID::INTARR"))

(in-package "ROS")
;;//! \htmlinclude IntArr.msg.html


(defclass PID::IntArr
  :super ros::object
  :slots (_ticks _cycles ))

(defmethod PID::IntArr
  (:init
   (&key
    ((:ticks __ticks) 0)
    ((:cycles __cycles) 0)
    )
   (send-super :init)
   (setq _ticks (round __ticks))
   (setq _cycles (round __cycles))
   self)
  (:ticks
   (&optional __ticks)
   (if __ticks (setq _ticks __ticks)) _ticks)
  (:cycles
   (&optional __cycles)
   (if __cycles (setq _cycles __cycles)) _cycles)
  (:serialization-length
   ()
   (+
    ;; int16 _ticks
    2
    ;; int16 _cycles
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _ticks
       (write-word _ticks s)
     ;; int16 _cycles
       (write-word _cycles s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _ticks
     (setq _ticks (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _cycles
     (setq _cycles (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get PID::IntArr :md5sum-) "5eb3806f964cd135ee7ee4b66ccd08ef")
(setf (get PID::IntArr :datatype-) "PID/IntArr")
(setf (get PID::IntArr :definition-)
      "int16 ticks
int16 cycles

")



(provide :PID/IntArr "5eb3806f964cd135ee7ee4b66ccd08ef")


