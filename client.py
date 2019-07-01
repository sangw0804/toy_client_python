import ftplib

host = input('host: ')
user = input('user: ')
password = input('password: ')

client = ftplib.FTP(host, user, password)

print(f'successfully log in at {host} as {user}')
while True:
  cmd = input('')

  if cmd == 'exit':
    client.quit()
    break
  elif cmd == 'ls':
    client.dir()
  elif cmd == 'pwd':
    print(client.pwd())
  elif cmd[:2] == 'cd':
    print(client.cwd(cmd[3:]))
  elif cmd[:5] == 'mkdir':
    print(client.mkd(cmd[6:]))
  else:
    print('Invalid command!!!')