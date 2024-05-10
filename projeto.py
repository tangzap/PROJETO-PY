from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from tkcalendar import Calendar, DateEntry
from datetime import date

from view import bar_valores, inserir_categoria, inserir_receitas, inserir_gastos





co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"  
co6 = "#038cfc"   
co7 = "#3fbfb9"   
co8 = "#263238"  
co9 = "#e9edf5"   

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

janela = Tk()
janela.title()
janela.geometry('900x650')
janela.configure(background=co1)
janela.resizable(width=FALSE,height=FALSE)

style= ttk.Style(janela)
style.theme_use("clam")
frameCima = Frame(janela,width=1043,height=50, bg= co1, relief="flat")
frameCima.grid(row=0,column=0)

frameMeio = Frame(janela,width=1043,height=361, bg= co1, pady=20, relief="raised")
frameMeio.grid(row=1,column=0, pady=1,padx=0,sticky=NSEW)

frameBaixo = Frame(janela,width=1043,height=300, bg= co0, relief="flat")
frameBaixo.grid(row=2,column=0, pady=0,padx=10,sticky=NSEW)

frame_gra_pie = Frame(frameMeio,width=580, height=250, background=co2)
frame_gra_pie.place(x=415, y=5)


app_logo = Label(frameCima, text=" Gestor Financeiro Pessoal",width=900,compound= LEFT, padx=5,relief=RAISED,anchor=NW,font=('Verdana 20 bold'),bg=co1,fg=co4)
app_logo.place(x=0,y=0)


global tree
def inserir_categoria_b():
   nome = e_categoria.get()

   lista_inserir = [nome]

   for i in lista_inserir:
      if i=='':
         Messagebox.showerror('Erro', 'Preencha todos os campos')
         return
    
inserir_categoria(lista_inserir)
messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
e_categoria.delete(0,'end')

      
      

def porcentagem():
  l_nome = Label(frameMeio, text="Porcentagem de Receita Gasta", height=1,anchor=NW,font=('Verdana 12'), bg=co1, fg=co4)
  l_nome.place(x=7,y=5)
  style = ttk.Style()
  style.theme_use('default')
  style.configure("black.Horizontal.TProgressbar", background='#daed6b')
  style.configure("TProgressBar",thickness=25)

  bar = Progressbar(frameMeio,length=180,style='black.Horizontal.TProgressbar')

  bar.place(x=10, y=35)
  bar['value'] = 50
  
  valor = 50
  l_porcentagem = Label(frameMeio, text="{:,.2f}%".format(valor),anchor=NW,font=('Verdana 12'), bg=co1, fg=co4)
  l_porcentagem.place(x=200,y=35)


def grafico_bar():
  lista_categorias = ['Renda','Despesas','Saldo']
  lista_valores = [3253, 2000, 5241]

  figura = plt.Figure(figsize=(4, 3.45), dpi=60)
  ax = figura.add_subplot(111)
  ax.autoscale(enable=True, axis='both', tight=None)

  ax.bar(lista_categorias,lista_valores, color=colors, width=0.9)

  c = 0
  for i in ax.patches:
      ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
  c += 1

  ax.set_xticklabels(lista_categorias,fontsize=16)
  ax.patch.set_facecolor('#ffffff')
  ax.spines['bottom'].set_color('#CCCCCC')
  ax.spines['bottom'].set_linewidth(1)
  ax.spines['right'].set_linewidth(0)
  ax.spines['left'].set_color('#CCCCCC')
  ax.spines['left'].set_linewidth(1)

  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  ax.spines['left'].set_visible(False)
  ax.tick_params(bottom=False, left=False)
  ax.set_axisbelow(True)
  ax.yaxis.grid(False, color='#EEEEEE')
  ax.xaxis.grid(False)

  canva = FigureCanvasTkAgg(figura, frameMeio)
  canva.get_tk_widget().place(x=10, y=70)








def resumo ():
  valor = [500,600,420]

  l_linha = Label(frameMeio,text="",width=215,height=1, anchor=NW, font=('Arial 1'), bg='#545454')
  l_linha.place(x=309,y=52)

  l_sumario = Label(frameMeio,text="Total Renda Mensal      ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
  l_sumario.place(x=309,y=35)

  l_sumario = Label(frameMeio,text="R$ {:,.2f}".format(valor[0]), anchor=NW, font=('Arial 17'), bg=co1, fg='#545454')
  l_sumario.place(x=309,y=70) 

  l_linha = Label(frameMeio,text="",width=215,height=1, anchor=NW, font=('Arial 1'), bg='#545454')
  l_linha.place(x=309,y=132)

  l_sumario = Label(frameMeio,text="Total De Despesas Mensais".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
  l_sumario.place(x=309,y=115)

  l_sumario = Label(frameMeio,text="R$ {:,.2f}".format(valor[1]), anchor=NW, font=('Arial 17'), bg=co1, fg='#545454')
  l_sumario.place(x=309,y=150) 

  l_linha = Label(frameMeio,text="",width=215,height=1, anchor=NW, font=('Arial 1'), bg='#545454')
  l_linha.place(x=309,y=207)

  l_sumario = Label(frameMeio,text="Saldo Total em Caixa     ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
  l_sumario.place(x=309,y=190)

  l_sumario = Label(frameMeio,text="R$ {:,.2f}".format(valor[2]), anchor=NW, font=('Arial 17'), bg=co1, fg='#545454')
  l_sumario.place(x=309,y=220) 



def grafico_pie():
   figura = plt.Figure(figsize=(5, 3), dpi=90)
   ax = figura.add_subplot(111)

   lista_valores = [345,225,534]
   lista_categorias = ['Renda', 'Despesa', 'Saldo']

   explode = []
   for i in lista_categorias:
       explode.append(0.05)
   ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True,startangle=90)
   ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))
   canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie)
   canva_categoria.get_tk_widget().grid(row=0, column=0)












