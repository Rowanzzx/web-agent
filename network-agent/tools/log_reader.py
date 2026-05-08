from tools.ssh_client import SSHClient

class LogReader:
    def get_logs(self):
        ssh = SSHClient()
        ssh.connect()

        cmd = "logread | tail -n 200"
        output, error = ssh.run(cmd)

        ssh.close()

        return output
