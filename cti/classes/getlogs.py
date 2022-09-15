import paramiko
import json
import pandas as pd

class Getlogs:
    def __init__(self, hostname, username, port):
        self.hostname = hostname
        self.username = username
        self.port = port

    def getlogs(self):
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname, username='csadmin', port='64295')
        sftp = ssh.open_sftp()
        sftp.get('/data/suricata/log/eve.json', 'temp/eve.json')
        sftp.close()
    
    def processlogs(self):
        with open ('temp/eve.json') as f:
            self.df = pd.DataFrame(json.loads(line) for line in f)
        self.df.drop(self.df.loc[self.df['src_ip'] == '10.0.0.4'].index, inplace=True)
        self.df.drop(self.df.loc[self.df['event_type'] != 'alert'].index, inplace=True)
        return self.df