porcentagem()
grafico_bar()
resumo()
grafico_pie()


frame_renda = Frame(frameBaixo,width=300,height=250, bg= co1)
frame_renda.grid(row=0,column=0)

frame_Operaçoes = Frame(frameBaixo,width=220,height=250, bg= co1)
frame_Operaçoes.grid(row=0,column=1,padx=5)

frame_Configuracao = Frame(frameBaixo,width=220,height=250, bg= co1)
frame_Configuracao.grid(row=0,column=2,padx=5)

app_tabela = Label(frameMeio, text="Tabela Receitas/Despesas",anchor=NW, font=('Verdana 12'),bg=co2,fg=co4)
app_tabela.place(x=5,y=309)

def mostrar_renda():
   tabela_head = ['#Id','Categoria','Data','Quantia']
   lista_itens = [[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,2,3,4]]

   global tree
   tree = ttk.Treeview(frame_renda, selectmode="extended",columns=tabela_head, show="headings")
   vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
   hsb = ttk.Scrollbar(frame_renda,orient="horizontal",command=tree.xview)

   tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
   tree.grid(column=0, row=0, sticky='nsew')
   vsb.grid(column=1, row=0, sticky='ns')
   hsb.grid(column=0,row=1,sticky='ew')

   hd=["center", "center", "center", "center"]
   h=[30,100,100,100]
   n=0

   for col in tabela_head:
      tree.heading(col, text=col.title(), anchor=CENTER)
      tree.column(col, width=h[n])

      n+=1
   for item in lista_itens:
      tree.insert('', 'end', values=item)

   

mostrar_renda()


l_info = Label(frame_Operaçoes, text='Insira novas despesas',height=1,anchor=NW, font=('Verdana 10 bold'),bg=co1, fg=co4)
l_info.place(x=10, y=10)
                    
l_categoria = Label(frame_Operaçoes, text='Categoria',height=1,anchor=NW, font=('Ivy 10'),bg=co1, fg=co4)
l_categoria.place(x=10, y=40)

categoria_funcao = ['Viagem', 'Comida']
categoria = []

for i in categoria_funcao:
   categoria.append(i[1])
combo_categoria_despesas = ttk.Combobox(frame_Operaçoes, width=10, font=('Ivy 10'))
combo_categoria_despesas['values'] = (categoria)
combo_categoria_despesas.place(x=110, y=41)


l_cal_despesas = Label(frame_Operaçoes, text='Data',height=1,anchor=NW, font=('Ivy 10'),bg=co1, fg=co4)
l_cal_despesas.place(x=10, y=70)

e_cal_despesas = DateEntry(frame_Operaçoes, widht=12, background='darkblue',foreground='white',borderwidth=2,year=2024)
e_cal_despesas.place(x=110, y=71)

l_valor_despesas = Label(frame_Operaçoes, text='Quantia Total',height=1,anchor=NW, font=('Ivy 10'),bg=co1, fg=co4)
l_valor_despesas.place(x=10, y=100)

e_valor_despesas = Entry(frame_Operaçoes,width=14, justify='left', relief='solid')
e_valor_despesas.place(x=110, y=101)


botao_inserir_despesas = Button(frame_Operaçoes, text="Adicionar".upper(),width=80, compound=LEFT,anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief=RIDGE )
botao_inserir_despesas.place(x=110, y=131)


l_excluir_ = Label(frame_Operaçoes, text='Excluir ação',height=1,anchor=NW, font=('Ivy 10 bold'),bg=co1, fg=co4)
l_excluir_.place(x=10, y=190)


botao_deletar = Button(frame_Operaçoes, text="Deletar".upper(),width=80, compound=LEFT,anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief=RIDGE )
botao_deletar.place(x=110, y=190)


l_info = Label(frame_Configuracao, text='Insira novas receitas',height=1,anchor=NW, font=('Verdana 10 bold'),bg=co1, fg=co4)
l_info.place(x=10, y=10)

l_cal_receitas = Label(frame_Configuracao, text='Data',height=1,anchor=NW, font=('Ivy 10'),bg=co1, fg=co4)
l_cal_receitas.place(x=10, y=40)

e_cal_receitas = DateEntry(frame_Configuracao, widht=12, background='darkblue',foreground='white',borderwidth=2,year=2024)
e_cal_receitas.place(x=110, y=41)

l_valor_receitas = Label(frame_Configuracao, text='Quantia Total',height=1,anchor=NW, font=('Ivy 10'),bg=co1, fg=co4)
l_valor_receitas.place(x=10, y=70)

e_valor_receitas = Entry(frame_Configuracao,width=14, justify='left', relief='solid')
e_valor_receitas.place(x=110, y=71)

botao_inserir_receitas = Button(frame_Configuracao, text="Adicionar".upper(),width=80, compound=LEFT,anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief=RIDGE )
botao_inserir_receitas.place(x=110, y=111)

l_info = Label(frame_Configuracao, text='Categoria',height=1,anchor=NW, font=('Ivy 10 bold'),bg=co1, fg=co4)
l_info.place(x=10, y=160)
e_categoria = Entry(frame_Configuracao,width=14, justify='left', relief='solid')
e_categoria.place(x=110, y=160)
botao_inserir_receitas = Button(frame_Configuracao, text="Adicionar".upper(),width=80, compound=LEFT,anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief=RIDGE )
botao_inserir_receitas.place(x=110, y=190)










janela.mainloop()


