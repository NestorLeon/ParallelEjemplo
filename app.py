import parallel

@parallel.decorate
def imprimir_numeros(max, nombre):
    suma = 0
    for n in range(1, max):
        suma += n
        print(nombre + " imprime " + str(n))
    return suma

def imprimir_resultados(valor):
    print('RESULTADO: ' + str(valor))

numeros = [
    (500, 'Arturo'),
    (700, 'Bebe'),
    (1000, 'Felipe')]

results = imprimir_numeros.map(numeros, timeout=5, max_workers=4)

'''
results = parallel.map(
    imprimir_numeros,  # the function to invoke
    numeros,                # parameters to parallelize
    timeout=5,           # timeout per thread
    max_workers=4        # max threads
)
'''

map(imprimir_resultados, results)