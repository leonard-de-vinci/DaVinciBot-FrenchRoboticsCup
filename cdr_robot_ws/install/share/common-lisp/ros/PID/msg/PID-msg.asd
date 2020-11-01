
(cl:in-package :asdf)

(defsystem "PID-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "FloatArr" :depends-on ("_package_FloatArr"))
    (:file "_package_FloatArr" :depends-on ("_package"))
    (:file "IntArr" :depends-on ("_package_IntArr"))
    (:file "_package_IntArr" :depends-on ("_package"))
  ))