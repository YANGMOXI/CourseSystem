# -*- coding: utf-8 -*-
# date: 2020/7/30 16:30


"""学生接口层"""

from db import models


def stu_register_interface(username, passwd):
    """学生-注册接口"""
    stu_obj = models.Student.select(username)
    if stu_obj:
        return False, '学生用户名已存在'

    # 保存数据
    stu_obj = models.Student(username, passwd)
    stu_obj.save()

    return True, '注册成功！'


# 登录 直接调 公共接口
# def stu_login_interface(username, passwd):
#     """学生-登录接口"""
#     # 1.判断-用户是否存在
#     stu_obj = models.Student.select(username)
#     if not stu_obj:
#         return False, '用户名不存在，请重新输入'
# 
#     if passwd == stu_obj.pwd:
#         return True, '登录成功！'
#     else:
#         return False, '密码错误！'


def add_sku_interface(sku_name, stu_name):
    """
    选择校区
    :param sku_name: 学校名
    :param stu_name: 学生名
    """
    # 判断-当前学生是否已经在校
    stu_obj = models.Student.select(stu_name)

    if stu_obj.school:
        return False, '当前学生已经选择过学校了'

    stu_obj.add_school(sku_name)
    return True, '选择学校成功'


def get_course_list_interface(stu_name):
    # 判断-学生是否 选择学校
    stu_obj = models.Student.select(stu_name)
    sku_name = stu_obj.school

    if not sku_name:
        return False, '还未选择学校'

    # 查询课程
    sku_obj = models.School.select(sku_name)
    course_list = sku_obj.course_list

    if not course_list:
        return False, '当前校区为开设课程，详情请联系管理员'

    return True, course_list


def add_course_interface(course_name, stu_name):
    """
    选择课程
    :param course_name: 课程名
    :param stu_name: 学生名
    """
    stu_obj = models.Student.select(stu_name)

    if course_name in stu_obj.course_list:
        return False, '当前课程已存在'

    stu_obj.add_course(course_name)
    return True, f'课程：【{course_name}】添加成功'


def check_score_interface(stu_name):
    """查看分数"""
    stu_obj = models.Student.select(stu_name)
    if stu_obj.score_dict:
        return stu_obj.score_dict

    return None


if __name__ == '__main__':
    pass