
(cl:in-package :asdf)

(defsystem "bot_coordinates-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "TrajectoryGen" :depends-on ("_package_TrajectoryGen"))
    (:file "_package_TrajectoryGen" :depends-on ("_package"))
  ))