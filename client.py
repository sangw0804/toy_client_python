import ftplib

host = input('host: ')
user = input('user: ')
password = input('password: ')

client = ftplib.FTP(host, user, password)

print(f'successfully log in at {host} as {user}')
while True:
  try:
    cmd = input('').split()

    if cmd[0] == 'exit':
      client.quit()
      break
    elif cmd[0] == 'ls':
      client.dir()
    elif cmd[0] == 'pwd':
      print(client.pwd())
    elif cmd[0] == 'cd':
      print(client.cwd(cmd[1]))
    elif cmd[0] == 'mkdir':
      print(client.mkd(cmd[1]))
    elif cmd[0] == 'rm':
      print(client.rmd(cmd[1]))
    elif cmd[0] == 'send':
      print(client.storbinary(f'STOR {cmd[1]}', open(cmd[1], 'rb')))
    elif cmd[0] == 'get':
      with open(cmd[1], 'wb') as f:
        print(client.retrbinary(f'RETR {cmd[1]}', f.write))
    else:
      print('Invalid command!!!')
  except Exception as E:
    print(E)