import cv2
import torch
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def convolucao(matriz_maior, matriz_menor):
    matriz_resultado = torch.zeros(matriz_maior.size(0)-2, matriz_maior.size(1)-2)
    for iM in range(1, matriz_maior.size(0)-1):
        for jM in range(1, matriz_maior.size(1)-1):
            recorte = matriz_maior[iM-1:iM+2, jM-1:jM+2]
            resultado = recorte * matriz_menor
            soma = resultado.sum()
            matriz_resultado[iM-1, jM-1] = soma
    return matriz_resultado

def le_matriz_entry():
    arquivo = entry_matriz.get()
    with open(arquivo, 'r') as f:
        matriz = []
        for linha in f:
            matriz.append([float(x) for x in linha.split()])
        matriz_tensor = torch.tensor(matriz)
        
    # Limpa a tabela
    for i in tabela.get_children():
        tabela.delete(i)
        
    # Adiciona a matriz à tabela
    for i, linha in enumerate(matriz_tensor.tolist()):
        tabela.insert('', 'end', text="Linha"+str(i), values=linha)
        
    return matriz_tensor

def le_imagem():
    imagem= cv2.imread(arquivo, cv2.IMREAD_GRAYSCALE)
    return torch.tensor(imagem)

def criar_interface():
    root = tk.Tk()
    root.title("Convolução")
    root.geometry("400x200")

    label_matriz = tk.Label(root, text="Digite o nome do arquivo da matriz: ")
    label_matriz.pack()

    # Entry para o usuário digitar o nome do arquivo
    entry_matriz = tk.Entry(root)
    entry_matriz.pack()

    # Botão para ler a matriz
    botao = tk.Button(root, text="Ler matriz", command=le_matriz_entry)
    botao.pack()

    # Tabela para exibir a matriz lida
    global tabela
    tabela = ttk.Treeview(root)
    tabela.pack()
    
    #nome para ler a imagem
    label_imagem = tk.Label(root, text="Digite o nome do arquivo da imagem: ")
    label_imagem.pack()
    entry_imagem = tk.Entry(root)
    entry_imagem.pack()
    
    #
    
    root.mainloop()

criar_interface()
