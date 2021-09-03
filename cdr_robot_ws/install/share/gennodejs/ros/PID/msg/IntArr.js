// Auto-generated. Do not edit!

// (in-package PID.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class IntArr {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ticks = null;
      this.cycles = null;
    }
    else {
      if (initObj.hasOwnProperty('ticks')) {
        this.ticks = initObj.ticks
      }
      else {
        this.ticks = 0;
      }
      if (initObj.hasOwnProperty('cycles')) {
        this.cycles = initObj.cycles
      }
      else {
        this.cycles = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type IntArr
    // Serialize message field [ticks]
    bufferOffset = _serializer.int16(obj.ticks, buffer, bufferOffset);
    // Serialize message field [cycles]
    bufferOffset = _serializer.int16(obj.cycles, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type IntArr
    let len;
    let data = new IntArr(null);
    // Deserialize message field [ticks]
    data.ticks = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [cycles]
    data.cycles = _deserializer.int16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'PID/IntArr';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5eb3806f964cd135ee7ee4b66ccd08ef';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16 ticks
    int16 cycles
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new IntArr(null);
    if (msg.ticks !== undefined) {
      resolved.ticks = msg.ticks;
    }
    else {
      resolved.ticks = 0
    }

    if (msg.cycles !== undefined) {
      resolved.cycles = msg.cycles;
    }
    else {
      resolved.cycles = 0
    }

    return resolved;
    }
};

module.exports = IntArr;
