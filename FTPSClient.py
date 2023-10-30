import ftplib
import ssl
import getpass
from utils import progress

class FTPSClient:
    def __init__(self, host, port, timeout=1, user="anonymous", passwd="guest@example.com"):
        self.ftp = ftplib.FTP_TLS()
        self.ftp.connect(host, port, timeout)
        self.ftp.login(user=user, passwd=passwd)
        self.ftp.prot_p()

    def upload_file(self, local_path, remote_path):
        with open(local_path, 'rb') as file:
            self.ftp.storbinary(f'STOR {remote_path}', file, 1024, callback=progress)

    def download_file(self, remote_path, local_path):
        with open(local_path, 'wb') as file:
            self.ftp.retrbinary(f'RETR {remote_path}', file.write, 1024, callback=progress)

    def quit(self):
        self.ftp.quit()

# if __name__ == "__main__":
#     host = input('Host: ')
#     port = int(input('Port: '))
#     timeout = int(input('Timeout: '))
#     user = input('\nUser: ')
#     password = getpass.getpass(prompt='Password: ', stream=None)

#     ftps_client = FTPSClient(host, port, timeout=timeout, user=user, passwd=password)
    
#     try:
#         ftps_client.upload_file('local_file.txt', 'remote_file.txt')
#         ftps_client.download_file('remote_file.txt', 'local_file_downloaded.txt')
#     except ftplib.error_perm as e:
#         print(f"FTPS Error: {e}")
#     finally:
#         ftps_client.quit()
