//导入python api 头文件
#include "Python.h"

//原始函数
int abs(int n){
  if(n<0){
    return n*-1;
  }
  return n;
}

//包装为模块：模块名_方法名  PyObject可以为NULL
static PyObject* template_abs(PyObject* self, PyObject* args){
  int num;
  if(!PyArg_ParseTuple(args,"i",&num)){
    return NULL;//读取整型失败返回NULL
  }
  return (PyObject*)Py_BuildValue("i",abs(num));//构造python对象返回
}

//构造模块方法的数组
static PyMethodDef methods[]={
  {"abs",template_abs,METH_VARARGS},
  {NULL,NULL},
};

//模块结构体
static struct PyModuleDef module={
  PyModuleDef_HEAD_INIT,
  "template",
  NULL,
  -1,
  methods
};

//初始化生成模块  注意命名！！！
void PyInit_template(void){
  PyModule_Create(&module);
}
