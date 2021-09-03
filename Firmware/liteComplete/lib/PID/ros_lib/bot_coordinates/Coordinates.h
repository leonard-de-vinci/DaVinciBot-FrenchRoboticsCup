#ifndef _ROS_bot_coordinates_Coordinates_h
#define _ROS_bot_coordinates_Coordinates_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace bot_coordinates
{

  class Coordinates : public ros::Msg
  {
    public:
      typedef float _x_type;
      _x_type x;
      typedef float _y_type;
      _y_type y;
      typedef float _theta_type;
      _theta_type theta;
      typedef float _xdot_type;
      _xdot_type xdot;
      typedef float _ydot_type;
      _ydot_type ydot;
      typedef float _thetadot_type;
      _thetadot_type thetadot;

    Coordinates():
      x(0),
      y(0),
      theta(0),
      xdot(0),
      ydot(0),
      thetadot(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_x;
      u_x.real = this->x;
      *(outbuffer + offset + 0) = (u_x.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_x.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_x.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_x.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->x);
      union {
        float real;
        uint32_t base;
      } u_y;
      u_y.real = this->y;
      *(outbuffer + offset + 0) = (u_y.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_y.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_y.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_y.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->y);
      union {
        float real;
        uint32_t base;
      } u_theta;
      u_theta.real = this->theta;
      *(outbuffer + offset + 0) = (u_theta.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_theta.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_theta.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_theta.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->theta);
      union {
        float real;
        uint32_t base;
      } u_xdot;
      u_xdot.real = this->xdot;
      *(outbuffer + offset + 0) = (u_xdot.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_xdot.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_xdot.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_xdot.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->xdot);
      union {
        float real;
        uint32_t base;
      } u_ydot;
      u_ydot.real = this->ydot;
      *(outbuffer + offset + 0) = (u_ydot.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_ydot.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_ydot.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_ydot.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->ydot);
      union {
        float real;
        uint32_t base;
      } u_thetadot;
      u_thetadot.real = this->thetadot;
      *(outbuffer + offset + 0) = (u_thetadot.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_thetadot.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_thetadot.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_thetadot.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->thetadot);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_x;
      u_x.base = 0;
      u_x.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_x.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_x.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_x.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->x = u_x.real;
      offset += sizeof(this->x);
      union {
        float real;
        uint32_t base;
      } u_y;
      u_y.base = 0;
      u_y.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_y.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_y.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_y.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->y = u_y.real;
      offset += sizeof(this->y);
      union {
        float real;
        uint32_t base;
      } u_theta;
      u_theta.base = 0;
      u_theta.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_theta.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_theta.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_theta.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->theta = u_theta.real;
      offset += sizeof(this->theta);
      union {
        float real;
        uint32_t base;
      } u_xdot;
      u_xdot.base = 0;
      u_xdot.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_xdot.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_xdot.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_xdot.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->xdot = u_xdot.real;
      offset += sizeof(this->xdot);
      union {
        float real;
        uint32_t base;
      } u_ydot;
      u_ydot.base = 0;
      u_ydot.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_ydot.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_ydot.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_ydot.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->ydot = u_ydot.real;
      offset += sizeof(this->ydot);
      union {
        float real;
        uint32_t base;
      } u_thetadot;
      u_thetadot.base = 0;
      u_thetadot.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_thetadot.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_thetadot.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_thetadot.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->thetadot = u_thetadot.real;
      offset += sizeof(this->thetadot);
     return offset;
    }

    virtual const char * getType() override { return "bot_coordinates/Coordinates"; };
    virtual const char * getMD5() override { return "d278de612384af14d52c03a0922c6a31"; };

  };

}
#endif
