import os
import paramiko

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip, rsa_ppk, uname):
        # TODO -
        self.server_ip = server_ip
        self.rsa_ppk = rsa_ppk
        self.uname = uname

    def ping(self):
        # TODO - Use os module to ping the server
        result = os.system("ping -n 5 %s" % self.server_ip)
        return result


