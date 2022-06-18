from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in food_prep/__init__.py
from food_prep import __version__ as version

setup(
	name="food_prep",
	version=version,
	description="A site for prepping for food a week in advance",
	author="Abdulrehman Muhammad Younis",
	author_email="abadulrehman@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
