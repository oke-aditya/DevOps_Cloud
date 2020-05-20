# How to publish a package to pypi

create the folder structure as mentioned

----> src
----> setup.py
	      -------> __init__.py
		  -------> file1.py
		  -------> file2.py
		  -------> license.txt
		  -------> README.md
		  -------> setup.cfg

Demo is shown from this folder. It has setup.py for the src directory which is bnog_distributions here.

# File info Setup.py

- Setup.py should contain how to setup your package
- Give it a name, version, description and packages to include.

E.g.

from setuptools import setup

setup(name='bnog_distributions',
      version='0.1',
      description='Gaussian distributions',
      packages=['bnog_distributions'],
      zip_safe=False)

# File info license.txt

- Use any license such as MIT license etc. These are available on github.

# File info README.md

- README.md contains markdown file that will describe the package.

# File info setup.cfg

- It's a simple file it has standard template which you can find.

E.g.

[metadata]
"#" This includes the license file(s) in the wheel. (put the hash properly)
license_files = license.txt

# Create an account

- for test packages on pypi test website and for other packages on pypi.org

# How to build and upload the package ?
- Install Twine

pip install twine

- Open terminal reach till setup.py directory

python setup.py sdist

- commands to upload to the pypi test repository and install from it

twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/simple/ <package-name>

- command to upload to the pypi repository and install from it
twine upload dist/*
pip install <package-name>


