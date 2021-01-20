# coding = utf-8

"""

Author:micheryu
Date:2020/3/18
Motto: 能用脑，就别动手~
"""
#
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# import os, zipfile, sys
#
#
# def Find_File(path):
#     # for root,dirs,files in os.walk(path):
#     #     print(files)
#     files = os.listdir(path)
#     if files:
#         for _ in files:
#             if '.html' in _:
#                 filepath = path + '\\' + _
#                 Send_Email(filepath)
#     else:
#         print('未找到目标源文件：path={0}'.format(path))
#
#
#
# def File_to_Zip(dirpath, zipFile):
#     for f in os.listdir(dirpath):
#         absFile = os.path.join(dirpath, f)
#         if os.path.isdir(absFile):
#             relFile = absFile[len(os.getcwd()) + 1:]
#             zipFile.write(relFile)
#             File_to_Zip(absFile, zipFile)
#         else:
#             relFile = absFile[len(os.getcwd()) + 1:]
#             zipFile.write(relFile)
#     return zipFile
#
#
#
#
# zipFilePath=os.path.join(os.getcwd(),'test.zip')
#
# zipFilePath=zipfile.ZipFile(zipFilePath,'w',zipfile.ZIP_DEFLATED)
#
# dirpath=os.getcwd()+'\\allure-report\\2020-03-18_15_38_09\\html'
# print(dirpath)
# print(File_to_Zip(dirpath,zipFilePath))
#
#
#
#
# mail_host = 'smtp.qq.com'
# mail_user = '1475002003@qq.com'
# mail_pwd = 'ydvxplmjdtmmgibd'
#
# sender = '1475002003@qq.com'
# receivers = ['micheryu@163.com']
#
#
# def Send_Email(file):
#     mail_title = '主题：测试报告{0}'.format(file.split('\\')[-3])
#     print(file)
#     f = open(file, 'rb')
#     mail_body = f.read()
#     print(mail_body)
#     f.close()
#
#     message = MIMEText(mail_body, 'text', 'utf-8')
#     message['From'] = "{}".format(sender)
#     message['To'] = ','.join(receivers)
#     message['Subject'] = mail_title
#
#     try:
#         smtp = smtplib.SMTP_SSL('smtp.qq.com')
#         smtp.login(mail_user, mail_pwd)
#         smtp.sendmail(sender, receivers, message.as_string())
#         print("邮件发送成功！！！")
#         smtp.close()
#     except smtplib.SMTPException:
#         print('邮件发送失败！！！')
#
#
# if __name__ == '__main__':
#     Find_File(r'D:\pycharm\PycharmProject\Study\Study\allure-report\2020-03-18_15_38_09\html')

import os,zipfile
def zip_dir(dirname,zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for dir in dirs:
                filelist.append(os.path.join(root,dir))
            for name in files:
                filelist.append(os.path.join(root, name))

    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        print (arcname)
        zf.write(tar,arcname)
    zf.close()

zip_dir(r'D:\pycharm\PycharmProject\Study\Study\allure-report\2020-03-20_11_05_15\html','report.rar')