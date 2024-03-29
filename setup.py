from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in qcs_invoice_advance/__init__.py
from qcs_invoice_advance import __version__ as version

setup(
	name="qcs_invoice_advance",
	version=version,
	description="QCS Invoice Advance",
	author="Quark Cyber Systems FZC",
	author_email="support@quarkcs.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
