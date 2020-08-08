# coding = utf-8

"""

Author:micheryu
Date:2020/3/19
Motto: 能用脑，就别动手~
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os, zipfile, time, mimetypes
from log.logconf import logconf
from config.Config import Config
from common import Consts


class SendReportEmail():
    def __init__(self, path):
        self.path = path
        self.config = Config()

    def Find_File(self):
        """

        :return: 添加文件打包
        """
        # for root,dirs,files in os.walk(path):
        #     print(files)
        files = os.listdir(self.path)
        Newdir = files[-1]
        if Newdir:
            self.path = os.path.join(self.path, Newdir)
            # print(self.path)
            reportpath = self.path + '\\html'
            # for _ in os.listdir(reportpath):
            #     if 'index.html' in _:
            #         # filepath = reportpath + '\\' + _
            #         print(reportpath)
            self.Send_email(self.File_to_Zip(reportpath, self.path))

        else:
            # print('未找到目标源文件：path={0}'.format(self.path))
            logconf().error('本次未找到测试文件:{0}'.format(self.path))

    def File_to_Zip(self, reportpath, Zipfilename):
        """

        :param reportpath: 源文件路径
        :param Zipfilename: 压缩文件路径
        :return: 打包好的文件路径
        """

        reportZip = os.path.join(Zipfilename, 'report.rar')

        filelist = []
        if os.path.isfile(reportpath):
            filelist.append(reportpath)
        else:
            for root, dirs, files in os.walk(reportpath):
                for dir in dirs:
                    filelist.append(os.path.join(root, dir))
                for name in files:
                    filelist.append(os.path.join(root, name))

        zf = zipfile.ZipFile(reportZip, "w", zipfile.zlib.DEFLATED)
        for tar in filelist:
            arcname = tar[len(reportpath):]
            # print(arcname)
            zf.write(tar, arcname)
        zf.close()
        logconf().info('测试报告打包完成{0}'.format(reportZip))
        return reportZip

    def Send_email(self, file):
        """
        :param file: 压缩文件
        :return:   邮件发送状态
        """
        stress_body = Consts.STRESS_LIST
        reslut_body = Consts.RESULT_LIST
        mail_host = self.config.smtpserver
        mail_user = self.config.username
        mail_pwd = self.config.password

        sender = self.config.sender
        receivers = [self.config.receiver]

        mail_title = '主题：测试报告{0}'.format(time.strftime('%Y-%m-%d_%H_%M_%S'))
        # print(file)
        body = 'Hi,all；\n本次接口自动化测试报告如下：\n    接口响应时间集(ms)：{0}\n    接口运行结果集：{1}'.format(stress_body, reslut_body)
        message = MIMEMultipart()
        message['From'] = "{}".format(sender)
        message['To'] = ','.join(receivers)
        message['Subject'] = Header(mail_title, 'utf-8').encode()
        message.attach(
            MIMEText(body + "\n此附件为自动开发，请勿回复/转发;\n查看请解压附件，并使用win10自带浏览器Microsoft Edge \
打开index.html文件，即可在线观看;或使用 pycharm打开index.html 选择谷歌浏览器。"
                     ,
                     'plain', 'utf-8'))

        with open(file, 'rb')as f:
            ctype, encoding = mimetypes.guess_type(file)
            if ctype is None or encoding is not None:
                ctype = 'application/x-zip-compressed'

            maintype, subtype = ctype.split('/', 1)

            # message = MIMEText(mail_body, 'text', 'utf-8')
            mime = MIMEBase(maintype, subtype, filename='测试报告.rar')
            mime.add_header('Content-Disposition', 'attachment', filename='测试报告.rar')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            mime.set_payload(f.read())

        encoders.encode_base64(mime)
        message.attach(mime)

        try:
            smtp = smtplib.SMTP_SSL(mail_host)
            smtp.login(mail_user, mail_pwd)
            smtp.sendmail(sender, receivers, message.as_string())

            # logconf().info('发送测试报告邮件完成')
            smtp.close()
        except smtplib.SMTPException:

            logconf().error('邮件发送失败！！！')
            raise


if __name__ == '__main__':
    SendReportEmail(r'D:\pycharm\PycharmProject\Study\Pytest_AllureProject\report\allure-report').Find_File()
