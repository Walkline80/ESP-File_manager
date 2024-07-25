import gc
from micropython import alloc_emergency_exception_buf
from utilities import (
	connect_to_wifi,
)
from web_server import WebServer
import filemanager


alloc_emergency_exception_buf(128)
gc.collect()

# Start WWW serveru
webserver = WebServer(web_folder='/www', port=80)

#region Handlers for filemanager
@webserver.handle('/contents')
def _handle_contents(client, path, request):
	filemanager.handle_contents(client, path, request)

@webserver.handle('/upload')
def _handle_upload(client, path, request):
	filemanager.handle_upload(client, path, request)

@webserver.handle('/download')
def _handle_download(client, path, request):
	filemanager.handle_download(client, path, request)

@webserver.handle('/delete')
def _handle_delete(client, path, request):
	filemanager.handle_delete(client, path, request)

@webserver.handle('/rename')
def _handle_rename(client, path, request):
	filemanager.handle_rename(client, path, request)

@webserver.handle('/newfolder')
def _handle_newfolder(client, path, request):
	filemanager.handle_newfolder(client, path, request)

@webserver.handle('/move')
def _handle_move(client, path, request):
	filemanager.handle_move(client, path, request)

@webserver.handle('/copy')
def _handle_copy(client, path, request):
	filemanager.handle_copy(client, path, request)

@webserver.handle('/status')
def _handle_status(client, path, request):
	filemanager.handle_status(client, path, request)
#endregion

if connect_to_wifi():
	webserver.start()
	gc.collect()
