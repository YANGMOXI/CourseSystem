# -*- coding: utf-8 -*-
# date: 2020/7/30 16:31


"""
老师接口层
"""


from db import models


def check_course_interface(tch_name):
    """老师-查看课程"""
    tch_obj = models.Teacher.select(tch_name)
    course_list = tch_obj.show_course()

    if not course_list:
        return False, '当前无安排课程，请联系管理员'

    return True, course_list


def add_tch_course_interface(course_name, tch_name):
    """老师-选择教授课程"""
    tch_obj = models.Teacher.select(tch_name)

    if course_name in tch_obj.tch_course_list:
        return False, f'当前课程：【{course_name}】已存在'

    tch_obj.add_tch_course(course_name)
    return True, f'课程：【{course_name}】添加成功'


def get_course_stu_interface(course_name, tch_name):
    """老师-查看课程下的学生"""
    tch_obj = models.Teacher.select(tch_name)

    stu_list = tch_obj.get_course_stu(course_name)
    if not stu_list:
        return False, '当前课程无学生'

    return True, stu_list


def change_stu_score(course_name, stu_name, score, tch_name):
    """修改学生分数"""
    # 1、获取老师对象，进行分数修改
    tch_obj = models.Teacher.select(tch_name)
    tch_obj.change_score(course_name, stu_name, score)

    return True, '修改成功'


if __name__ == '__main__':
    pass