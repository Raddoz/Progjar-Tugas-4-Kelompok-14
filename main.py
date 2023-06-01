import smtplib
import sys
import os

log_file_path = "debug.log"
log_file = open(log_file_path, 'w')
original_stderr = sys.stderr
sys.stderr = log_file

mailserver = smtplib.SMTP('smtp.office365.com',587)
mailserver.set_debuglevel(1)
mailserver.ehlo()
mailserver.starttls()
mailserver.login('email@mhs.its.ac.id', '')
mailserver.sendmail('email@mhs.its.ac.id','email@gmail.com','\nemail body')

mailserver.quit()