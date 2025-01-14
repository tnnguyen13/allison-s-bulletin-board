from setuptools import find_packages, setup
from flask import Flask
import os

app = Flask(__name__)

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

"""
contain) to include. find_packages() finds these directories 
automatically so you don’t have to type them out. To include other 
files, such as the static and templates directories, 
include_package_data is set. Python needs another file named MANIFEST.in
to tell what this other data is.
"""