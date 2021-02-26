# -*- coding: utf-8 -*-
# date: 2020/7/30 16:32


"""
- 讲师视图
    - 1.登录
    - 2.查看教授课程
    - 3.选择讲授课程
    - 4.查看课程下的学生
    - 5.修改学生分数
"""

from lib import common
from interface import common_interface, teacher_interface


tch_info = {
    'user': None
}


def login():
    """老师-登录"""
    while True:
        username = input('\033[1;34m {} \033[0m'.format('>>> 请输入用户名:')).strip()
        passwd = input('\033[1;34m {} \033[0m'.format('>>> 请输入密码:')).strip()

        # 登录接口
        flag, msg = common_interface.login_interface(
            username, passwd, user_type='teacher')

        if flag:
            tch_info['user'] = username
            print(f'\033[1;32m {msg} \033[0m')
            break
        else:
            print(f'\033[1;31m {msg} \033[0m')
            break


@common.auth('teacher')
def check_course():
    """讲师-查看教授课程"""
    flag, msg = teacher_interface.check_course_interface(
        tch_info.get('user'))

    if flag:
        print(f'\033[1;32m {msg} \033[0m')
        return
    else:
        print(f'\033[1;31m {msg} \033[0m')



@common.auth('teacher')
def choose_teaching_course():
    """讲师-选择讲授课程"""
    # 1.打印所有学校，并选择
    while True:
        flag, sku_list = common_interface.get_all_sku_interface()

        if not flag:
            print(f'\033[1;31m {sku_list} \033[0m')
            break

        else:
            print('------- 全部校区 -------')
            print('编号\t校区名')
            for i, sku in enumerate(sku_list):
                print(f'{i + 1}  {sku}')

            choice = input('\033[1;34m {} \033[0m'.format('>>> 请输入选择的校区编号:')).strip()
            if not choice.isdigit():
                print('\033[1;33m {} \033[0m'.format('请输入有效数字'))
                continue

            choice = int(choice)
            if choice not in range(len(sku_list) + 1):
                print('\033[1;33m {} \033[0m'.format('请输入正确编号'))

            sku_name = sku_list[choice - 1]  # 选择学校

            # 2.从选择的学校中获取所有课程
            flag, course_list = common_interface.get_all_course_in_sku_interface(
                sku_name)

            if not flag:
                print(f'\033[1;31m {course_list} \033[0m')
                break

            else:
                print('编号\t课程名')
                for j, course in enumerate(course_list):
                    print(f'{j + 1}  {course}')

                choice2 = input('\033[1;34m {} \033[0m'.format('>>> 请输入选择教授的课程编号:')).strip()
                if not choice2.isdigit():
                    print('\033[1;33m {} \033[0m'.format('请输入有效数字'))
                    continue

                choice2 = int(choice2)
                if choice2 not in range(len(course_list) + 1):
                    print('\033[1;33m {} \033[0m'.format('请输入正确编号'))

                course_name = course_list[choice2 - 1]  # 选择课程

            # 3.调用选择教授课程接口
            flag, msg = teacher_interface.add_tch_course_interface(
                course_name, tch_info.get('user'))

            if flag:
                print(f'\033[1;32m {msg} \033[0m')
                break
            else:
                print(f'\033[1;31m {msg} \033[0m')
                break


@common.auth('teacher')
def check_course_student():
    """讲师-查看课程学生"""
    while True:
        # 1、获取当前老师 教授的课程
        flag, course_list = teacher_interface.check_course_interface(
            tch_info.get('user'))

        if not flag:
            print(f'\033[1;31m {course_list} \033[0m')
            break

        else:
            print('编号\t课程名')
            for k, course in enumerate(course_list):
                print(f'{k + 1}   {course}')

            choice = input('\033[1;34m {} \033[0m'.format('>>> 请输入需要查看的课程编号:')).strip()
            if not choice.isdigit():
                print('\033[1;33m {} \033[0m'.format('请输入有效数字'))
                continue

            choice = int(choice)
            if choice not in range(len(course_list) + 1):
                print('\033[1;33m {} \033[0m'.format('请输入正确编号'))

            course_name = course_list[choice - 1]  # 选择查看的课程

            # 2、调用查看课程下的学生接口
            flag2, stu_list = teacher_interface.get_course_stu_interface(
                course_name, tch_info.get('user'))

            if flag2:
                print(f'\033[1;32m {stu_list} \033[0m')
                break
            else:
                print(f'\033[1;31m {stu_list} \033[0m')
                break


@common.auth('teacher')
def change_score():
    """讲师-修改学生分数"""
    while True:
        # 1、获取当前老师 教授的课程
        flag, course_list = teacher_interface.check_course_interface(
            tch_info.get('user'))

        if not flag:
            print(f'\033[1;31m {course_list} \033[0m')
            break

        else:
            print('编号\t课程名')
            for k, course in enumerate(course_list):
                print(f'{k + 1}  {course}')

            choice = input('\033[1;34m {} \033[0m'.format('>>> 请输入需要查看的课程编号:')).strip()
            if not choice.isdigit():
                print('\033[1;33m {} \033[0m'.format('请输入有效数字'))
                continue

            choice = int(choice)
            if choice not in range(len(course_list) + 1):
                print('\033[1;33m {} \033[0m'.format('请输入正确编号'))

            course_name = course_list[choice - 1]  # 选择查看的课程

            # 2、调用查看课程下的学生接口
            flag2, stu_list = teacher_interface.get_course_stu_interface(
                course_name, tch_info.get('user'))

            if not flag2:
                print(f'\033[1;31m {stu_list} \033[0m')
                break

            else:
                print('----------学生花名册----------')
                print('编号\t学生名')
                for m, stu in enumerate(stu_list):
                    print(f'{m + 1}   {stu}')

                choice2 = input('\033[1;34m {} \033[0m'.format('>>> 请输入学生编号:')).strip()
                if not choice2.isdigit():
                    print('\033[1;33m {} \033[0m'.format('请输入有效数字'))
                    continue

                choice2 = int(choice2)
                if choice2 not in range(len(stu_list) + 1):
                    print('\033[1;33m {} \033[0m'.format('请输入正确编号'))

                stu_name = stu_list[choice2 - 1]  # 选择学生

                # 输入-打分
                score = input('\033[1;34m {} \033[0m'.format('>>> 请输入分数:')).strip()
                if not score.isdigit():
                    print('\033[1;33m {} \033[0m'.format('请输入有效数字'))
                    continue

                # 调用修改学生分数接口
                flag3, msg = teacher_interface.change_stu_score(
                    course_name, stu_name, score, tch_info.get('user'))

                if flag3:
                    print(f'\033[1;32m {stu_list} \033[0m')
                    break


func_dic = {
    '1': ['登录', login],
    '2': ['查看教授课程', check_course],
    '3': ['选择讲授课程', choose_teaching_course],
    '4': ['查看课程下的学生', check_course_student],
    '5': ['修改学生分数', change_score],
    'q': ['返回']
}


def tch_view():
    """讲师功能"""
    while True:
        print('----- 讲师功能 -----')
        for k in func_dic:
            print(' ', k, func_dic[k][0])
        print('---------- end ----------')

        choice = input('\033[1;34m {} \033[0m'.format('>>> 请输入功能编号:')).strip()

        if choice in ['q', 'Q']: break

        if choice not in func_dic:
            print('\033[1;33m {} \033[0m'.format('输入有误，请重新输入'))
            continue

        func_dic[choice][1]()




if __name__ == '__main__':
    tch_view()