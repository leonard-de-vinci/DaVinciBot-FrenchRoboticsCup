#ifndef _ROS_PID_IntArr_h
#define _ROS_PID_IntArr_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace PID
{

  class IntArr : public ros::Msg
  {
    public:
      typedef int16_t _ticks_type;
      _ticks_type ticks;
      typedef int16_t _cycles_type;
      _cycles_type cycles;

    IntArr():
      ticks(0),
      cycles(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
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
        int16_t real;
        uint16_t base;
      } u_cycles;
      u_cycles.real = this->cycles;
      *(outbuffer + offset + 0) = (u_cycles.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_cycles.base >> (8 * 1)) & 0xFF;
      offset += sizeof(this->cycles);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
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
        int16_t real;
        uint16_t base;
      } u_cycles;
      u_cycles.base = 0;
      u_cycles.base |= ((uint16_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_cycles.base |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->cycles = u_cycles.real;
      offset += sizeof(this->cycles);
     return offset;
    }

    const char * getType(){ return "PID/IntArr"; };
    const char * getMD5(){ return "5eb3806f964cd135ee7ee4b66ccd08ef"; };

  };

}
#endif
