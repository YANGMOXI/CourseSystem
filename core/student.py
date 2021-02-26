# -*- coding: utf-8 -*-
# date: 2020/7/30 16:32


"""
- 学生视图
    - 1.注册
    - 2.登录
    - 3.选择校区
    - 4.选择课程（选择学校>> 选择课程）
        - 双向绑定：学生选择课程，课程也选择学生
    - 5.查看分数
"""

from interface import student_interface, common_interface
from lib import common


stu_info = {
    'user': None
}


def register():
    """学生-注册"""
    while True:
        username = input('\033[1;34m {} \033[0m'.format('>>> 请输入用户名:')).strip()
        passwd = input('\033[1;34m {} \033[0m'.format('>>> 请输入密码:')).strip()
        re_passwd = input('\033[1;34m {} \033[0m'.format('>>> 请再次确认密码:')).strip()

        if passwd == re_passwd:
            flag, msg = student_interface.stu_register_interface(
                username,passwd)

            if flag:
                print(f'\033[1;32m {msg} \033[0m')
                break
            else:
                print(f'\033[1;31m {msg} \033[0m')


def login():
    """学生-登录"""
    while True:
        username = input('\033[1;34m {} \033[0m'.format('>>> 请输入用户名:')).strip()
        passwd = input('\033[1;34m {} \033[0m'.format('>>> 请输入密码:')).strip()

        # 登录接口
        flag, msg = common_interface.login_interface(
            username, passwd, user_type='student')

        if flag:
            stu_info['user'] = username
            print(f'\033[1;32m {msg} \033[0m')
            break
        else:
            print(f'\033[1;31m {msg} \033[0m')


@common.auth('student')
def choose_school():
    """学生-选择校区"""
    while True:
        flag, sku_list = common_interface.get_all_sku_interface()

        if not flag:
            print(f'\033[1;31m {sku_list} \033[0m')
            break
        else:
            print('------- 全部校区 -------')
            for index, sku in enumerate(sku_list):
                print(f'编号：{index+1} 校区名称：{sku}')

            choice = input('\033[1;34m {} \033[0m'.format('>>> 请输入校区编号:')).strip()

            if not choice.isdigit():
                print('\033[1;33m {} \033[0m'.format('请输入有效数字'))
                continue

            choice = int(choice)

            if choice not in range(len(sku_list) + 1):
                print('\033[1;33m {} \033[0m'.format('请输入正确编号'))

            sku_name = sku_list[choice - 1]  # 选择学校

            # 学生选择学校接口
            flag, msg = student_interface.add_sku_interface(
                sku_name, stu_info.get('user'))

            if flag:
                print(f'\033[1;32m {msg} \033[0m')
                break
            else:
                print(f'\033[1;31m {msg} \033[0m')
                break



@common.auth('student')
def choose_course():
    """学生-选择学校-课程"""
    while True:
        # 1、获取当前所在学校 所有课程
        flag, course_list = student_interface.get_course_list_interface(
            stu_info.get('user'))

        if not flag:
            print(f'\033[1;31m {course_list} \033[0m')
            break

        else:
            print('------- 全部课程 -------')
            for index, course in enumerate(course_list):
                print(f'编号：{index + 1} 课程名称：{course}')

            choice = input('\033[1;34m {} \033[0m'.format('>>> 请输入选择的课程编号:')).strip()

            if not choice.isdigit():
                print('\033[1;33m {} \033[0m'.format('请输入有效数字'))
                continue

            choice = int(choice)

            if choice not in range(len(course_list) + 1):
                print('\033[1;33m {} \033[0m'.format('请输入正确编号'))

            course_name = course_list[choice - 1]  # 选择课程

            # 调用 学生选择课程接口
            flag, msg = student_interface.add_course_interface(
                course_name, stu_info.get('user'))

            if flag:
                print(f'\033[1;32m {msg} \033[0m')
                break
            else:
                print(f'\033[1;31m {msg} \033[0m')
                break


@common.auth('student')
def check_score():
    """学生-查看课程分数"""
    score_dict = student_interface.check_score_interface(
        stu_info.get('user'))

    if not score_dict:
        print('\033[1;31m {} \033[0m'.format('暂无课程信息，请先报名'))
        return

    else: print(score_dict)
    # for course_name, score in score_dict.items:
    #     print(course_name, score)
        # print(f'课程名称：【{course_name}】 分数：【{score}】')





func_dic = {
    '1': ['注册', register],
    '2': ['登录', login],
    '3': ['选择校区', choose_school],
    '4': ['选择课程', choose_course],
    '5': ['查看分数', check_score],
    'q': ['返回']
}


def stu_view():
    """学生功能主程序"""
    while True:
        print('----- 学生选课功能 -----')
        for k in func_dic:
            print(' ', k, func_dic[k][0])
        print('---------- end ----------')

        choice = input('\033[1;34m {} \033[0m'.format('>>> 请输入功能编号:')).strip()

        if choice == 'q': break

        if choice not in func_dic:
            print('\033[1;33m {} \033[0m'.format('输入有误，请重新输入'))
            continue

        func_dic[choice][1]()



if __name__ == '__main__':
    stu_view()