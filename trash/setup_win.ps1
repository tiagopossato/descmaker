Write-Host "Criando ambiente virtual..."

python -m venv env

Write-Host "Ativando ambiente virtual..."

.\env\Scripts\Activate.ps1

Write-Host "Instalando dependências..."

pip install -r .\requirements.txt

Write-Host "Script concluído."
