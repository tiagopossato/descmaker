#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
cd "$BASEDIR"

# apaga a pasta build, caso exista
rm -rf build

# cria novamente a pasta
mkdir -p build

# entra na pasta
cd build
# https://cmake.org/cmake/help/latest/variable/CMAKE_BUILD_TYPE.html
#cmake .. -DCMAKE_C_COMPILER=gcc -DCMAKE_BUILD_TYPE=Release ../
cmake cmake .. -DCMAKE_C_COMPILER=gcc -DCMAKE_BUILD_TYPE=Debug ../
# make clean all
make supervisor
./supervisor

if [ ! $? -eq 0 ]; then
    echo "Erro na execução do programa!"
fi