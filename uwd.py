from pathlib    import Path
from string     import ascii_letters, digits
from random     import choice
from os         import system, name

from time       import sleep

from requests   import get

script_version  = '1.0'
script_title    = 'unsplash WP Downloader by ALIILAPRO (version {})'.format(script_version)

def start_script():
	system('title ' + script_title if name == 'nt' else 'PS1="\[\e]0;' + script_title + '\a\]"; echo $PS1')
	system('cls' if name == 'nt' else 'clear')
	print (f'''
	 ..: {script_title} :..
 
 [!] ABOUT SCRIPT:
 [-] With this script, you can download wallpaper from site unsplash.com
 [-] Version: {script_version}
 --------
 [!] ABOUT CODER:
 [-] ALIILAPRO, Programmer and developer from IRAN.
 [-] Website  : aliilapro.github.io
 [-] Telegram : aliilapro
 --------
''')

def genString(stringLength):
	letters = ascii_letters + digits

	return ''.join(choice(letters) for i in range(stringLength))

def req(url):
	try:
		r = get(url)
	except:
		r = get(url)

	return r

def download():
	try:
		start_script()
		DOWNLOAD_FOLDER = './wp'
		FILE_NAME       = 'unsplash-{}.jpg'.format(genString(7))
		FILE_PATH       = '{}/{}'.format(DOWNLOAD_FOLDER,FILE_NAME)
		BASE_URL        = 'https://source.unsplash.com'
		RES_URL         = '1920x1080'
		KEYWORDS        = ['HD Wallpapers', 'Experimental', 'hope', 'travel', 'dark']
		URL             = '{}/{}/?{}'.format(BASE_URL, RES_URL, choice(KEYWORDS))
		Path(DOWNLOAD_FOLDER).mkdir(parents=True, exist_ok=True)
		print("[+] Start downloading...")
		img_data = req(URL).content
		with open(FILE_PATH, 'wb') as handler:
			handler.write(img_data)
		print("[+] Wallpaper [{}] successfully downloaded.".format(FILE_NAME))
		sleep(5)
	except Exception as error:
		print(error)
		sleep(5)

def run():
	while True:
		start_script()
		user_input = input("[?] Do you want to download a new wallpaper? (y/n):")
		if user_input == "y":
			download()
		elif user_input == "n":
			break
		else:
			print("[!] Error: {} is not a valid parameter.".format(user_input))
			sleep(3)

run()