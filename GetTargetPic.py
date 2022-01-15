import os
import re
import sys
from os.path import abspath, dirname


class GetTargetPic:
    def __init__(self, modname):
        super(GetTargetPic, self).__init__()
        self.modname = modname  # 类的参数，其他函数都可以调用使用，不用重复赋值
        self.target_file_path = None
        self.target_folder_path = None
        # self.target_folder_path = self.get_target_folder_path(self.modname)  # 声明静态方法后，可以这么用，一般不会这么用
        self.keyword = ".jpg"

    @staticmethod
    def get_target_folder_path(modname):
        """
        不同的模式下，匹配对应文件夹的图片
        :returns: 需要匹配的目标图片地址，如果没有返回空值
        """
        if modname == "御魂":
            target_folder_path = abspath(dirname(__file__)) + r'\img\yuhun'
            # self.find_pic = self.get_target_file_path(target_file_path, ".jpg")
        elif modname == "探索":
            target_folder_path = abspath(dirname(__file__)) + r'\img\tansuo'
        elif modname == "突破":
            target_folder_path = abspath(dirname(__file__)) + r'\img\tupo'
        elif modname == "活动":
            target_folder_path = abspath(dirname(__file__)) + r'\img\huodong'
        elif modname == "觉醒":
            target_folder_path = abspath(dirname(__file__)) + r'\img\juexing'
        elif modname == "百鬼夜行":
            target_folder_path = abspath(dirname(__file__)) + r'\img\baigui'
        elif modname == "微信红包":
            target_folder_path = abspath(dirname(__file__)) + r'\img\wxhongbao'
        else:
            target_folder_path = None
        return target_folder_path

    @property
    def get_target_file_path(self):
        """读取匹配模板图片路径"""
        folder_path = self.get_target_folder_path(self.modname)
        # folder_path = self.target_folder_path
        if folder_path is None:
            print("未找到目标文件夹或图片地址！即将退出！")
            sys.exit(0)  # 脚本结束
        else:
            print("------------------------------------------------------------")
            print("正在读取目标图片(仅限.jpg格式)……")
            self.target_file_path = []
            for cur_dir, sub_dir, included_file in os.walk(folder_path):
                if included_file:
                    for file in included_file:
                        if re.search(self.keyword, file):
                            print(cur_dir + "\\" + file)
                            # print(file)
                            self.target_file_path.append(cur_dir + "\\" + file)
            if len(self.target_file_path) == 0:
                print("未找到目标文件夹或图片地址！")
                sys.exit(0)  # 脚本结束
            print("图片路径读取完成!共[%d]张图片" % len(self.target_file_path))
            print("------------------------------------------------------------")
            return self.target_file_path

    @staticmethod
    def trans_path_to_name(path_string):
        """获取指定文件路径的文件名称"""
        pattern = re.compile(r'([^<>/\\|:"*?]+)\.\w+$')
        data = pattern.findall(path_string)
        if data:
            return data[0]
