//导入python api 头文件
#include "Python.h"

//原始函数
int test(int n){
    while(n<1000000){
        if(n/2==0){
            n++;
            continue;
        }
        if(n/3==0){
            n+=2;
            continue;
        }
        n++;
    }
    return n;
}

int taikong(int i){
  return ++i;
}

//包装为模块：模块名_方法名  PyObject可以为NULL
static PyObject* template_test(PyObject* self, PyObject* args){
  int num;
  if(!PyArg_ParseTuple(args,"i",&num)){//i是衔接类型标识符 表示整型
    return NULL;//读取整型失败返回NULL
  }
  return (PyObject*)Py_BuildValue("i",test(num));//构造python对象返回
}

//构造模块内方法的数组
static PyMethodDef methods[]={
  {"test",template_test,METH_VARARGS},
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
