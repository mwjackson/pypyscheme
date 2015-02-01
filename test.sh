#!/bin/sh
echo 'python:'
python -m timeit -n 1000 -s'import main' 'main.test()'
echo 'pypy: '
pypy -m timeit -n 1000 -s'import main' 'main.test()'
