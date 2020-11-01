// Auto-generated. Do not edit!

// (in-package bot_coordinates.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Coordinates {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x = null;
      this.y = null;
      this.theta = null;
      this.xdot = null;
      this.ydot = null;
      this.thetadot = null;
    }
    else {
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = 0.0;
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = 0.0;
      }
      if (initObj.hasOwnProperty('theta')) {
        this.theta = initObj.theta
      }
      else {
        this.theta = 0.0;
      }
      if (initObj.hasOwnProperty('xdot')) {
        this.xdot = initObj.xdot
      }
      else {
        this.xdot = 0.0;
      }
      if (initObj.hasOwnProperty('ydot')) {
        this.ydot = initObj.ydot
      }
      else {
        this.ydot = 0.0;
      }
      if (initObj.hasOwnProperty('thetadot')) {
        this.thetadot = initObj.thetadot
      }
      else {
        this.thetadot = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Coordinates
    // Serialize message field [x]
    bufferOffset = _serializer.float32(obj.x, buffer, bufferOffset);
    // Serialize message field [y]
    bufferOffset = _serializer.float32(obj.y, buffer, bufferOffset);
    // Serialize message field [theta]
    bufferOffset = _serializer.float32(obj.theta, buffer, bufferOffset);
    // Serialize message field [xdot]
    bufferOffset = _serializer.float32(obj.xdot, buffer, bufferOffset);
    // Serialize message field [ydot]
    bufferOffset = _serializer.float32(obj.ydot, buffer, bufferOffset);
    // Serialize message field [thetadot]
    bufferOffset = _serializer.float32(obj.thetadot, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Coordinates
    let len;
    let data = new Coordinates(null);
    // Deserialize message field [x]
    data.x = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [y]
    data.y = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [theta]
    data.theta = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [xdot]
    data.xdot = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [ydot]
    data.ydot = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [thetadot]
    data.thetadot = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'bot_coordinates/Coordinates';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd278de612384af14d52c03a0922c6a31';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 x
    float32 y
    float32 theta
    float32 xdot
    float32 ydot
    float32 thetadot
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Coordinates(null);
    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = 0.0
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = 0.0
    }

    if (msg.theta !== undefined) {
      resolved.theta = msg.theta;
    }
    else {
      resolved.theta = 0.0
    }

    if (msg.xdot !== undefined) {
      resolved.xdot = msg.xdot;
    }
    else {
      resolved.xdot = 0.0
    }

    if (msg.ydot !== undefined) {
      resolved.ydot = msg.ydot;
    }
    else {
      resolved.ydot = 0.0
    }

    if (msg.thetadot !== undefined) {
      resolved.thetadot = msg.thetadot;
    }
    else {
      resolved.thetadot = 0.0
    }

    return resolved;
    }
};

module.exports = Coordinates;
