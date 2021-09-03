
(cl:in-package :asdf)

(defsystem "bot_coordinates-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Coordinates" :depends-on ("_package_Coordinates"))
    (:file "_package_Coordinates" :depends-on ("_package"))
  ))