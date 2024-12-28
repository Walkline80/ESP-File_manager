"""
Copyright © 2024 Walkline Wang (https://walkline.wang)
Gitee: https://github.com/Walkline80/ESP-File_manager
Forked: https://github.com/mispacek/ESP-File_manager
"""
import os
import network
from time import sleep_ms


def file_path_exists(path: str) -> bool:
	try:
		os.stat(path)
		return True
	except OSError:
		return False

def is_directory(path: str) -> bool:
	try:
		return os.stat(path)[0] & 0x4000 != 0
	except OSError:
		return False

def read_in_chunks(file_object, chunk_size: int = 1024):
	while True:
		data = file_object.read(chunk_size)

		if not data:
			break

		yield data

def convert_file_size(size: int) -> str:
	units = 'Bytes', 'KB', 'MB', 'GB', 'TB'
	unit = units[0]

	for i in range(1, len(units)):
		if size >= 1024:
			size /= 1024
			unit = units[i]
		else:
			break

	return f'{size:.2f} {unit}'

def connect_to_wifi() -> bool:
	sta = network.WLAN(network.STA_IF)
	sta.active(True)

	if sta.isconnected():
		return True

	wifi_list = sta.scan()

	print('Wifi List:')
	for index, wifi in enumerate(wifi_list, start=1):
		print(f'    [{index}] {wifi[0].decode()}')

	selected = None
	while True:
		try:
			selected = int(input('Choose a wifi to connect: '))
			assert isinstance(selected, int) and 0 < selected <= len(wifi_list)
			break
		except KeyboardInterrupt:
			return False
		except:
			pass

	ssid = wifi_list[selected - 1][0].decode()
	password = input(f'Input password for {ssid}: ')

	sta.connect(ssid, password)

	while (not sta.isconnected()):
		status = sta.status()

		if status in [network.STAT_IDLE, network.STAT_GOT_IP, network.STAT_NO_AP_FOUND, network.STAT_WRONG_PASSWORD]:
			break
		elif status == network.STAT_CONNECTING:
			pass

		sleep_ms(200)

	sleep_ms(1000)
	status = sta.status()

	if status == network.STAT_GOT_IP:
		print("Wifi connected, network config:", sta.ifconfig())
		return True
	else:
		print(f'Connect wifi failed with status code: {status}')
		return False
