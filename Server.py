import os
import paramiko

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip, rsa_ppk, uname, upgrade):
        # TODO -
        self.server_ip = server_ip
        self.rsa_ppk = rsa_ppk
        self.uname = uname
        self.upgrade = upgrade

    def ping(self):
        # TODO - Use os module to ping the server
        result = os.system("ping -n 5 %s" % self.server_ip)
        return result

    def upgrade(self):
        # # https://blog.ruanbekker.com/blog/2018/04/23/using-paramiko-module-in-python-to-execute-remote-bash-commands/
        ssh = paramiko.SSHClient()
        # https://stackoverflow.com/questions/9963391/how-do-use-paramiko-rsakey-from-private-key
        my_key = paramiko.RSAKey.from_private_key(self.rsa_ppk)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.server_ip, uname=self.uname, pkey=my_key)

        stdin, stdout, stderr = ssh.exec_command(self.command)
        for line in stdout.read().splitlines():
            print(line)
        # Disconnect
        ssh.close()


