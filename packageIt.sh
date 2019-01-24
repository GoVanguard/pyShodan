#!/bin/bash
rm -Rf dist/
rm -Rf build/
rm -Rf pydradis3.egg-info/
python3 setup.py sdist bdist_wheel
