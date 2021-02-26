# -*- coding: utf-8 -*-
# date: 2020/7/30 15:50


"""
用户保存对象、获取对象
用pickle保存对象
"""

import os, pickle
from conf import settings


def save_data(obj):
    """保存用户数据"""
    # 1.获取“对象”保存文件夹 路径
    class_name = obj.__class__.__name__    # 文件夹名-对象的类名
    user_dir_path = os.path.join(settings.DB_PATH, class_name)

    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 2.拼接 当前用户的pickle文件路径
    user_path = os.path.join(user_dir_path, obj.user)    # 文件名-用户名

    # 3.保存pickle文件
    with open(user_path, 'wb') as f:
        pickle.dump(obj, f)



def select_data(cls, username):
    """查找数据"""
    class_name = cls.__name__  # 文件夹名-对象的类名
    user_dir_path = os.path.join(settings.DB_PATH, class_name)

    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 2.拼接 当前用户的pickle文件路径
    user_path = os.path.join(user_dir_path, username)  # 文件名-用户名

    if os.path.exists(user_path):
        with open(user_path, 'rb') as f:
            pickle_obj = pickle.load(f)
        return pickle_obj

    return None



if __name__ == '__main__':
    pass