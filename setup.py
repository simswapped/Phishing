# <3 - shark

# Setup for PYMultiTor v6.9

import re
from os import path
from setuptools import setup, find_packages

__folder__ = path.dirname(__file__)

with open(path.join(__folder__, 'README.md')) as ld_file:
    long_description = ld_file.read()
    ld_file.flush()

with open(path.join(__folder__, 'pymultitor.py')) as lib_file:
    r = re.search(r'__version__\s+=\s+(?P<q>["\'])(?P<ver>\d+(?:\.\d+)*)(?P=q)', lib_file.read())
    version = r.group('ver')

with open(path.join(__folder__, 'requirements.txt')) as req_file:
    install_requires = req_file.read()

setup(
    name='PyMultiTor',
    version=version,
    description='PyMultiTor - Never Stop Even If Your IP Dropped.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Shark',
    author_email='cupid@*****.c***',
    packages=find_packages(exclude=['examples', 'tests']),
    py_modules=['pymultitor'],
    entry_points={
        'console_scripts': [
            'pymultitor = pymultitor:main',
        ]
    },
    install_requires=install_requires,
    license="SMDv6.9",
    platforms='ALL',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: Proxy Servers',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

