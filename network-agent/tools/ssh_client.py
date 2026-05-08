import paramiko
from config import ROUTER_IP, ROUTER_USER, ROUTER_PASSWORD

class SSHClient:
    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        self.client.connect(
            ROUTER_IP,
            username=ROUTER_USER,
            password=ROUTER_PASSWORD
        )

    def run(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read().decode(), stderr.read().decode()

    def close(self):
        self.client.close()
