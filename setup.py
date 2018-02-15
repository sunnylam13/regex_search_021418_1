try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Regex program that searches text files in a folder for a user supplied regular expression.',
	'author': 'Sunny Lam',
	'url': 'URL to get it at',
	'download_url': 'Where to download it',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['re'],
	'scripts': [],
	'name': 'Regex Search'
}

setup(**config)