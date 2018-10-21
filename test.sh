#!/bin/bash
# Script que corre las pruebas del proyecto
find . -path ./env -prune -o \
    -path "*migrations*" -prune -o \
    -name "*.py" -exec pylint {} + || exit 1

# corremos las pruebas
python manage.py test || exit 1
exit 0