"""
Copyright © 2024 Walkline Wang (https://walkline.wang)
Gitee: https://github.com/Walkline80/ESP-File_manager
Forked: https://github.com/mispacek/ESP-File_manager
"""
import gc
from micropython import alloc_emergency_exception_buf

module_folder = ''
__version__ = '0.0.3'

try:
	from utilities import connect_to_wifi
	from web_server import WebServer
	from web_handler import *
except ImportError:
	from .utilities import connect_to_wifi
	from .web_server import WebServer
	from .web_handler import *

	module_folder = 'filemanager'


alloc_emergency_exception_buf(128)
gc.collect()

# Start WWW serveru
webserver = WebServer(web_folder=f'/{module_folder}/www', port=8080)

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

@webserver.handle('/reboot')
def _handle_reboot(client, path, request):
	handle_reboot(client, path, request)
#endregion

if connect_to_wifi():
	webserver.start()
	gc.collect()
