#ifndef _ROS_PID_speed_h
#define _ROS_PID_speed_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace PID
{

  class speed : public ros::Msg
  {
    public:
      typedef int16_t _ticks_type;
      _ticks_type ticks;
      typedef bool _dir_type;
      _dir_type dir;

    speed():
      ticks(0),
      dir(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      union {
        int16_t real;
        uint16_t base;
      } u_ticks;
      u_ticks.real = this->ticks;
      *(outbuffer + offset + 0) = (u_ticks.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_ticks.base >> (8 * 1)) & 0xFF;
      offset += sizeof(this->ticks);
      union {
        bool real;
        uint8_t base;
      } u_dir;
      u_dir.real = this->dir;
      *(outbuffer + offset + 0) = (u_dir.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->dir);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      union {
        int16_t real;
        uint16_t base;
      } u_ticks;
      u_ticks.base = 0;
      u_ticks.base |= ((uint16_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_ticks.base |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->ticks = u_ticks.real;
      offset += sizeof(this->ticks);
      union {
        bool real;
        uint8_t base;
      } u_dir;
      u_dir.base = 0;
      u_dir.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->dir = u_dir.real;
      offset += sizeof(this->dir);
     return offset;
    }

    virtual const char * getType() override { return "PID/speed"; };
    virtual const char * getMD5() override { return "191ae91cdfe480496a6f201d593ae3cf"; };

  };

}
#endif
