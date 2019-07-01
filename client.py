import ftplib

host = input('host: ')
user = input('user: ')
password = input('password: ')

print(user, password)
client = ftplib.FTP(host)
client.login(user, password)
print(client.pwd())
client.dir()