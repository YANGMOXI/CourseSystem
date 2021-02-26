# -*- coding: utf-8 -*-
# date: 2020/7/30 15:50

"""
公共方法
"""

def auth(role):
    """
    多用户-登录认证装饰器
    :param role: 管理员、学员、讲师
    """
    from core import admin, teacher, student

    def login_auth(func):
        def inner(*args, **kwargs):

            if role == 'admin':
                if admin.user_info.get('user'):
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('\033[1;33m {} \033[0m'.format('请登录后查看'))
                    admin.login()

            elif role == 'teacher':
                if teacher.tch_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('\033[1;33m {} \033[0m'.format('请登录后查看'))
                    teacher.login()

            elif role == 'student':
                if student.stu_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('\033[1;33m {} \033[0m'.format('请登录后查看'))
                    student.login()
            else:
                print('\033[1;33m {} \033[0m'.format('当前视图没有权限'))

        return inner
    return login_auth






if __name__ == '__main__':
    pass