import time

inicio = time.time()

for i in range(1, 1_000_000):
    pass 
fim = time.time()
tempo_execucao = fim - inicio
print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
