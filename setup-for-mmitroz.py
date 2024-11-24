import sys
import os
import warnings
warnings.filterwarnings('ignore')
try:
    project_name = str(sys.argv[1])
except IndexError:
    print('Please enter the project name after setup.py')
    sys.exit(0)
try:
    os.mkdir(project_name)
except FileExistsError:
    print('Folder already exists!')
    sys.exit(0)
except:
    print("Unkown error.")
    sys.exit(0)

mmitroz_functions = open(f'./{project_name}/mmitroz_functions.py','w')
mmitroz_functions.write("""import mmitroz_variables

def get_header_method(request):
    method = request[:request.find(' ')]
    header = request[request.find('/'):request.find(' H')]
    return (method, header)

def check_send_requested(request,client):
    method,requested_file = get_header_method(request)
    if requested_file in mmitroz_variables.files.keys():
        file = open(f'{mmitroz_variables.files.get(requested_file)[0]}','r')
        content = file.read()
        file.close()
        client.sendall((f'''HTTP/1.1 200 OK\nContent-Type: {mmitroz_variables.files.get(requested_file)[1]}\n\n'''+content).encode())
    else :
        file = open(f'{mmitroz_variables.notfound}','r')
        content = file.read()
        file.close()
        client.sendall(('''HTTP/1.1 404 Not Found\n\n'''+content).encode())

def accept_client(server):
    while True:
        client, address = server.accept()
        request = client.recv(1024).decode()
        check_send_requested(request,client)
        client.close()""")
mmitroz_functions.close()
mmitroz_main=open(f'./{project_name}/mmitroz_main.py','w')
mmitroz_main.write("""import socket
import os
import threading
import mmitroz_functions as func
import mmitroz_variables as vars
os.system('color')
green = '\033[32m'
red = '\033[31m'
yellow = '\033[33m'
reset = '\033[0m'

def main():
    print(f'''{green}
    ___  ___ ___  ___  _____   _____  ______   _____   ______
    |  \/  | |  \/  | |_   _| |_   _| | ___ \ |  _  | |___  /
    | .  . | | .  . |   | |     | |   | |_/ / | | | |    / / 
    | |\/| | | |\/| |   | |     | |   |    /  | | | |   / /  
    | |  | | | |  | |  _| |_    | |   | |\ \  \ \_/ / ./ /___
    \_|  |_/ \_|  |_/  \___/    \_/   \_| \_|  \___/  \_____/
                                                         
                                                         {reset}''')
    print(f'MMitroz pyhton server, by {red}pyXploit{reset} on github {yellow}http://github.com/pyXploit{reset}')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :
        server.bind(vars.iport)
    except :
        server.bind(('127.0.0.1',80))
        print('iport is not set in mmitroz_variables.py. Using 127.0.0.1:80 as default')
    try :
        server.listen(vars.maxclients)
    except :
        server.listen(5)
        print('maxclients is not set in mmitroz_variables.py. Using 5 as default')
    accept_client = threading.Thread(target=func.accept_client, args=(server,))
    accept_client.daemon = True
    accept_client.start()
    try :
        while True:
            pass
    except KeyboardInterrupt:
        print('Server stopped')
    else :
        print('Unknown Error')

if __name__ == '__main__':
    main()

    """)
mmitroz_variables = open(f'./{project_name}/mmitroz_variables.py','w')
mmitroz_variables.write('''# This is the main directory
main_dir = './app'
# This is for not found page
notfound=f'{main_dir}/404.html'
# This is for ip and port
iport = ('127.0.0.1',80)
# This is for the max clients of course
maxclients = 5
# This is the dictionary containing the requests as keys and the dirs and types of dirs as values
files = {'/' : (f'{main_dir}/index.html','text/html'),
         }''')
mmitroz_variables.close()
os.mkdir(f'./{project_name}/app')
index = open(f'./{project_name}/app/index.html', 'w')
index.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project in mmitroz</title>
</head>
<body>
    <p>MMitroz Start page</p>
</body>
</html>''')
index.close()
index404 = open(f'./{project_name}/app/404.html','w')
index404.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Not found!</title>
</head>
<body>
    <p>404 Not found!</p>
</body>
</html>''')
index404.close()
licen = open(f'./{project_name}/LICENSE', 'w')
licen.write("""Copyright (c) 2024 pyXploit

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.""")
licen.close()
print(f'MMitroz server {project_name} created succefully.')
