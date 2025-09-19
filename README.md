Aula 04 - POO - 19/09/2025


## Atividade

Você deve desenvolver uma aplicação em Python (modo terminal) para coletar métricas básicas do sistema onde o programa está sendo executado.

O objetivo é aplicar herança, polimorfismo e orientação a objetos em um contexto próximo ao mundo real (DevOps).

Requisitos:

1. Criar uma classe Metrica que define a estrutura de uma métrica do sistema.

2. Essa classe Metrica deve ter, pelo menos, os atributos `unidade` e `valor`, que serão implementados pelas classes filhas.

3. Criar subclasses que representam métricas específicas, por exemplo:

    CpuMetrica → retorna o uso da CPU em porcentagem.

    MemoriaMetrica → retorna o uso de memória em MB.

    DiscoMetrica → retorna o espaço livre em disco.

4. A aplicação deve coletar os valores das métricas e salvar a saída em um arquivo CSV com o seguinte formato:

        datetime,metrica,valor,unidade
        2025-09-19 15:30:01,CPU,12.4,%
        2025-09-19 15:30:01,Memoria,2048,MB
        2025-09-19 15:30:01,Disco,50234,MB

5. Desafios Extras
    a) permitir que o programa colete métricas periodicamente (loop), por exemplo, coletar métricas a cada 5 segundos durante 10 iterações

    b) aceitar parâmetros via terminal para escolher executar métricas individualmente, mudar o intervalo de tempo entre coletas ou o nome do arquivo de saída


Dicas:

### biblioteca útil para coletar métricas do sistema
    
```python
    import psutil  

    # informações da memória
        psutil.virtual_memory() 
    
    # informações do disco
        psutil.disk_usage('/')
        psutil.disk_usage.free
    
    # informações de CPU
    psutil.cpu_percent(interval=1)
    

```

### biblioteca para criar, ler e modificar arquivos .csv
```python
    import csv
```

### exemplo para pegar a data e hora atual do sistema
```python
    from datetime import datetime
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```
