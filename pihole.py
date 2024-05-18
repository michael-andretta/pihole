### Import Libraries ###
import os
import sys
import time
import paramiko

### Import Secret ###
from env_vars.secrets import ph_user, ph_pass, ph_ip

### Define Functions ###
def ssh_connect():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ph_ip, username=ph_user, password=ph_pass)
    return ssh

def pihole_question():
    reply = str(input('Do you want to update Pi-hole? (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return print('Invalid input. Please enter "y" or "n".')

def check_for_update():
    ssh = ssh_connect()
    stdin, stdout, stderr = ssh.exec_command('pihole -v')
    for line in stdout:
        if 'Pi-hole version' in line:
            current_version = line.split(' ')[5].strip()
            new_version = line.split(' ')[-1].strip().replace('(', '').replace(')', '')
    if current_version == new_version:
        print('Pi-hole is up to date')
    else:
        print(f'Pi-hole is not up to date. Current version: {current_version}, New version: {new_version}')
        if pihole_question():
            print('Updating Pi-hole...')
            stdin, stdout, stderr = ssh.exec_command('pihole -up')
            for line in stdout: 
                print(line.strip())
    ssh.close()
    return current_version, new_version

if __name__ == '__main__':
    check_for_update()
