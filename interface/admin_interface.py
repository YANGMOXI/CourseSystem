# -*- coding: utf-8 -*-
# date: 2020/7/30 16:30

"""管理员接口"""

from db import models


def admin_register_interface(username, passwd):
    """管理员-注册接口"""
    # 判断 用户名是否存在
    admin_obj = models.Admin.select(username)
    if admin_obj:
        return False, '用户已存在'

    # 保存数据
    admin_obj = models.Admin(username, passwd)
    admin_obj.save()

    return True, '注册成功！'
    # 密码加密


# 登录 调公共接口
# def admin_login_interface(username, passwd):
#     """管理员-登录接口"""
#     # 1.判断-用户是否存在
#     admin_obj = models.Admin.select(username)
#     if not admin_obj:
#         return False, '用户名不存在，请重新输入'
#
#     # 2.判断-校验密码
#     if passwd == admin_obj.pwd:
#         return True, '登录成功！'
#
#     return False, '密码错误'


def create_school_interface(sku_name, sku_addr, admin_name):
    """
    创建校区接口
    :param admin_name: 创建的管理员
    :param sku_name: 学校名
    :param sku_addr: 学校地址
    """
    # 1.查看当前学校是否存在
    sku_obj = models.School.select(sku_name)

    # 1）已存在
    if sku_obj:
        return False, '该校区已存在'

    # 2）创建学校
    admin_obj = models.Admin.select(admin_name)    # 由管理员创建
    admin_obj.create_school(sku_name, sku_addr)

    return True, f'学校：【{sku_name}】创建成功'


def create_course_interface(sku_name, course_name, admin_name):
    """
    管理员-创建课程
    :param admin_name: 创建的管理员
    :param sku_name: 学校名
    :param course_name: 课程
    """
    sku_obj = models.School.select(sku_name)
    if course_name in sku_obj.course_list:
        return False, '当前课程已存在'

    # 1）不存在，管理员-创建课程
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_course(sku_obj, course_name)

    return True, f'课程：【{course_name}】创建成功，已添加到校区：【{sku_name}】'


def create_teacher_interface(tch_name, admin_name, tch_pwd='123'):
    """
    管理员-创建讲师
    :param tch_name:
    :param admin_name:
    """
    # 1）判断-老师是否存在
    tch_obj = models.Teacher.select(tch_name)
    if tch_obj:
        return False, '当前讲师已存在'

    # 2）不存在-，管理员-创建讲师
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(tch_name, tch_pwd)

    return True, f'讲师：【{tch_name}】创建成功'



if __name__ == '__main__':
    pass