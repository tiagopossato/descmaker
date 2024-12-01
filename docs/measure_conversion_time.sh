#!/bin/sh

# Verifica se o arquivo de entrada foi fornecido
if [ -z "$1" ]; then
  echo "Uso: $0 <caminho_para_o_arquivo_de_entrada>"
  exit 1
fi

input_file=$1

# Função para capturar o tempo de execução em milissegundos
measure_time() {
  start_time=$(date +%s%3N)
  python3 descmaker.py -l python -i "$input_file" > /dev/null 2>&1
  end_time=$(date +%s%3N)
  exec_time=$((end_time - start_time))
  echo $exec_time
}

# Variável para armazenar o tempo total em milissegundos
total_time_ms=0

# Loop para executar o comando 10 vezes
for i in 1 2 3 4 5 6 7 8 9 10
do
  rm -rf generated_code
  # Captura o tempo de execução usando a função measure_time
  exec_time=$(measure_time)
  
  # Adiciona o tempo total em milissegundos
  total_time_ms=$((total_time_ms + exec_time))
done

# Calcula o tempo médio em milissegundos
average_time_ms=$((total_time_ms / 10))

# Exibe o tempo médio em milissegundos
echo "Tempo médio de execução: $average_time_ms milissegundos"