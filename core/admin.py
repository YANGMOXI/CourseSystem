# -*- coding: utf-8 -*-
# date: 2020/7/30 16:32


"""
- 管理员视图
    - 1.注册
    - 2.登录
    - 3.创建学校
    - 4.创建课程（先选择学校）
    - 5.创建讲师
"""


from interface import admin_interface, common_interface
from lib import common



user_info = {
    'user': None
}


def register():
    while True:
        username = input('\033[1;34m {} \033[0m'.format('>>> 请输入用户名:')).strip()
        passwd = input('\033[1;34m {} \033[0m'.format('>>> 请输入密码:')).strip()
        re_passwd = input('\033[1;34m {} \033[0m'.format('>>> 请确认密码:')).strip()

        if passwd == re_passwd:
            # 注册接口
            flag, msg = admin_interface.admin_register_interface(
                username, passwd)

            if flag:
                print(f'\033[1;32m {msg} \033[0m')
                break
            else:
                print(f'\033[1;31m {msg} \033[0m')

        else: print('\033[1;33m {} \033[0m'.format('两次密码不一致，请重新输入'))



def login():
    while True:
        username = input('\033[1;34m {} \033[0m'.format('>>> 请输入用户名:')).strip()
        passwd = input('\033[1;34m {} \033[0m'.format('>>> 请输入密码:')).strip()

        # 登录接口
        flag, msg = common_interface.login_interface(
            username, passwd, user_type='admin')

        if flag:
            user_info['user'] = username
            print(f'\033[1;32m {msg} \033[0m')
            break
        else:
            print(f'\033[1;31m {msg} \033[0m')


@common.auth('admin')
def create_school():
    """创建校区"""
    while True:
        sku_name = input('\033[1;34m {} \033[0m'.format('>>> 请输入学校名称:')).strip()
        sku_addr = input('\033[1;34m {} \033[0m'.format('>>> 请输入学校地址:')).strip()

        # 调用学校接口
        flag, msg = admin_interface.create_school_interface(
            sku_name, sku_addr, user_info.get('user'))

        if flag:
            print(f'\033[1;32m {msg} \033[0m')
            break
        else:
            print(f'\033[1;31m {msg} \033[0m')


@common.auth('admin')
def create_course():
    while True:
        # 1) 选择学校
        flag, msg = common_interface.get_all_sku_interface()

        if not flag:
            print(f'\033[1;31m {msg} \033[0m')
            break

        for index, sku_name in enumerate(msg):
            print(f'编号：{index + 1} 学校名：{sku_name}')

        # 让学生输入学校编号
        choice = input('\033[1;34m {} \033[0m'.format('>>> 请输入选择的学校编号:')).strip()
        if not choice.isdigit():
            print('\033[1;33m {} \033[0m'.format('请输入有效数字'))
            continue

        choice = int(choice)

        if choice not in range(len(msg) + 1):
            print('\033[1;33m {} \033[0m'.format('请输入正确编号'))

        # 2）选择课程
        sku_name = msg[choice-1]  # 选择学校
        course_name = input('\033[1;34m {} \033[0m'.format('>>> 请输入课程名称:')).strip()

        # 创建课程接口
        flag, msg = admin_interface.create_course_interface(
            sku_name, course_name, user_info.get('user'))

        if flag:
            print(f'\033[1;32m {msg} \033[0m')
            break
        else:
            print(f'\033[1;31m {msg} \033[0m')


@common.auth('admin')
def create_teacher():
    while True:
        tch_name = input('\033[1;34m {} \033[0m'.format('>>> 请输入老师的名字:')).strip()

        # 创建讲师接口
        flag, msg = admin_interface.create_teacher_interface(
            tch_name, user_info.get('user'))

        if flag:
            print(f'\033[1;32m {msg} \033[0m')
            break
        else:
            print(f'\033[1;31m {msg} \033[0m')


func_dic = {
    # 'q': ['返回主菜单'],
    '1': ['注册', register],
    '2': ['登录', login],
    '3': ['创建校区', create_school],
    '4': ['创建课程', create_course],
    '5': ['创建课程讲师', create_teacher],
    'q': ['返回']

}


def admin_view():
    """管理员视图主函数"""
    while True:
        print('------- 管理员功能 -------')
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
    admin_view()