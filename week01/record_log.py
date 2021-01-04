#week01 作业：编写一个函数, 当函数被调用时，将调用的时间记录在日志中, 日志文件的保存位置建议为：/var/log/python- 当前日期 /xxxx.log

import os
import logging
import time

def recordlog():
    day =  time.strftime("%Y%m%d")
    record_dir =  '/var/log/python-%s/' % day
    recordfile = record_dir + 'userecord.log'
    if os.path.exists(record_dir):
        pass
    else:
        os.makedirs(record_dir)
        
    logging.basicConfig(filename=recordfile,
                        level= logging.DEBUG,
                        datefmt= '%Y-%m-%d %H:%m:%s',
                        format = '%(asctime)s %(name)-8s %(levelname)-8s %(filename)s [lines: %(lineno)d] %(message)s',
                        filemode='a'
                        )
    
    logging.info('now this funciton is used')

if __name__ == '__main__':
    recordlog()
    