/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 1.3.36
 * 
 * This file is not intended to be easily readable and contains a number of 
 * coding conventions designed to improve portability and efficiency. Do not make
 * changes to this file unless you know what you are doing--modify the SWIG 
 * interface file instead. 
 * ----------------------------------------------------------------------------- */

#ifndef SWIG_Process_WRAP_H_
#define SWIG_Process_WRAP_H_

namespace Swig {
  class Director;
}


class SwigDirector_Process : public Process, public Swig::Director {

public:
    SwigDirector_Process(VALUE self);
    virtual void operator ()();
    virtual ~SwigDirector_Process();
};


#endif