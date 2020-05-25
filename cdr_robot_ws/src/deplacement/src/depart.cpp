#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include <wiringPi.h>       
#include "std_msgs/Int16.h"

int main(int argc, char **argv)
{
   setenv("WIRINGPI_GPIOMEM", "1", 1); //On crée l'environnement WIRINGPI_GPIO permettant à ROS de détecter les pins de la Rasp

  ros::init(argc, argv, "Tirette"); //Iniatisation de la node 'Tirette'
  ros::NodeHandle n;
  ros::Publisher pin_go_pub = n.advertise<std_msgs::Int16>("PinGo", 1000); //Création du Publisher "PinGo", publiant 0 si tirette tirée, 1 sinon
  wiringPiSetup();  //'Lancement" de WiringPi

  pinMode(0, INPUT); //wiringPi Pin 0 is BCM_GPIO 17 de la Rasp ; on le met en mode Input
  
  ros::Rate loop_rate(10); //Voir plus bas, à "loop_rate.sleep()"
  int count = 0;

  while (ros::ok())
  {
    std_msgs::Int16 msg; 
    msg.data = digitalRead(0); //On lit la valeur du Pin 0 (donc GPIO 17)
    pin_go_pub.publish(msg); //On publie cette valeur sous forme de Message Int16
    ros::spinOnce(); //On empêche la node de quitter
    loop_rate.sleep(); //Permet, sans rentrer dans les détails, de parcourir cette boucle à une fréquene de 10 Hz, et donc de ne pas surcharger le système ROS en envoyant trop de message
    ++count;
  }
  return 0;
}
