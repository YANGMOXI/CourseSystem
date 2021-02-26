# -*- coding: utf-8 -*-
# date: 2020/7/30 15:50


"""
用户视图层-主视图
"""


from core import admin, student, teacher



func_dic = {
    # '0': ['退出', exit],
    '1': ['管理员功能', admin.admin_view],
    '2': ['学生功能', student.stu_view],
    '3': ['讲师功能', teacher.tch_view]
}


def run():
    while True:
        print("===== 欢迎来到选课系统 =====")
        for i in func_dic:
            print(' ', i, func_dic[i][0])
        print('========== end ==========')


        choice = input('\033[1;34m {} \033[0m'.format('>>> 请输入功能编号:')).strip()
        if choice not in func_dic:
            print('\033[1;33m {} \033[0m'.format('输入有误，请重新输入'))
            continue

        func_dic[choice][1]()



if __name__ == '__main__':
    run()