Installation
============

Automatic:
----------
```bash
pip install python_x64_parser
```

Manual:
------
```
git clone --recursive https://github.com/FloydZ/python_x64_parser
cd python_x64_parser/nasm
make
```

The `make` command generates the needed python files from the antlr model.

TODO:
====

- nasm parser currently not fully correct.
- add more asm syntax (see antlr repo)
- add converter scripts between them
