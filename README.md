# MMITROZ
Mmitroz is a python based server to host a web sever using socket library.
## Installation
Via git :
```bash
git clone github.com/pyXploit/mmitroz
cd mmitroz
python -W "ignore" setup-for-mmitroz.py <server_name>
```
Python 3.8 or up is required.
## Important notes
This project is still in development and not ready to be used.

Run the server by :
```bash
python mmitroz_main.py
```

To add your page, stylesheet, image etc ...
```python
# In mmitroz_variables.py
files = {'/' : (f'{main_dir}/index.html','text/html'),
         }
# First type the url used to access the file as key, and create a tuple containing at index 0 the dir and at index one the MIME type(text/html, text/css, etc ...) as value.

# Choose the ip and port 
iport = ('127.0.0.1',80) # Defaults
# Choose max clients
maxclients = 5 # Default

# And make sure to put all your files in a sub folder so you don't get security issues
```
## License
This project is under MIT license, check LICENSE file.
