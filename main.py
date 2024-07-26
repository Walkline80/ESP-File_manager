import gc
from micropython import alloc_emergency_exception_buf
from utilities import connect_to_wifi
from web_server import WebServer
from web_handler import *


__version__ = '0.0.2'
module_folder = ''

try:
	module_folder = __file__.rsplit('/', 1)[0]

	if module_folder == __file__:
		module_folder = ''
except NameError:
	pass


alloc_emergency_exception_buf(128)
gc.collect()

# Start WWW serveru
webserver = WebServer(web_folder=f'/{module_folder}/www', port=80)

#region Handlers for web_handlers
@webserver.handle('/contents')
def _handle_contents(client, path, request):
	handle_contents(client, path, request)

@webserver.handle('/upload')
def _handle_upload(client, path, request):
	handle_upload(client, path, request)

@webserver.handle('/download')
def _handle_download(client, path, request):
	handle_download(client, path, request)

@webserver.handle('/delete')
def _handle_delete(client, path, request):
	handle_delete(client, path, request)

@webserver.handle('/rename')
def _handle_rename(client, path, request):
	handle_rename(client, path, request)

@webserver.handle('/newfolder')
def _handle_newfolder(client, path, request):
	handle_newfolder(client, path, request)

@webserver.handle('/move')
def _handle_move(client, path, request):
	handle_move(client, path, request)

@webserver.handle('/copy')
def _handle_copy(client, path, request):
	handle_copy(client, path, request)

@webserver.handle('/status')
def _handle_status(client, path, request):
	handle_status(client, path, request)
#endregion

if connect_to_wifi():
	webserver.start()
	gc.collect()
