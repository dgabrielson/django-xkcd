#######################
from __future__ import print_function, unicode_literals

#######################
from setuptools import find_packages, setup


def read_requirements(filename="requirements.txt"):
    return [ line.strip() for line in open(filename) if line and line[0] != '#' ]



setup(
    name='django-xkcd',
    version='0.4.0',
    author='Dave Gabrielson',
    author_email='Dave.Gabrielson@Gmail.Com',
    description='Django model and utils for archiving the xkcd comic',
    url="http://xkcd.com",
    license="GNU Lesser General Public License (LGPL) 3.0",
    packages=find_packages(exclude=['xkcd.demo_site']),
    install_requires=read_requirements(),
    zip_safe=False,
    include_package_data=True,
)
