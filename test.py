import paramiko
t = paramiko.Transport(('172.96.251.83', 28891))
t.connect(username='root', password='pLkPv8gDigm5')  # 登录远程服务器
sftp = paramiko.SFTPClient.from_transport(t)  # sftp传输协议
src = '/home/meipai/videos/5b91fdf1.mp4'
des = 'D:/5b91fdf1.mp4'
sftp.get(src, des)
t.close()
