# Copyright (c) 2018 GenYuanLian
# -*- coding: utf-8 -*-


def _init():  # 初始化
    global _global_dict
    _global_dict = {}


def set_value(key, value):
    _global_dict[key] = value


def get_value(key, defvalue=None):
    try:
        return _global_dict[key]
    except KeyError:
        return defvalue

subsidy = {}
