#ifndef _ROS_bot_coordinates_movement_h
#define _ROS_bot_coordinates_movement_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace bot_coordinates
{

  class movement : public ros::Msg
  {
    public:
      typedef float _x_type;
      _x_type x;
      typedef float _y_type;
      _y_type y;
      typedef float _epsilon_type;
      _epsilon_type epsilon;
      typedef int32_t _mod_type;
      _mod_type mod;

    movement():
      x(0),
      y(0),
      epsilon(0),
      mod(0)
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
      } u_epsilon;
      u_epsilon.real = this->epsilon;
      *(outbuffer + offset + 0) = (u_epsilon.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_epsilon.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_epsilon.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_epsilon.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->epsilon);
      union {
        int32_t real;
        uint32_t base;
      } u_mod;
      u_mod.real = this->mod;
      *(outbuffer + offset + 0) = (u_mod.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_mod.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_mod.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_mod.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->mod);
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
      } u_epsilon;
      u_epsilon.base = 0;
      u_epsilon.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_epsilon.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_epsilon.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_epsilon.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->epsilon = u_epsilon.real;
      offset += sizeof(this->epsilon);
      union {
        int32_t real;
        uint32_t base;
      } u_mod;
      u_mod.base = 0;
      u_mod.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_mod.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_mod.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_mod.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->mod = u_mod.real;
      offset += sizeof(this->mod);
     return offset;
    }

    virtual const char * getType() override { return "bot_coordinates/movement"; };
    virtual const char * getMD5() override { return "157db54e3c9d56ffd859a3461ad9d12b"; };

  };

}
#endif
