#!/usr/bin/python3.7

import re
import csv
import os

def Scan_rsi():
    '''
    #Objective: 
    #    Scan RSI file and write data in CSV file
    # Input: 
    #   RSI FILE
    # Output:  
    #   Write following data to a CSV file
    #       Junos Version 
    #       Active alarm 
    #       Chassis Type 
    #       Top 5 active demons  
    #       Loopback IP address 
    #       IPv4 Route Count (def and non-def VRF) 
    '''

    #print the doc string of function
    #print(scan_rsi.__doc__)

    # Get the RSI file name/location from user
    fname = str(input('[USER INPUT] RSI File name & path:')) or 'RSI_FILE.txt'

    try:
        with open(fname, mode='r') as fh:
            try:
                with open('rsi_scan_out.csv', mode='w+', newline='') as nh:
                    wr = csv.writer(nh)
                    wr.writerow(['Data Type','Data from RSI'])
                    print('*' * 90)
                    print(f'{"Data Type":<30}{"Data from RSI":<30}')
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
                                    if not re.search('root.*idle:.*cpu[0-9]|WCPU|Free|waiting|last',data):
                                        pl = pl + data.split()[10] + ','
                                        flag += 1
                                        if flag == 5:
                                            break
                                    elif re.search('root@\w+',data):
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
            except:
                print('Oops! Problem While writing data in CSV file.. !!')
            else:
                print('+++++ Writing data into CSV file +++++++')
    except FileNotFoundError:
        print(f'Oops! Problem opening RSI file: {fname}.. please check file name/path!!')
    else:
        print('*' * 90)
    finally:
        print(f'Python Script {os.path.realpath(__file__)} Execution Completed!')

if __name__ == '__main__':
    Scan_rsi()
    