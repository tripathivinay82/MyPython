#!/usr/bin/python3.7

import re
import csv

'''
#Objective: 
#    Scan RSI file and get data 
# Input: 
#   RSI FILE
# Output:  
#   Junos Version 
#   Active alarm 
#   Chassis Type 
#   Top 5 active demons  
#   Loopback IP address 
#   IPv4 Route Count (def and non-def VRF) 
#   Write all the data to a CSV file 
'''

# Function to scan given RSI file and generate output in terminal print and CSV format
def scan_rsi():

    # Get the RSI file name/location from user
    fname = str(input('RSI File name & path:')) or 'RSI_FILE.txt'

    #Open RSI and get the
    with open(fname, mode='r') as fh:
        with open('rsi_scan_out.csv', mode='w+', newline='') as nh:
            wr = csv.writer(nh)
            wr.writerow(['Data Type','Data Mined from RSI'])
            print('*' * 90)
            print(f'{"Data Type":<30}{"Data Mined from RSI":<30}')
            print('*' * 90)
            for data in fh:
                if re.search('^Model: ',data): 
                    wr.writerow(['Chassis Model',data.split()[1]])
                    print(f'{"Chassis Model":<30}{data.split()[1]:<30}')
                elif re.search('Junos:',data): 
                    wr.writerow(['JUNOS Version',data.split()[1]])
                    print(f'{"JUNOS Version":<30}{data.split()[1]:<30}')
                elif re.search('No alarms currently active',data):
                    wr.writerow(['Active Alarm','NO'])
                    print(f'{"Active Alarm":<30}{"NO":<30}')
                elif re.search('[0-9]+.*alarms.*currently.*active',data):
                    wr.writerow(['Active Alarm',data.split()[0]])
                    print(f'{"Active Alarm":<30}{data.split()[0]:<30}')
                elif re.search('show route summary',data):
                    rt_count = []
                    for data in fh:
                        if data.strip() != '':
                            if re.search('^inet.0:|\w+.inet.0:',data):
                                rt_count.append(int(data.split()[3]))
                            elif re.search('root@\w+',data):
                                break
                    wr.writerow(['Total IPv4 Route Count',sum(rt_count)]) 
                    print(f'{"Total IPv4 Route Count":<30}{sum(rt_count):<30}')
                elif re.search('show system processes extensive no-forwarding',data):
                    flag = 0
                    pl = ''
                    for data in fh:
                        if data.strip() != '':
                            if re.search('root.*idle:.*cpu[0-9]|WCPU|Free|waiting|last',data):
                                continue
                            else:
                                pl = pl + data.split()[10] + ','
                                flag += 1
                                if flag == 5:
                                    break
                    wr.writerow(['Top 5 active process',pl])
                    print(f'{"Top 5 active process":<30}{pl:<30}')
                elif re.search('Addresses, Flags: Primary Preferred Is-Default Is-Primary',data):
                    flag = 0
                    for data in fh:
                        if data.strip() != '':
                            if re.search('Destination: Unspecified, Local: [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+',data):
                                wr.writerow(['IPv4 Loopback Address',data.split()[3].split(',')[0]])
                                tmp = data.split()[3].split(',')[0]
                                print(f'{"IPv4 Loopback Address":<30}{tmp:<30}')
                                flag += 1
                                if flag == 2:
                                    break
                            elif re.search('root@\w+',data):
                                break
    print('*' * 90)

if __name__ == '__main__':
    scan_rsi()
