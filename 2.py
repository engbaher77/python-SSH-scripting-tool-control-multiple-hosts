import sys
import paramiko
import getpass

def ssh_command(ssh):
    #command = input("Command:")
    command = "reboot"
    ssh.invoke_shell()
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read())

def ssh_connect(host, user, key):
    try:
        ssh = paramiko.SSHClient()
        print('Restarting ....')
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=key)

        ssh_command(ssh)
    except Exception as e:
        print('Connection Failed')
        print(e)

if __name__=='__main__':
    #user = input("Username:")
    user = "user_name"
    #key = input("Public key full path:")
    key = "password"
    host = input("Target Hostname:")
    ssh_connect(host, user, key)

