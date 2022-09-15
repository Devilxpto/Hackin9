import subprocess
import pandas as pd

class Spiderfoot:
    def __init__(self, host):
        self.host = host
    
    def scan(self):
        command = f"spiderfoot -s {self.host} -q -o json -u footprint >> temp/{self.host}_spider.txt"
        subprocess.run(command, shell=True)
    
    def process(self):
        self.df = pd.read_json(f'temp/{self.host}_spider.txt')
        return self.df
