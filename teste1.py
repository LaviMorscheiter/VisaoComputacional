import torch

matriz_maior = torch.full((5,5),2)

matriz_maior [0][2]= 9
matriz_maior [2][1]= 5

print (matriz_maior)

matriz_menor = torch.ones(3,3)
print(matriz_menor)

matriz_resultado = torch.zeros(matriz_maior.size(0)-2, matriz_maior.size(1)-2)

for iM in range(1, matriz_maior.size(0)-1):
    for jM in range(1,matriz_maior.size(1)-1):
        print ('Pixel atual: ',iM, jM)
        
        recorte = matriz_maior[iM-1:iM+2, jM-1:jM+2]
        print('Recorte: \n', recorte)
        
        resultado = recorte * matriz_menor
        print('Resultado: \n', resultado)
        
        soma = resultado.sum()
        print('Soma: ', soma)
        
        matriz_resultado[iM-1, jM-1] = soma
        print (matriz_resultado)
        
        input('Pressione Enter para continuar...')
        
print('Matriz Resultado: \n', matriz_resultado)