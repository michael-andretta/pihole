### Import Libraries ###
import os
import sys
import time
import paramiko

### Import Secret ###
from env_vars.secrets import ph_user, ph_pass, ph_ip

### Define Functions ###
def pihole_connect():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ph_ip, username=ph_user, password=ph_pass)
    return ssh

def check_pihole_status():
    ssh = pihole_connect()
    stdin, stdout, stderr = ssh.exec_command('pihole status')
    status = stdout.read().decode('utf-8').strip()
    ssh.close()
    return status

def check_version():
    ssh = pihole_connect()
    stdin, stdout, stderr = ssh.exec_command('pihole -v')
    version = stdout.read().decode('utf-8').strip()
    ssh.close()
    return version

def pihole_command(command):
    ssh = pihole_connect()
    stdin, stdout, stderr = ssh.exec_command(command)
    status = stdout.read().decode('utf-8').strip()
    ssh.close()
    return status

### Main Function ###
if __name__ == '__main__':
    status = pihole_command('pihole status')
    print(status)
    sys.exit(0)
