# -*- coding: utf-8 -*-
# date: 2020/7/30 22:09


"""
公共接口
"""

import os
from conf import settings
from db import models


def login_interface(username, passwd, user_type):
    """
    公共-登录接口
    :param username:
    :param passwd:
    :param user_type: 'admin' or 'student' or 'teacher'
    """
    if user_type == 'admin':
        obj = models.Admin.select(username)

    elif user_type == 'student':
        obj = models.Student.select(username)

    elif user_type == 'teacher':
        obj = models.Teacher.select(username)

    else:
        return False, '登录角色不对，请重新输入'

    # 判断-用户是否存在
    # 1)用户存在
    if obj:
        if passwd == obj.pwd:
            return True, '登录成功！'
        else:
            return False, '密码错误！'

    # 2)用户不存在
    else:
        return False, '用户名不存在，请重新输入'


def get_all_sku_interface():
    """获取所有学校信息"""
    sku_dir = os.path.join(settings.DB_PATH, 'School')

    # 1）判断-文件夹是否存在
    if not os.path.exists(sku_dir):
        return False, '没有学校，请先联系管理员'

    # 2) 存在，获取文件夹中所有文件名
    sku_list = os.listdir(sku_dir)
    return True, sku_list


def get_all_course_in_sku_interface(sku_name):
    """获取学校的所有课程"""
    sku_obj = models.School.select(sku_name)
    course_list = sku_obj.course_list

    if not course_list:
        return False, '当前校区还未开设课程'

    return True, course_list


if __name__ == '__main__':
    pass