# Development

## Installing for Development

To install the program in such a way that it is still editable from the source
tree, run the following from the repo's base directory:

```
pip install --editable .
```

For more information, refer to
[Installing Packages](https://packaging.python.org/tutorials/installing-packages/).

## Uploading to PyPI

First, make sure all of the required tools are installed and up-to-date:

```
python -m pip install --user --upgrade setuptools wheel twine
```

Then build and upload the artifacts by running these commands from the repo's
base directory:

```
python setup.py sdist bdist_wheel
python -m twine upload dist/*
```

For more information, refer to
[Packaging Projects](https://packaging.python.org/tutorials/packaging-projects/).
