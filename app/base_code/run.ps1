$BASEDIR = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $BASEDIR

# apaga a pasta build, caso exista
Remove-Item -Path build -Recurse -Force -ErrorAction SilentlyContinue

# cria novamente a pasta
New-Item -ItemType Directory -Path build | Out-Null

# entra na pasta
Set-Location build

# https://cmake.org/cmake/help/latest/variable/CMAKE_BUILD_TYPE.html
#cmake .. -DCMAKE_C_COMPILER=gcc -DCMAKE_BUILD_TYPE=Release ../
cmake .. -DCMAKE_C_COMPILER=gcc -DCMAKE_BUILD_TYPE=Debug ../

# make clean all
make supervisor
./supervisor

if ($LASTEXITCODE -ne 0) {
    Write-Output "Erro na execução do programa!"
}
