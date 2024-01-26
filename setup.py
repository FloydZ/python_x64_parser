import os
import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                       'README.md')) as f:
    long_description = f.read()

def custom_command():
    import sys
    if sys.platform in ['linux']:
        os.system('./build.sh')


class CustomInstallCommand(install):
    def run(self):
        custom_command()
        install.run(self)


class CustomDevelopCommand(develop):
    def run(self):
        custom_command()
        develop.run(self)


class CustomEggInfoCommand(egg_info):
    def run(self):
        custom_command()
        egg_info.run(self)


setuptools.setup(
    name='python_x64_parser',
    version='0.0.1',
    author='Floyd Zweydinger',
    author_email='zweydfg8@rub.de',
    description=('A utility for performing basic text transformations.'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    cmdclass={
        'sdist': sdist
    },
    project_urls={
        'Source Code': 'https://github.com/FloydZ/python_x64_parser',
        "Author's Website": 'https://pingfloyd.de',
        'Documentation': '',
    },
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 1 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Utilities',
    ],
    packages=[
        'src',
    ],
)
