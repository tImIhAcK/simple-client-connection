import paramiko
import getpass

class SFTPClient:
    def __init__(self, host, port, username, password):
        self.transport = paramiko.Transport((host, port))
        self.transport.connect(username=username, password=password)
        self.sftp = self.transport.open_sftp()

    def upload_file(self, local_path, remote_path):
        self.sftp.put(local_path, remote_path)

    def download_file(self, remote_path, local_path):
        self.sftp.get(remote_path, local_path)

    def close(self):
        self.sftp.close()
        self.transport.close()

# if __name__ == "__main__":
#     host = input('Host: ')
#     port = int(input('Port: '))
#     username = input('Username: ')
#     password = getpass.getpass(prompt='Password: ', stream=None)

#     sftp_client = SFTPClient(host, port, username, password)
    
#     try:
#         sftp_client.upload_file('local_file.txt', 'remote_file.txt')
#         sftp_client.download_file('remote_file.txt', 'local_file_downloaded.txt')
#     except paramiko.SSHException as e:
#         print(f"SFTP Error: {e}")
#     finally:
#         sftp_client.close()
