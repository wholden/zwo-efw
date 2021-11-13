from setuptools import setup, find_packages

setup(
	name='zwo_efw',
	version='1.0',
	author='William Holden',
	description=('Python bindings for controlling the ZWO electronic filter wheel (EFW).'),
	packages=find_packages(),
	include_package_data=True,
	zip_safe=True,
	)