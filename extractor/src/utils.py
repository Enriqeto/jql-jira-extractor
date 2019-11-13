from yaml import safe_load

def config():
	with open('../config.yaml', 'r', encoding='utf-8') as cfile:
		return safe_load(cfile.read())