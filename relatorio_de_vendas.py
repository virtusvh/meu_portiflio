import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
import customtkinter as ctk
from tkinter import filedialog
import os
import platform


def gerador_de_relatorio(arquivo_csv):
    tabela = pd.read_csv(arquivo_csv)
    tabela['Total'] = tabela['Quantidade'] * tabela['Preço']

    totalv = tabela['Total'].sum()

    tabela['Data'] = pd.to_datetime(tabela['Data'], dayfirst=True)
    #tabela['Mês'] = tabela['Data'].dt.to_period('M')
    tabela.insert(1,'Mês',tabela['Data'].dt.to_period('M').dt.strftime('%m/%Y'))

    #quanto se produziu em cada mes
    producao_mensal = tabela.groupby('Mês')['Total'].sum()
    #produtos vendidos com suas quantidades e o total vendido(valores)
    produtos_vendidos = tabela.groupby('Produto').agg({'Quantidade': sum, 'Total':sum}).reset_index()
    #quantidade de produtos vendidos
    produtos_v = tabela.groupby('Produto')['Quantidade'].sum()
    #produto mais vendido (valor)
    total_max = tabela.groupby('Produto')['Total'].sum().max()

    #nome do produto mais vendido
    produtos_mais_v = produtos_v.idxmax()
    #maior quantidade vendidda daquele produto (produto_mais_v)
    qtd_max_v = produtos_v.max()

    #transformando tabela de volta em str
    tabela_png = tabela.copy()
    tabela_png['Data'] = tabela_png['Data'].dt.strftime('%d/%m/%Y')

    '''print(tabela_png)
    print(f'valor total de vendas: R${totalv:.2f}') #adicionar como legenda?
    print(10*'-')
    print(f'produção mensal:\n{producao_mensal}')
    print(10*'-')
    print(f'produtos vendidos:\n{produtos_vendidos}')
    print(10*'-')
    print(f'o produto mais vendido foi {produtos_mais_v}\nforam vendidas {qtd_max_v} unidades, dando um total de R${total_max},00 ') ##########!!!!!!!!!!############
    print(10*'-')'''

    #grafico de produtividade mensal
    producao_mensal.plot(kind='bar',color='black', rot=0)
    plt.title('vendas/mes')
    plt.ylabel('Total de vendas')
    plt.xlabel('Mês')
    plt.savefig('grafico de vendas.png')
    plt.close()

    def criar_tabela(variavel, nome):
        fig, ax = plt.subplots()
        ax.axis('tight')
        ax.axis('off')
        data_frame = variavel.reset_index()
        ax.table(cellText=data_frame.astype(str).values, colLabels=data_frame.columns, cellLoc='center',loc='center')
        plt.savefig(f'tabela_{nome}.png', dpi=300)
        plt.close()

    #tabela de produção mensal
    criar_tabela(producao_mensal, 'producao_mensal')

    #tabela completa (geral)
    criar_tabela(tabela,'geral')

    #gerar pdf
    nome_pdf = 'relatorio_de_vendas.pdf'
    doc = SimpleDocTemplate(nome_pdf, pagesize=A4)
    #criar o estilo dos textos das legendas
    estilo = ParagraphStyle(name="Legenda",fontName="Times-Roman", fontSize=12,)
    #estiloN = estilo['Normal']
    #adicionando as imagens e legendas
    elementos = [Image('grafico de vendas.png', width=500, height=260),
                 #Spacer(1,0.3),
                 Image('tabela_geral.png', width=500, height=360),
                 #Spacer(1,0.3),
                 Paragraph(f'o valor total de vendasfoi de R${totalv:.2f} e o produto mais vendido foi {produtos_mais_v}\n, foram vendidas {qtd_max_v} unidades, dando um total de R${total_max},00 ', estilo),
                 #Spacer(1,0.3),
                 Image('tabela_producao_mensal.png', width=500, height=360),
                 ]
    doc.build(elementos)

    def show_pdf(caminho):
        acessar = platform.system()
        if acessar == "Windows":
            os.startfile(caminho)
        elif acessar == "Darwin":
            os.system(f"open '{caminho}'")
        else:
            os.system(f"xdg-open '{caminho}'")
    show_pdf(nome_pdf)

def ler_csv():
    #diretorio_inicial = 'c:/"caminho ate o csv"'
    arquivo_csv = filedialog.askopenfilename(
    #initialdir=diretorio_inicial
    filetypes=[('tabela.CSV', '*.csv')]
)
    if arquivo_csv:
        gerador_de_relatorio(arquivo_csv)

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

janela = ctk.CTk()
janela.title('leitor de arquivo CSV')
janela.geometry('300x200')

botao = ctk.CTkButton(janela, text= 'selecionar CSV', command=ler_csv)
botao.pack(pady=80)

tela = ctk.CTkLabel(janela, )

janela.mainloop()
