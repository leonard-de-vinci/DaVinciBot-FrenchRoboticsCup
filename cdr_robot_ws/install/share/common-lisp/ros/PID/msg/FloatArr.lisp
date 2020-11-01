; Auto-generated. Do not edit!


(cl:in-package PID-msg)


;//! \htmlinclude FloatArr.msg.html

(cl:defclass <FloatArr> (roslisp-msg-protocol:ros-message)
  ((v
    :reader v
    :initarg :v
    :type cl:float
    :initform 0.0)
   (theta
    :reader theta
    :initarg :theta
    :type cl:float
    :initform 0.0))
)

(cl:defclass FloatArr (<FloatArr>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FloatArr>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FloatArr)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name PID-msg:<FloatArr> is deprecated: use PID-msg:FloatArr instead.")))

(cl:ensure-generic-function 'v-val :lambda-list '(m))
(cl:defmethod v-val ((m <FloatArr>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader PID-msg:v-val is deprecated.  Use PID-msg:v instead.")
  (v m))

(cl:ensure-generic-function 'theta-val :lambda-list '(m))
(cl:defmethod theta-val ((m <FloatArr>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader PID-msg:theta-val is deprecated.  Use PID-msg:theta instead.")
  (theta m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FloatArr>) ostream)
  "Serializes a message object of type '<FloatArr>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'v))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'theta))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FloatArr>) istream)
  "Deserializes a message object of type '<FloatArr>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'v) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'theta) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FloatArr>)))
  "Returns string type for a message object of type '<FloatArr>"
  "PID/FloatArr")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FloatArr)))
  "Returns string type for a message object of type 'FloatArr"
  "PID/FloatArr")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FloatArr>)))
  "Returns md5sum for a message object of type '<FloatArr>"
  "a5efdc7608f256f976ad7573b0f4e032")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FloatArr)))
  "Returns md5sum for a message object of type 'FloatArr"
  "a5efdc7608f256f976ad7573b0f4e032")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FloatArr>)))
  "Returns full string definition for message of type '<FloatArr>"
  (cl:format cl:nil "float32 v~%float32 theta~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FloatArr)))
  "Returns full string definition for message of type 'FloatArr"
  (cl:format cl:nil "float32 v~%float32 theta~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FloatArr>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FloatArr>))
  "Converts a ROS message object to a list"
  (cl:list 'FloatArr
    (cl:cons ':v (v msg))
    (cl:cons ':theta (theta msg))
))
