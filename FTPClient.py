import os
import socket
import ftplib
import getpass
from utils import progress
        
class FTPClient:
    def __init__(self, host, port, timeout=1, user="anonymous", passwd="guest@example.com"):
        self.ftp = ftplib.FTP()
        self.ftp.connect(host, port, timeout)
        self.ftp.login(user=user, passwd=passwd)
        
    def list_files(self):
        self.ftp.retrlines('LIST', callback=print)
        
    def upload_file(self, filename):
        ext = os.path.splitext(filename)[1]
        filepath = os.path.join('files', filename)
        if not os.path.exists(filepath):
            print(f"File '{filename}' does not exist.")
            return
        with open(filepath, 'rb') as file:
            self.ftp.storbinary('STOR %s' % filename, file.write, callback=progress)
            
    def download_file(self, filename):
        filepath = os.path.join('downloads', filename)
        with open(filepath, 'rb') as file:
            self.ftp.retrbinary('RETR %s' % filename, file.write, callback=progress)
            
    def quit(self):
        self.ftp.quit()
        

# if __name__ == "__main__":
#     host = input('Host: ')
#     port = int(input('Port: '))
#     timeout = int(input('Timeout: '))
#     user = input('\n\nUser: ')
#     passwd = getpass.getpass(prompt='Password: ', stream=None)
    
#     ftp_client = FTPClient(host, port, timeout=timeout, user=user, passwd=passwd)
#     try:
#         ftp_client.list_files()
#         ftp_client.upload_file('testfile.txt')
#         ftp_client.download_file('testfile.txt')
#     except ftplib.all_errors as e:
#         print(f"FTP Error: {e}")
#     finally:
#         ftp_client.quit()