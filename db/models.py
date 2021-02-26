# -*- coding: utf-8 -*-
# date: 2020/7/30 16:34


"""
- 用来存放管理类
    - 管理员
    - 学校
    - 讲师
    - 课程
    - 学员
"""


from db import db_handler


class Base:
    def save(self):
        db_handler.save_data(self)    # 保存对象

    @classmethod
    def select(cls, username):
        obj = db_handler.select_data(cls, username)    # 加载对象
        return obj


class Admin(Base):
    """管理员"""
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def create_school(self, sku_name, sku_addr):
        """管理员-创建校区"""
        sku_obj = School(sku_name, sku_addr)    # 实例化School，保存
        sku_obj.save()

    def create_course(self, sku_obj, course_name):
        """管理员-创建课程"""
        course_obj = Course(course_name)
        course_obj.save()
        # 获取学校，添加课程
        sku_obj.course_list.append(course_name)
        sku_obj.save()    # 更新学校数据

    def create_teacher(self, tch_name, tch_pwd):
        """管理员-创建讲师"""
        tch_obj = Teacher(tch_name, tch_pwd)
        tch_obj.save()


class School(Base):
    """校区"""
    def __init__(self, sku_name, addr):
        self.user = sku_name    # 用self.user: db_handler的select_data需统一规范
        self.addr = addr
        self.course_list = []    # 每个校区有相应的课程


class Course(Base):
    """课程"""
    def __init__(self, course_name):
        self.user = course_name
        self.stu_list = []


class Teacher(Base):
    """讲师"""
    def __init__(self, tch_name, tch_pwd):
        self.user = tch_name
        self.pwd = tch_pwd
        self.tch_course_list = []

    def show_course(self):
        """查看教授课程"""
        return self.tch_course_list

    def add_tch_course(self, course_name):
        """老师-添加教授的课程"""
        self.tch_course_list.append(course_name)
        self.save()

    def get_course_stu(self, course_name):
        """查看课程下的学生"""
        course_obj = Course.select(course_name)
        return course_obj.stu_list

    def change_score(self, course_name, stu_name, score):
        """老师-修改学生分数"""
        # 1、获取学生对象，修改分数
        stu_obj = Student.select(stu_name)
        print(stu_obj)
        print(stu_obj.__dict__)

        stu_obj.score_dict[course_name] = score
        stu_obj.save()



class Student(Base):
    """学员"""
    def __init__(self, stu_name, stu_pwd):
        self.user = stu_name
        self.pwd = stu_pwd
        self.school = None    # 一个学生仅有一个校区
        self.course_list = []    # 一个学生可以选择多门课程
        self.score_dict = {}    # {'course': score}
        # self.paid = {}    #  {'course_name': True}

    def add_school(self, sku_name):
        """选择学校"""
        self.school = sku_name
        self.save()

    def add_course(self, course_name):
        """添加学校_课程"""
        self.course_list.append(course_name)
        self.score_dict[course_name] = 0    # 初始分数为0
        self.save()
        # 课程绑定学生
        course_obj = Course.select(course_name)
        course_obj.stu_list.append(self.user)
        course_obj.save()








if __name__ == '__main__':
    pass