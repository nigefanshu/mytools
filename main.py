# from bitcoin_tools import *
import bitcoin_tools
import global_var
import threading
import time, timeit
import sys  # 访问与解释器交互的变量和函数
import os  # 访问操作系统的变量和方法
from multiprocessing import Process, Pool, Pipe
import smtplib
import requests, json
import logging # 日志工具

# bitcoin_tools.compute_target_diff()

# a=[1,2,3,4,]
# b=a[0:2]
# print(b)

bitcoin_tools.compute_target_diff()

