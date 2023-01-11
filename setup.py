import os
import setuptools
from distutils.command.sdist import sdist as sdist_orig
from distutils.errors import DistutilsExecError


with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                       'README.md')) as f:
    long_description = f.read()


class sdist(sdist_orig):
    """
    runs a simple shell script to setup everything
    """
    def run(self):
        try:
            self.spawn(['./setup.sh'])
        except DistutilsExecError:
            self.warn('failed to run the setup script')
        super().run()


setuptools.setup(
    name='python_x64_parser',
    version='0.0.1',
    author='Floyd Zweydinger',
    author_email='floyd.zweydinger',
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
    # entry_points={
    #     'console_scripts': [
    #         'python_x64_parser=src.python_x64_parser:cli',
    #     ],
    # },
)
