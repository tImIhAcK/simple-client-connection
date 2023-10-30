from FTPClient import FTPClient
from SFTPClient import SFTPClient
from FTPSClient import FTPSClient
import paramiko
import getpass
import ftplib

if __name__ == "__main__":
    print("Choose a file transfer method:")
    print("1. FTPClient")
    print("2. SFTPClient")
    print("3. FTPSClient")
    
    choice = input("Enter the number of your choice: ")

    host = input('Host: ')
    port = int(input('Port: '))
    timeout = int(input('Timeout: '))
    user = input('User: ')
    password = getpass.getpass(prompt="Password: ", stream=None)
    if choice == '1':
        ftp_client = FTPClient(host, port, timeout, user, password)
        try:
            ftp_client.list_files()
            ftp_client.upload_file('testfile.txt')
            ftp_client.download_file('testfile.txt')
        except ftplib.all_errors as e:
            print(f"FTP Error: {e}")
        finally:
            ftp_client.quit()
    elif choice == '2':
        sftp_client = SFTPClient(host, port, user, password)
        try:
            sftp_client.upload_file('local_file.txt', 'remote_file.txt')
            sftp_client.download_file('remote_file.txt', 'local_file_downloaded.txt')
        except paramiko.SSHException as e:
            print(f"SFTP Error: {e}")
        finally:
            sftp_client.close()
    elif choice == '3':
        ftps_client = FTPSClient(host, port, timeout, user, password)
        try:
            ftps_client.upload_file('local_file.txt', 'remote_file.txt')
            ftps_client.download_file('remote_file.txt', 'local_file_downloaded.txt')
        except ftplib.error_perm as e:
            print(f"FTPS Error: {e}")
        finally:
            ftps_client.quit()
    else:
        print("Invalid choice. Please select 1, 2, or 3 for the corresponding option.")
