# Test Case

## ESP32 with PlatformIO

To use with PlatformIO, comment the main function in `main.c` and rename `main.c` to `main.cpp`. 


Para compilar e excutar use: `./run.sh`

# uso

- Instanciar os eventos no arquivo `events.h`

- Para cada supervisor
    - Criar um arquivo '.h' com o nome do supervisor

    - Instanciar o alfabeto do supervisor, composto pelos eventos pertencentes somente àquele supervisor
        - O nome das variáveis de eventos do alfabeto do supervisor deve ser composto pelo nome do supervisor + '_evt' + número sequencial iniciando em 0
            - Exemplo de nome de variável de evento do alfabeto do supervisor: `supervisor_evt0`
        - O último alphabeto instanciado possui `next = NULL`
        - O primeiro alfabeto instanciado deverá ser passado como parâmetro para a função `supervisor_init`
    - Instanciar os estados
    - Instanciar as transições
        - O nome das transições deve ser composto pelo nome do estado de origem + '_t' + número sequencial iniciando em 0
            - Exemplo de nome de transição para o estado q0: `q0_t0`
            - Por convenção, a transição '_t0' deve ser a primeira transição da lista de transições do estado

        - Instanciar o supervisor