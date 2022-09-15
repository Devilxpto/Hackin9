import nmap
import pandas as pd

class Scan:
    def __init__(self, host):
        self.host = host

    def scanhost(self):
        nm = nmap.PortScanner()
        nm.scan(hosts=self.host, arguments='-A')
        f = open('./temp/tempcsvnmap.csv', 'w')
        print(nm.csv(), file=f)
        f.close()
        self.df = pd.read_csv('./temp/tempcsvnmap.csv', sep=';', engine='python')
        return self.df