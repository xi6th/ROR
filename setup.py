from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in customregistration/__init__.py
from customregistration import __version__ as version

setup(
	name="customregistration",
	version=version,
	description="Custom event config",
	author="ejise45@gmail.com",
	author_email="ejise45@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
