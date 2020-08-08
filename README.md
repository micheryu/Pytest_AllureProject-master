# API_Automation
基于Pytest+request+Allure的接口自动化开源框架

----
#### 模块类的设计
common  公共方法
    `Request.py` 封装request方法，可以支持多协议扩展（get\post\put）
    `Assert.py` 封装assert方法
    `Session.py` 封装获取登录token方法
    `Hash.py` 封装常用加密方法
    'Consts.py'  定义全局变量
    'Shell.py'   封装shell脚本
    'base.py'     封装驱动配置

config   配置文件
    `Config.py`读取配置文件，包括：不同环境的配置

log      日志模块
    logconf.py   读取yaml文件log配置

page     接口页面

Params   参数配置
    params.py   返回接口参数
    tools.py    读取yaml文件接口配置

report    报告文件

    `SendReport.py`封装smtplib方法，运行结果发送邮件通知


testcases   测试用例文件
    `Run.py` 核心代码。定义并执行用例集，生成报告

----
####
