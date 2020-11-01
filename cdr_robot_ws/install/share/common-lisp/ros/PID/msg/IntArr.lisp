; Auto-generated. Do not edit!


(cl:in-package PID-msg)


;//! \htmlinclude IntArr.msg.html

(cl:defclass <IntArr> (roslisp-msg-protocol:ros-message)
  ((ticks
    :reader ticks
    :initarg :ticks
    :type cl:fixnum
    :initform 0)
   (cycles
    :reader cycles
    :initarg :cycles
    :type cl:fixnum
    :initform 0))
)

(cl:defclass IntArr (<IntArr>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <IntArr>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'IntArr)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name PID-msg:<IntArr> is deprecated: use PID-msg:IntArr instead.")))

(cl:ensure-generic-function 'ticks-val :lambda-list '(m))
(cl:defmethod ticks-val ((m <IntArr>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader PID-msg:ticks-val is deprecated.  Use PID-msg:ticks instead.")
  (ticks m))

(cl:ensure-generic-function 'cycles-val :lambda-list '(m))
(cl:defmethod cycles-val ((m <IntArr>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader PID-msg:cycles-val is deprecated.  Use PID-msg:cycles instead.")
  (cycles m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <IntArr>) ostream)
  "Serializes a message object of type '<IntArr>"
  (cl:let* ((signed (cl:slot-value msg 'ticks)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'cycles)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <IntArr>) istream)
  "Deserializes a message object of type '<IntArr>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ticks) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'cycles) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<IntArr>)))
  "Returns string type for a message object of type '<IntArr>"
  "PID/IntArr")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'IntArr)))
  "Returns string type for a message object of type 'IntArr"
  "PID/IntArr")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<IntArr>)))
  "Returns md5sum for a message object of type '<IntArr>"
  "5eb3806f964cd135ee7ee4b66ccd08ef")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'IntArr)))
  "Returns md5sum for a message object of type 'IntArr"
  "5eb3806f964cd135ee7ee4b66ccd08ef")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<IntArr>)))
  "Returns full string definition for message of type '<IntArr>"
  (cl:format cl:nil "int16 ticks~%int16 cycles~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'IntArr)))
  "Returns full string definition for message of type 'IntArr"
  (cl:format cl:nil "int16 ticks~%int16 cycles~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <IntArr>))
  (cl:+ 0
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <IntArr>))
  "Converts a ROS message object to a list"
  (cl:list 'IntArr
    (cl:cons ':ticks (ticks msg))
    (cl:cons ':cycles (cycles msg))
))
