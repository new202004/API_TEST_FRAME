import os
import logging

current_path = os.path.dirname(__file__)  # 获取路径
log_path = os.path.join(current_path, '../log/test.log')


class LogUtils:
    def __init__(self, log_file_path=log_path):
        self.log_file_path = log_file_path
        self.logger = logging.getLogger(__name__)  # 创建一个日志对象 定义一个名词
        self.logger.setLevel(level=logging.INFO)  # 设置全局日志基本  debug info worning error
        console = logging.StreamHandler()  #创建一个控制台输出日志的对象
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console.setFormatter(formatter)

        file_log = logging.FileHandler(log_path,)
        file_log.setFormatter(formatter)
        self.logger.addHandler(console)  # 日志对象配置在控制台输出
        self.logger.addHandler(file_log)  # 日志对象配置在文件中输出

    def info(self, message):
        self.logger.info(message)


if __name__ == '__main__':
    LogUtils().info('newdream')
