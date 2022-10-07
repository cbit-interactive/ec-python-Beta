import smtplib
import socket

host = input("What is your IP: ")
port = 25
local_hostname = socket.gethostname()

print("""
[[[[[[[[[[  [[[[[[[
[[[[        [[[
[[[[        [[[
[[[[[[[     [[[
[[[[        [[[
[[[[        [[[
[[[[[[[[[[  [[[[[[[

Enter a bug that is found and we will try to fix it. You can also go to our Github page.
""")

from_addr = 'bugtracking_ec.iiab@outlook.com'
to_addrs = 'forestriaeon.gov@gmail.com'
msg = input("Enter problem: ")

smtp_obj = smtplib.SMTP(host, port, local_hostname)
smtplib.SMTP.sendmail(from_addr, to_addrs, msg)
