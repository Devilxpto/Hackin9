from classes import getlogs
from classes import nmap_scan
from classes import spider

#collect the logs
try:
    hostname = input('Please enter the hostname to collect logs: ')
    username = input('Please enter the username to collect logs: ')
    port = input('Please enter the tcp port to collect logs: ')
    new_log = getlogs.Getlogs(hostname, username, port)
    new_log.getlogs()
    new_log.processlogs()
except Exception as e:
        print(e)

#create list with unique IPs
unique_ips = new_log.df["src_ip"].unique()
for ip in unique_ips:
    try:
        new_scan = nmap_scan.Scan(ip)
        new_scan.scanhost()
        html_nmap = new_scan.df.to_html()
   
        new_spider = spider.Spiderfoot(ip)
        new_spider.scan()
        new_spider.process()
 
        new_report = open(f'reports/{ip}_report.html', 'w')
        new_report.write(html_nmap)
        new_report.close()
 
        append_report = open(f'reports/{ip}_report.html', 'a')
        types = new_spider.df['type'].to_list()
        processed_types = []
        for type in types:
            if type not in processed_types:
                df_new = new_spider.df[new_spider.df['type'] == type]
                print(f'{df_new}\n')
                html_spider = df_new.to_html()
                append_report.write(html_spider)
                processed_types.append(type)
        append_report.close()
        print(f'Report {ip}_report.html created in Reports folder')
    except Exception as e:
        print(e)