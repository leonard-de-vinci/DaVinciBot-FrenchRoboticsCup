; Auto-generated. Do not edit!


(cl:in-package bot_coordinates-srv)


;//! \htmlinclude TrajectoryGen-request.msg.html

(cl:defclass <TrajectoryGen-request> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0))
)

(cl:defclass TrajectoryGen-request (<TrajectoryGen-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TrajectoryGen-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TrajectoryGen-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name bot_coordinates-srv:<TrajectoryGen-request> is deprecated: use bot_coordinates-srv:TrajectoryGen-request instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <TrajectoryGen-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bot_coordinates-srv:x-val is deprecated.  Use bot_coordinates-srv:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <TrajectoryGen-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bot_coordinates-srv:y-val is deprecated.  Use bot_coordinates-srv:y instead.")
  (y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TrajectoryGen-request>) ostream)
  "Serializes a message object of type '<TrajectoryGen-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TrajectoryGen-request>) istream)
  "Deserializes a message object of type '<TrajectoryGen-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TrajectoryGen-request>)))
  "Returns string type for a service object of type '<TrajectoryGen-request>"
  "bot_coordinates/TrajectoryGenRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TrajectoryGen-request)))
  "Returns string type for a service object of type 'TrajectoryGen-request"
  "bot_coordinates/TrajectoryGenRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TrajectoryGen-request>)))
  "Returns md5sum for a message object of type '<TrajectoryGen-request>"
  "e99dfd300d1e59a2f817598c6d8f754c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TrajectoryGen-request)))
  "Returns md5sum for a message object of type 'TrajectoryGen-request"
  "e99dfd300d1e59a2f817598c6d8f754c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TrajectoryGen-request>)))
  "Returns full string definition for message of type '<TrajectoryGen-request>"
  (cl:format cl:nil "float32 x~%float32 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TrajectoryGen-request)))
  "Returns full string definition for message of type 'TrajectoryGen-request"
  (cl:format cl:nil "float32 x~%float32 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TrajectoryGen-request>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TrajectoryGen-request>))
  "Converts a ROS message object to a list"
  (cl:list 'TrajectoryGen-request
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
))
;//! \htmlinclude TrajectoryGen-response.msg.html

(cl:defclass <TrajectoryGen-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass TrajectoryGen-response (<TrajectoryGen-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TrajectoryGen-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TrajectoryGen-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name bot_coordinates-srv:<TrajectoryGen-response> is deprecated: use bot_coordinates-srv:TrajectoryGen-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <TrajectoryGen-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bot_coordinates-srv:success-val is deprecated.  Use bot_coordinates-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TrajectoryGen-response>) ostream)
  "Serializes a message object of type '<TrajectoryGen-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TrajectoryGen-response>) istream)
  "Deserializes a message object of type '<TrajectoryGen-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TrajectoryGen-response>)))
  "Returns string type for a service object of type '<TrajectoryGen-response>"
  "bot_coordinates/TrajectoryGenResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TrajectoryGen-response)))
  "Returns string type for a service object of type 'TrajectoryGen-response"
  "bot_coordinates/TrajectoryGenResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TrajectoryGen-response>)))
  "Returns md5sum for a message object of type '<TrajectoryGen-response>"
  "e99dfd300d1e59a2f817598c6d8f754c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TrajectoryGen-response)))
  "Returns md5sum for a message object of type 'TrajectoryGen-response"
  "e99dfd300d1e59a2f817598c6d8f754c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TrajectoryGen-response>)))
  "Returns full string definition for message of type '<TrajectoryGen-response>"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TrajectoryGen-response)))
  "Returns full string definition for message of type 'TrajectoryGen-response"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TrajectoryGen-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TrajectoryGen-response>))
  "Converts a ROS message object to a list"
  (cl:list 'TrajectoryGen-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'TrajectoryGen)))
  'TrajectoryGen-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'TrajectoryGen)))
  'TrajectoryGen-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TrajectoryGen)))
  "Returns string type for a service object of type '<TrajectoryGen>"
  "bot_coordinates/TrajectoryGen")